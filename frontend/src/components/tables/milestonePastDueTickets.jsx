import useApi from '../../api';
import { useEffect, useState } from 'react';
import getColumns from '../../tableColumns/getTicketTableColumns';
import { Card, Flex, Table } from 'antd';

const MilestonePastDueTickets = () => {
  const [milestoneIds, setMilestoneIds] = useState([]);

  const pastDueMilestoneParams = {
    due_date_before: new Date().toISOString(),
  }

  const openPastDueTicketParams = {
    open: true,
    milestone_ids: [], // to be filled after fetching past due milestones
    include: ['thing', 'user', 'category'],
  };

  const api = {
    milestones: {
      list: useApi.milestone.fetchMany(pastDueMilestoneParams),
    },
    tickets: {
      pastDue: useApi.ticket.fetchMany(openPastDueTicketParams, { lazy: true }),
    },
  };

  useEffect(() => {
    console.log("Fetched milestones:", api.milestones.list.data);
    if (api.milestones.list.data) {
      setMilestoneIds(
        api.milestones.list.data.map((m) => m.id),
      );
    }
  }, [api.milestones.list.loading]);

  useEffect(() => {
    if (milestoneIds.length > 0) {
      console.log("Fetching past due tickets for milestones:", milestoneIds);
      api.tickets.pastDue.fetchData({
        ...openPastDueTicketParams,
        milestone_ids: milestoneIds,
      });
    }
  }, [milestoneIds]);

  const cols = ["Title", "Thing", "Category", "Assigned User"];

  return (
    <Card
      title={"Current Todos"}
      style={{
        marginTop: "10px",
        width: 500
      }}>
      <Flex vertical flex={1} >
        <Table
          dataSource={api.tickets.pastDue.data ? api.tickets.pastDue.data : []}
          columns={getColumns(cols)}
          pagination={false}
          scroll={{ y: 400 }}
          loading={api.tickets.pastDue.loading}
          error={api.tickets.pastDue.error}
          rowKey="id" />
      </Flex>
    </Card>
  );
}

export default MilestonePastDueTickets;
