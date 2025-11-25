import { Select } from "antd";
import { useEffect } from "react";
import useApi from "../../api/";

const MilestoneMultiDropdown = (
  { selectedMilestoneIds, setSelectedMilestoneIds, filters, placeholder = "Select Milestones" }
) => {
  const params = {
    ...filters,
    page_size: filters?.page_size || 10000,
    page_number: 1
  }
  const { data, loading, error, fetchData } = useApi.milestone.fetchMany(params);

  const handleChange = (value) => {
    console.log("value selected in MilestoneMultiDropdown:", value);
    setSelectedMilestoneIds(value);
  };

  useEffect(() => {
    fetchData(params);
  }, [filters]);

  console.log("selectedMilestoneIds:", selectedMilestoneIds);

  return (
    <Select
      showSearch
      mode="multiple"
      style={{ width: "150px" }}
      placeholder={placeholder}
      allowClear
      onClear={() => handleChange(null)}
      error={error}
      onChange={handleChange}
      value={selectedMilestoneIds || []}
      filterOption={(input, option) =>
        (option?.label ?? '').toLowerCase().includes(input.toLowerCase())
      }
      options={data ? data.map(milestone => ({
        label: milestone.name,
        value: milestone.id
      })) : []}
    />
  );
}


export default MilestoneMultiDropdown;
