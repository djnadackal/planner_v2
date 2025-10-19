import apiUtils from "../util";

const { useFetch } = apiUtils;

const ACTIONS_URL = "/api/actions/";

const useFetchActions = (
  { ticket_id, include } = {},
  { lazy = false } = {},
) => {
  const urlBuilder = (url, params) => {
    const { ticket_id, include } = params;
    if (ticket_id !== undefined) {
      url.searchParams.append("ticket_id", ticket_id);
    }

    // set the include param if provided
    // include can be a string or an array of strings
    if (include) {
      if (Array.isArray(include)) {
        include.forEach((inc) => url.searchParams.append("include", inc));
      } else {
        url.searchParams.append("include", include);
      }
    }
    return url;
  };

  const { data, loading, error, fetchData } = useFetch(
    ACTIONS_URL,
    urlBuilder,
    { ticket_id, include },
    { lazy },
  );

  return { data, loading, error, refetch: fetchData };
};

export default useFetchActions;
