import useCreateAction from "./create";
import useFetchActions from "./fetchMany";
import useFetchActionTypes from "./fetchTypes";

const actionApi = {
  create: useCreateAction,
  fetchMany: useFetchActions,
  fetchTypes: useFetchActionTypes,
};

export default actionApi;
