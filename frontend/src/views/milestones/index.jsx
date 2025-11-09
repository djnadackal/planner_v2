import { Flex } from "antd";
import components from "../../components";
import useMilestoneViewHooks from "./hooks";


const {
  tables: { MilestoneList, TicketList },
  details: { MilestoneDetails, MilestoneModal },
} = components;

const MilestoneView = () => {
  const hooks = useMilestoneViewHooks();
  return (<>
    <Flex style={{ height: '100%' }} gap="10px">
      <MilestoneList
        milestoneId={hooks.milestoneId}
        milestones={hooks.milestonesData || []}
        loading={hooks.milestonesLoading}
        createLoading={hooks.createMilestoneLoading}
        createCallback={() => hooks.setAddMilestoneModalOpen(true)}
        selectMilestone={(milestoneId) => hooks.selectMilestone(milestoneId)} />
      {hooks.milestoneId &&
        <MilestoneDetails
          milestone={hooks.milestoneData}
          editCallback={() => {
            // set the mutateMilestone to the current milestone data
            hooks.mutateMilestone.set.name(hooks.milestoneData.name);
            hooks.mutateMilestone.set.description(hooks.milestoneData.description);
            hooks.mutateMilestone.set.due_date(hooks.milestoneData.due_date);
            // then open the modal
            hooks.setEditMilestoneModalOpen(true);
          }}
        />
      }
      {hooks.milestoneId &&
        <TicketList
          tickets={hooks.ticketData || []}
          ticketsLoading={hooks.ticketLoading}
          selectTicket={hooks.selectTicket} />}
    </Flex>
    <MilestoneModal
      title="New Milestone"
      open={hooks.addMilestoneModalOpen}
      onOk={async () => {
        await hooks.createMilestone({
          name: hooks.mutateMilestone.name,
          description: hooks.mutateMilestone.description,
          due_date: hooks.mutateMilestone.due_date,
        });
        hooks.fetchMilestones();
        hooks.mutateMilestone.reset();
        hooks.refreshMilestone();
        hooks.setAddMilestoneModalOpen(false)
      }}
      onCancel={() => {
        hooks.mutateMilestone.reset();
        hooks.setAddMilestoneModalOpen(false)
      }}
      milestone={hooks.mutateMilestone} />
    <MilestoneModal
      title="Edit Milestone"
      open={hooks.editMilestoneModalOpen}
      onOk={async () => {
        await hooks.updateMilestone({
          id: hooks.milestoneId,
          name: hooks.mutateMilestone.name,
          description: hooks.mutateMilestone.description,
          due_date: hooks.mutateMilestone.due_date,
        });
        hooks.fetchMilestones();
        hooks.mutateMilestone.reset();
        hooks.refreshMilestone();
        hooks.setEditMilestoneModalOpen(false)
      }}
      onCancel={() => {
        hooks.mutateMilestone.reset();
        hooks.setEditMilestoneModalOpen(false)
      }}
      milestone={hooks.mutateMilestone} />
  </>)
}


export default MilestoneView;
