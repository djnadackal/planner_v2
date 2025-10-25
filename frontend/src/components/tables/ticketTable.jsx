import { useEffect, useState } from "react";
import { Button, Card, Table, Flex } from "antd";
import { gray, grey } from "@ant-design/colors";
import useApi from "../../api/";
import "../../App.css";


const TicketTable = ({
  checkedThingIds,
  selectedThingId,
  tableMode,
  onRow,
  selectedTicketId,
  beginAddTicket,
  scrollHeight
}) => {

  const {
    data,
    loading,
    error,
    doRefetch,
    showClosedToggleText,
    handleShowClosedToggle
  } = useTicketTableHooks(checkedThingIds, selectedThingId, tableMode);

  return (
    <Card
      title={`Tickets (${data ? data.length : 0})`}
      style={{
        marginTop: "10px",
        width: tableMode === "compact" ? 500 : 800
      }}
      extra={beginAddTicket && <Flex gap="10px">
        <Button
          onClick={handleShowClosedToggle}>
          {showClosedToggleText}
        </Button>
        <Button
          type="primary"
          onClick={beginAddTicket}>
          Add Ticket
        </Button>
      </Flex>}>
      <Table
        dataSource={data ? data : []}
        columns={getColumns(tableMode)}
        scroll={{ y: scrollHeight ? scrollHeight : 600 }}
        rowClassName={(record) => {
          // if its selected, highlight it
          if (record.id === selectedTicketId) return "selected-row";
          // if its closed, gray it out
          if (!record.open) return "grey-row"
        }}
        loading={loading}
        error={error}
        onRow={onRow}
        rowKey="id" />
    </Card>
  )
}


const getColumns = (mode = "full") => {

  const formatDate = (dateString) => {
    const options = {
      year: 'numeric',
      month: 'numeric',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    };
    return new Date(dateString).toLocaleDateString(undefined, options);
  }

  const columns = [
    {
      title: 'Title',
      dataIndex: 'title',
      key: 'title',
    },
    {
      title: 'Thing',
      dataIndex: ['thing', 'name'],
      key: 'thing_name',
    },
    {
      title: 'Category',
      dataIndex: ['category', 'name'],
      key: 'category_name',
    },
  ]
  if (mode === "compact") return columns;
  const createdColumn = {
    title: 'Created',
    dataIndex: 'created_at',
    key: 'created_at',
    render: (text) => formatDate(text),
  }
  const updatedColumn = {
    title: 'Updated',
    dataIndex: 'updated_at',
    key: 'updated_at',
    render: (text) => formatDate(text),
  }
  columns.push(createdColumn);
  columns.push(updatedColumn);
  return columns;
}

const useTicketTableHooks = (checkedThingIds, selectedThingId, tableMode) => {
  // initialize query params for consistency throughout component
  const [showClosed, setShowClosed] = useState(false);
  const [showClosedToggleText, setShowToggleText] = useState("Show Closed");
  const queryParams = {
    thing_ids: selectedThingId ? [selectedThingId] : checkedThingIds ? checkedThingIds : [],
    include: ["thing", "category"],
    open: showClosed ? undefined : true,
  }
  // initialize state
  const { data, loading, error, refetch } = useApi.ticket.fetchMany(queryParams, { lazy: true });

  // set default table mode
  if (!tableMode) tableMode = "full"; // other option is "compact"

  //helper function
  const doRefetch = () => {
    refetch(queryParams);
  }

  // onclick for the show closed button
  const handleShowClosedToggle = () => {
    console.log("Setting showClosed to", !showClosed);
    if (!showClosed) {
      setShowToggleText("Hide Closed");
      setShowClosed(true);
    } else {
      setShowToggleText("Show Closed");
      setShowClosed(false);
    }
  }

  // on mount and when checkedThingIds or selectedThingId changes, refetch data
  useEffect(() => {
    doRefetch();
  }, [checkedThingIds, selectedThingId, showClosed]);
  return { data, loading, error, doRefetch, handleShowClosedToggle, showClosedToggleText };
}

export default TicketTable;
