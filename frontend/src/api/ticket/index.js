import useCreateTicket from "./create";
import useFetchTicket from "./fetchOne";
import useFetchTickets from "./fetchMany";
import useFetchTicketCategories from "./fetchCategories";
import useUpdateTicket from "./update";

const ticketApi = {
  create: useCreateTicket,
  fetchOne: useFetchTicket,
  fetchMany: useFetchTickets,
  update: useUpdateTicket,
  fetchCategories: useFetchTicketCategories,
};

export default ticketApi;
