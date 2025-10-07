import { Button, Descriptions, Input } from "antd"
import { useEffect, useState } from "react";


const ThingDetails = ({ thing, loading, error }) => {
  const {
    mode,
    setMode,
    changeHandler,
    getValue
  } = detailsHooks(thing);

  useEffect(() => {
    if (mode === "view") {
      console.log("Resetting unsaved changes");

    }
  }, [mode])
  return (
    <Descriptions
      title="Thing Details"
      column={1}
      loading={loading}
      error={error}
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
      size="small">
      <Descriptions.Item label="Name">
        {mode === "view" ?
          thing?.name :
          <Input
            value={getValue("name")}
            onChange={changeHandler("name")} />}
      </Descriptions.Item>
      <Descriptions.Item label="Docs Link">
        {mode === "view" ?
          (thing?.docs_link ?
            <a
              href={thing?.docs_link}
              target="_blank"
              rel="noopener noreferrer">
              {thing?.docs_link}
            </a> :
            'No link') :
          <Input
            value={getValue("docs_link")}
            onChange={changeHandler("docs_link")} />}
      </Descriptions.Item>
      <Descriptions.Item label="category">
        {mode === "view" ?
          (thing?.category ? thing.category.name : 'No category') :
          <Input
            value={getValue("category")}
            onChange={changeHandler("category")} />}
      </Descriptions.Item>
      <Descriptions.Item label="Parent">
        {mode === "view" ?
          (thing?.parent ? thing.parent.name : 'No parent') :
          <Input
            value={getValue("parent")}
            onChange={changeHandler("parent")} />}
      </Descriptions.Item>
      <Descriptions.Item label="Description">
        {mode === "view" ?
          (thing?.description ? thing.description : 'No description') :
          <Input.TextArea
            value={getValue("description")}
            onChange={changeHandler("description")}
            autoSize={{ minRows: 3, maxRows: 5 }} />}
      </Descriptions.Item>
    </Descriptions>
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
  console.log("mode in ModeButton:", mode);
  return (
    <Button type="primary" onClick={onClick}>
      {mode === "view" ? "Edit" : "Cancel"}
    </Button>
  )
}

const detailsHooks = (thing) => {
  const [mode, setMode] = useState("view"); // "view", "edit" or "create"
  const [unsavedChanges, setUnsavedChanges] = useState({});

  const isChanged = (field) => {
    return unsavedChanges[field] !== undefined;
  }

  console.log("mode is ", mode);

  const changeHandler = (field) => {
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
  return { mode, setMode, changeHandler, getValue };
}

export default ThingDetails;
