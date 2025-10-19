import apiUtils from "../util";

const { useFetch } = apiUtils;

const THINGS_URL = "/api/things/";

const useFetchThings = ({ parent_id, include } = {}, { lazy = false } = {}) => {
  const urlBuilder = (url, params) => {
    const { parent_id, include } = params;
    if (parent_id !== undefined) {
      url.searchParams.append("parent_id", parent_id);
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
    THINGS_URL,
    urlBuilder,
    { parent_id, include },
    { lazy },
  );

  return { data, loading, error, refetch: fetchData };
};

export default useFetchThings;
