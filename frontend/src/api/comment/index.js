import useFetchComments from "./useFetchComments";
import useCreateComment from "./useCreateComment";

const commentsApi = {
  create: useCreateComment,
  fetchMany: useFetchComments,
};

export default commentsApi;
