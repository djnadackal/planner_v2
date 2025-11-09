import useCreateUser from "./create";
import useFetchUsers from "./fetchMany";
import useFetchUser from "./fetchOne";
import useUpdateUser from "./update";

const userApi = {
  create: useCreateUser,
  fetchMany: useFetchUsers,
  fetchOne: useFetchUser,
  update: useUpdateUser,
};

export default userApi;
