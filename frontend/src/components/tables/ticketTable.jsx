import { useEffect, useState } from "react";
import { Table } from "antd";
import api from "../../api/";


const TicketTable = ({ checkedThingIds, selectedThingId }) => {
  const { data, loading, error, refetch } = api.useFetchTickets(checkedThingIds);

  const [tableMode, setTableMode] = useState("full");

  useEffect(() => {
    if (!selectedThingId) {
      setTableMode("full");
      refetch(checkedThingIds)
    }
  }, [checkedThingIds, selectedThingId])

  useEffect(() => {
    if (selectedThingId) {
      setTableMode("compact");
      refetch([selectedThingId])
    } else {
      setTableMode("full");
      refetch(checkedThingIds)
    }
  }, [selectedThingId])

  return (
    <Table
      title={() => `Tickets (${data ? data.length : 0})`}
      dataSource={data ? data : []}
      columns={getColumns(tableMode)}
      loading={loading}
      error={error}
      rowKey="id" />
  )
}


const getColumns = (mode = "full") => {
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
  }
  const updatedColumn = {
    title: 'Updated',
    dataIndex: 'updated_at',
    key: 'updated_at',
  }
  columns.push(createdColumn);
  columns.push(updatedColumn);
  return columns;
}

export default TicketTable;
