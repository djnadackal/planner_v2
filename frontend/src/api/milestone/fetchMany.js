import apiUtils from "../util";

const { useFetch } = apiUtils;

const MILESTONES_URL = "/api/milestones/";

const useFetchMilestones = ({ ticket_id } = {}) => {
  const urlBuilder = (url, params) => {
    const { ticket_id } = params;
    if (ticket_id !== undefined) {
      url.searchParams.append("ticket_id", ticket_id);
    }
    return url;
  };
  const { data, loading, error, fetchData } = useFetch(
    MILESTONES_URL,
    urlBuilder,
    { ticket_id },
  );

  return { data, loading, error, fetchData };
};

export default useFetchMilestones;
