import { useState } from "react";

const useCategoryBuffer = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [color, setColor] = useState("");
  const userModalReset = () => {
    setName("");
    setDescription("");
    setColor("");
  };
  const buffer = {
    name,
    description,
    color,
    set: {
      name: setName,
      description: setDescription,
      color: setColor,
    },
    reset: userModalReset,
  };
  return buffer;
};

export default useCategoryBuffer;
