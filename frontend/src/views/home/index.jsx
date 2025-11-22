import { Card, Flex } from "antd";
import components from "../../components";
import useHomeViewHooks from "./hooks";
import useApi from "../../api";
import OpenScheduledTicketTable from "./openScheduledTickets";


const {
  tables: { MilestonePastDueTickets },
  details: { MilestoneDetails, MilestoneModal },
  Charts: { UserTicketsPie, TopThingTicketsPie }
} = components;

const HomeView = () => {
  return (
    <Flex vertical gap="10px">
      <Flex gap="10px">
        <Card
          title="Open Tickets by User"
          style={{ minHeight: "400px" }}>
          <UserTicketsPie />
        </Card>
        <Card
          title="Open Tickets by Top Things"
          style={{ minHeight: "400px" }}>
          <TopThingTicketsPie />
        </Card>
        <OpenScheduledTicketTable />
      </Flex>
      <Flex gap="10px">
        <MilestonePastDueTickets />
      </Flex>
    </Flex>
  );
}

export default HomeView;
