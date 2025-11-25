const useTicketQueryParams = (queryParams) => {
  const pageSize = queryParams.pageSize || 25;
  const pageNumber = queryParams.pageNumber || 1;
  return {
    thing_ids: queryParams.thingIds,
    include: ["thing", "category", "user"],
    search: queryParams.search || undefined,
    category_id: queryParams.ticketCategoryId || undefined,
    category_ids: queryParams.ticketCategoryIds,
    open: queryParams.showClosed ? undefined : true,
    milestone_id: queryParams.milestoneId || undefined,
    milestone_ids: queryParams.milestoneIds,
    schedule_id: queryParams.scheduleId || undefined,
    user_id: queryParams.userId || undefined,
    user_ids: queryParams.userIds,
    page_number: pageNumber,
    page_size: pageSize,
  };
};

export default useTicketQueryParams;
