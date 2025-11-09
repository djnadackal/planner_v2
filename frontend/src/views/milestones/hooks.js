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

  // API Hooks
  const {
    data: milestoneData,
    loading: milestoneLoading,
    error: milestoneError,
    fetchOne: fetchMilestone,
  } = useApi.milestone.fetchOne(milestoneId);
  const {
    data: ticketData,
    loading: ticketLoading,
    error: ticketError,
    refetch: fetchTickets,
  } = useApi.ticket.fetchMany({ milestone_id: milestoneId });
  const {
    data: milestonesData,
    loading: milestonesLoading,
    error: milestonesError,
    fetchData: fetchMilestones,
  } = useApi.milestone.fetchMany();
  const {
    data: createMilestoneData,
    loading: createMilestoneLoading,
    error: createMilestoneError,
    create: createMilestone,
  } = useApi.milestone.create();
  const {
    data: updateMilestoneData,
    loading: updateMilestoneLoading,
    error: updateMilestoneError,
    update: updateMilestone,
  } = useApi.milestone.update();
  // Refreshers
  const refreshMilestone = () => {
    if (milestoneId) {
      fetchMilestone(milestoneId);
    }
  };
  const refreshTickets = () => {
    if (milestoneId) {
      fetchTickets({ milestone_id: milestoneId });
    }
  };
  useEffect(() => {
    if (milestoneId) {
      refreshMilestone();
      refreshTickets();
    }
  }, [milestoneId]);
  return {
    milestoneId,
    selectMilestone,
    selectTicket,
    addMilestoneModalOpen,
    editMilestoneModalOpen,
    setAddMilestoneModalOpen,
    setEditMilestoneModalOpen,
    mutateMilestone,
    milestoneData,
    milestoneLoading,
    milestoneError,
    fetchMilestone,
    refreshMilestone,
    milestonesData,
    milestonesLoading,
    milestonesError,
    fetchMilestones,
    ticketData,
    ticketLoading,
    ticketError,
    fetchTickets,
    createMilestoneData,
    createMilestoneLoading,
    createMilestoneError,
    createMilestone,
    updateMilestoneData,
    updateMilestoneLoading,
    updateMilestoneError,
    updateMilestone,
  };
};

export default useMilestoneViewHooks;
