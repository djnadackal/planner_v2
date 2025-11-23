import apiUtils from "../util";

const { useFetch } = apiUtils;

const MILESTONES_URL = "/api/milestones/";

const useFetchMilestones = ({
  ticket_id,
  due_date_before,
  due_date_after,
} = {}) => {
  const urlBuilder = (url, params) => {
    const { ticket_id, due_date_before, due_date_after } = params;
    if (ticket_id !== undefined) {
      url.searchParams.append("ticket_id", ticket_id);
    }
    if (due_date_before !== undefined) {
      url.searchParams.append("due_date_before", due_date_before);
    }
    if (due_date_after !== undefined) {
      url.searchParams.append("due_date_after", due_date_after);
    }
    return url;
  };
  const { data, loading, error, fetchData } = useFetch(
    MILESTONES_URL,
    urlBuilder,
    {
      ticket_id,
      due_date_before,
      due_date_after,
    },
  );

  return { data, loading, error, fetchData };
};

export default useFetchMilestones;
