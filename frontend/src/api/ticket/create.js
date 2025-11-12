import apiUtils from "../util";

const { useCreate } = apiUtils;

const TICKET_CREATE_URL = "/api/tickets/";

const useCreateTicket = () => {
  const { data, loading, error, create } = useCreate(TICKET_CREATE_URL);
  return { data, loading, error, create };
};

export default useCreateTicket;
