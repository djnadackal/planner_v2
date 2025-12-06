import { useState } from "react";
import useCategoryBuffer from "./categoryBuffer";

const useCategoryModalControl = (api, categoryName, categoryId) => {
  const [addModalOpen, setAddModalOpen] = useState(false);
  const [editModalOpen, setEditModalOpen] = useState(false);
  const [mode, setMode] = useState("add"); // "add" or "edit"
  const buffer = useCategoryBuffer();

  const categoryApi = api[categoryName];

  const modalControl = {
    error:
      categoryApi.selected.error ||
      categoryApi.create.error ||
      categoryApi.update.error,
    loading:
      categoryApi.selected.loading ||
      categoryApi.create.loading ||
      categoryApi.update.loading,
    mode,
    category: buffer,
    add: {
      isOpen: addModalOpen,
      open: () => {
        setMode("add");
        buffer.reset();
        setAddModalOpen(true);
      },
      close: () => setAddModalOpen(false),
      submit: async () => {
        await categoryApi.create.create({
          name: buffer.name,
          description: buffer.description,
          color: buffer.color,
        });
        api.refreshAll();
        buffer.reset();
        setAddModalOpen(false);
      },
    },
    edit: {
      isOpen: editModalOpen,
      open: () => {
        setMode("edit");
        buffer.set.username(categoryApi.selected.data.username);
        setEditModalOpen(true);
      },
      close: () => setEditModalOpen(false),
      submit: async () => {
        await categoryApi.update.update({
          id: categoryId,
          name: buffer.name,
          description: buffer.description,
          color: buffer.color,
        });
        api.refreshAll();
        buffer.reset();
        setEditModalOpen(false);
      },
    },
  };
  return modalControl;
};

export default useCategoryModalControl;
