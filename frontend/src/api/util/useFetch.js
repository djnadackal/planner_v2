import { useEffect } from "react";
import useFetchState from "../../util/useFetchState";

const useFetch = (
  rootUrl,
  urlBuilder = (url, params) => url,
  params = {},
  { lazy = false } = {},
) => {
  const { data, setData, loading, setLoading, error, setError, reset } =
    useFetchState(null);

  const fetchData = async (params = {}) => {
    // reset state
    reset();
    // build url
    const url = urlBuilder(new URL(rootUrl, window.location.origin), params);

    // fetch data, manage state
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error on fetch! status: ${response.status}`);
      }
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (!lazy) {
      fetchData(params);
    }
  }, []);

  return { data, loading, error, fetchData };
};

export default useFetch;
