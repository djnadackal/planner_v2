export const formatDate = (dateString, compact = false) => {
  const options = {
    month: "numeric",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  };
  if (!compact) {
    options.year = "numeric";
  }
  return new Date(dateString).toLocaleDateString(undefined, options);
};
