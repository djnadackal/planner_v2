import { Button, Card, Checkbox, Descriptions, Flex, Input } from "antd"
import { useEffect, useState } from "react";
import api from "../../api/";


const TicketDetails = ({ ticket, loading, error, refreshTicket }) => {
  const {
    mode,
    setMode,
    changeHandler,
    getValue,
    resetChanges,
    updateData,
    updateLoading,
    updateError,
    updateThing
  } = detailsHooks(ticket, refreshTicket, loading, error);


  return (
    <Card
      title="Ticket Details"
      extra={
        <ModeButton
          mode={mode}
          setMode={setMode} />
      }
      style={{
        marginTop: '10px',
        padding: '10px',
        width: '250px',
      }}
    >
      <Flex vertical>
        <Descriptions
          column={1}
          error={error}
          size="small">
          <Descriptions.Item label="Title">
            {mode === "view" ?
              ticket?.title :
              <Input
                value={getValue("title")}
                onChange={changeHandler("title")} />}
          </Descriptions.Item>
          <Descriptions.Item label="Open">
            {mode === "view" ?
              (ticket?.open ? 'Yes' : 'No') :
              <Checkbox
                checked={getValue("open")}
                onChange={changeHandler("open")} />}
          </Descriptions.Item>
          <Descriptions.Item label="category">
            {mode === "view" ?
              (ticket?.category ? ticket.category.name : 'No category') :
              <Input
                value={getValue("category")}
                onChange={changeHandler("category")} />}
          </Descriptions.Item>
          <Descriptions.Item label="Parent">
            {mode === "view" ?
              (ticket?.parent ? ticket.parent.name : 'No parent') :
              <Input
                value={getValue("parent")}
                onChange={changeHandler("parent")} />}
          </Descriptions.Item>
          <Descriptions.Item label="Description">
            {mode === "view" ?
              (ticket?.description ? ticket.description : 'No description') :
              <Input.TextArea
                value={getValue("description")}
                onChange={changeHandler("description")}
                autoSize={{ minRows: 3, maxRows: 5 }} />}
          </Descriptions.Item>
        </Descriptions>
        <Flex justify="end">
          {mode === "edit" &&
            <Button
              type="primary"
              onClick={() => {
                const updatedThing = {
                  id: ticket.id,
                  name: getValue("name"),
                  docs_link: getValue("docs_link"),
                  category: getValue("category"),
                  parent: getValue("parent"),
                  description: getValue("description"),
                };
                console.log("Updating thing with data:", updatedThing);
                updateThing(updatedThing);
              }}>
              Save
            </Button>}
        </Flex>
      </Flex>
    </Card>
  )
}

const ModeButton = ({ mode, setMode }) => {
  const onClick = () => {
    if (mode === "view") {
      setMode("edit");
    } else {
      setMode("view");
    }
  }
  return (
    <Button type="primary" onClick={onClick}>
      {mode === "view" ? "Edit" : "Cancel"}
    </Button>
  )
}

const detailsHooks = (thing, refreshTicket, loading, error) => {
  const [mode, setMode] = useState("view"); // "view" or "edit"
  const [unsavedChanges, setUnsavedChanges] = useState({});

  const {
    data: updateData,
    loading: updateLoading,
    error: updateError,
    updateThing
  } = api.useUpdateTicket();

  // when going to view mode, reset unsaved changes
  useEffect(() => {
    if (mode === "view") {
      // Reset unsaved changes when switching back to view mode
      resetChanges();
    }
  }, [mode])

  // when updateData is available, refresh the thing details
  useEffect(() => {
    if (updateData) {
      console.log("Thing updated:", updateData);
      refreshTicket();
      setMode("view");
    }
  }, [updateLoading])

  const isChanged = (field) => {
    return unsavedChanges[field] !== undefined;
  }

  const changeHandler = (field) => {
    if (field === "open") {
      return (e) => {
        const newValue = e.target.checked;
        setUnsavedChanges({
          ...unsavedChanges,
          [field]: newValue,
        });
      }
    }
    return (e) => {
      const newValue = e.target.value;
      setUnsavedChanges({
        ...unsavedChanges,
        [field]: newValue,
      });
    }
  }

  const getValue = (field) => {
    return isChanged(field) ? unsavedChanges[field] : thing ? thing[field] : '';
  }

  const resetChanges = () => {
    setUnsavedChanges({});
  }
  return {
    mode,
    setMode,
    changeHandler,
    getValue,
    resetChanges,
    updateData,
    updateLoading,
    updateError,
    updateThing

  };
}

export default TicketDetails;
