import apiUtils from "../util";

const { useFetch } = apiUtils;

const THING_CATEGORIES_URL = "/api/things/categories/";

const useFetchThingCategories = () => {
  const { data, loading, error, fetchData } = useFetch(THING_CATEGORIES_URL);

  return { data, loading, error, refetch: fetchData };
};

export default useFetchThingCategories;
