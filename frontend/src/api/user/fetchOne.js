import apiUtils from "../util";

const { useFetchOne } = apiUtils;

// url
const USER_GET_URL = "/api/users";

const useFetchUser = (userId = undefined) => {
  const { data, loading, error, fetchOne } = useFetchOne(USER_GET_URL, userId);

  // return state and the fetch function
  return { data, loading, error, fetchOne };
};

export default useFetchUser;
