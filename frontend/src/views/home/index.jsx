import { Card, Flex } from "antd";
import OpenScheduledTicketTable from "./openScheduledTickets";
import MilestonePastDueTickets from "./milestonePastDueTickets";
import UserTicketsPie from "./userTicketsPie";
import TopThingTicketsPie from "./topThingTicketsPie";


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
