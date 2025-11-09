import { useNavigate, useParams } from "react-router-dom";
import useMutateMilestone from "../../components/details/milestoneModal/mutateMilestoneHooks";
import { useEffect, useState } from "react";
import useApi from "../../api";

const useMilestoneViewHooks = () => {
  // URL State
  const { milestoneId } = useParams();
  const navigate = useNavigate();
  // helpers
  const selectMilestone = (id) => {
    if (id == milestoneId) {
      navigate(`/milestones/`);
    } else {
      navigate(`/milestones/${id}`);
    }
  };
  const selectTicket = (id) => {
    navigate(`/tickets/${id}`);
  };

  // Component State
  const [addMilestoneModalOpen, setAddMilestoneModalOpen] = useState(false);
  const [editMilestoneModalOpen, setEditMilestoneModalOpen] = useState(false);
  const mutateMilestone = useMutateMilestone();

  // API state
  const api = {
    milestone: {
      selected: useApi.milestone.fetchOne(milestoneId),
      list: useApi.milestone.fetchMany(),
      create: useApi.milestone.create(),
      update: useApi.milestone.update(),
    },
    ticket: {
      list: useApi.ticket.fetchMany({ milestone_id: milestoneId }),
    },
  };
  api.refreshAll = () => {
    if (milestoneId) {
      api.milestone.selected.fetchOne(milestoneId);
    }
    api.milestone.list.fetchData();
    if (milestoneId) {
      api.ticket.list.fetchData({ milestone_id: milestoneId });
    }
  };

  // Modal State
  const modalControl = {
    add: {
      isOpen: addMilestoneModalOpen,
      open: () => {
        setAddMilestoneModalOpen(true);
      },
      close: () => {
        mutateMilestone.reset();
        setAddMilestoneModalOpen(false);
      },
      submit: async () => {
        await api.milestone.create.create({
          name: mutateMilestone.name,
          description: mutateMilestone.description,
          due_date: mutateMilestone.due_date,
        });
        api.refreshAll();
        mutateMilestone.reset();
        setAddMilestoneModalOpen(false);
      },
    },
    edit: {
      isOpen: editMilestoneModalOpen,
      open: () => {
        // set the mutateMilestone to the current milestone data
        mutateMilestone.set.name(api.milestone.selected.data.name);
        mutateMilestone.set.description(
          api.milestone.selected.data.description,
        );
        mutateMilestone.set.due_date(api.milestone.selected.data.due_date);
        // then open the modal
        setEditMilestoneModalOpen(true);
      },
      close: () => {
        mutateMilestone.reset();
        setEditMilestoneModalOpen(false);
      },
      submit: async () => {
        await api.milestone.update.update({
          id: milestoneId,
          name: mutateMilestone.name,
          description: mutateMilestone.description,
          due_date: mutateMilestone.due_date,
        });
        api.refreshAll();
        mutateMilestone.reset();
        setEditMilestoneModalOpen(false);
      },
    },
  };

  // refresh all on milestoneId change
  useEffect(() => {
    if (milestoneId) {
      api.refreshAll();
    }
  }, [milestoneId]);

  return {
    milestoneId,
    api,
    select: {
      milestone: selectMilestone,
      ticket: selectTicket,
    },
    modalControl,
    mutateMilestone,
  };
};

export default useMilestoneViewHooks;
