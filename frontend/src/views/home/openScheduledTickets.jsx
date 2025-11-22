import { Card, Table, Flex } from "antd";
import useApi from "../../api";


const OpenScheduledTicketTable = () => {
  const queryParams = {
    scheduled: true,
    open: true,
    include: ['thing', 'user'],
    page_size: 10000,
  }
  const { data, count, loading, error, fetchData } = useApi.ticket.fetchMany(
    queryParams,
  );

  return (
    <Card
      title={`Open Scheduled Tickets (${count ? count : 0})`}
      style={{
        width: 450,
      }}>
      <Flex vertical flex={1} >
        <Table
          dataSource={data ? data : []}
          columns={getColumns()}
          rowHoverable={false}
          scroll={{ y: 400 }}
          pagination={false}
          loading={loading}
          error={error}
          rowKey="id" />
      </Flex>
    </Card>
  )
}


const getColumns = () => {

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
  ]
  const userColumn = {
    title: 'Assigned User',
    dataIndex: ['user', 'username'],
    key: 'user',
  }
  columns.push(userColumn);
  return columns;
}



export default OpenScheduledTicketTable;
