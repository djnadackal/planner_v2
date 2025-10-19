import useCreateThing from "./create";
import useFetchThing from "./fetchOne";
import useFetchThingTree from "./fetchTree";
import useFetchThings from "./fetchMany";
import useFetchThingCategories from "./fetchCategories";
import useUpdateThing from "./update";

const thingApi = {
  create: useCreateThing,
  fetchOne: useFetchThing,
  fetchTree: useFetchThingTree,
  fetchMany: useFetchThings,
  update: useUpdateThing,
  fetchCategories: useFetchThingCategories,
};

export default thingApi;
