import useFetchComments from "./fetchMany";
import useCreateComment from "./create";

const commentsApi = {
  create: useCreateComment,
  fetchMany: useFetchComments,
};

export default commentsApi;
