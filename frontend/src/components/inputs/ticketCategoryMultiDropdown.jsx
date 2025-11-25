import { Select } from "antd";
import { useEffect } from "react";
import useApi from "../../api/";

const TicketCategoryMultiDropdown = ({ selectedCategoryIds, setSelectedCategoryIds }) => {
  const { data, loading, error } = useApi.ticket.fetchCategories();

  const handleChange = (value) => {
    console.log("value selected in TicketCategoryMultiDropdown:", value);
    setSelectedCategoryIds(value);
  };

  console.log("selectedCategoryIds:", selectedCategoryIds);

  return (
    <Select
      showSearch
      mode="multiple"
      loading={loading}
      style={{ width: 200 }}
      placeholder="Select categories"
      optionFilterProp="children"
      error={error}
      onChange={handleChange}
      value={selectedCategoryIds || []}
      allowClear
      onClear={() => handleChange(null)}
      filterOption={(input, option) =>
        (option?.label ?? '').toLowerCase().includes(input.toLowerCase())
      }
      options={data ? data.map(ticketCategory => ({
        label: ticketCategory.name,
        value: ticketCategory.id
      })) : []}
    />
  );
}


export default TicketCategoryMultiDropdown;
