import useCreateAction from "./useCreateAction";
import useFetchActions from "./useFetchActions";
import useFetchActionTypes from "./useFetchActionTypes";

const actionApi = {
  create: useCreateAction,
  fetchMany: useFetchActions,
  fetchTypes: useFetchActionTypes,
};

export default actionApi;
