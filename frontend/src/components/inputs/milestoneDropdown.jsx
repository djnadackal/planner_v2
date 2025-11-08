import { Select } from "antd";
import { useEffect } from "react";
import useApi from "../../api/";

const MilestoneDropdown = ({ selectedMilestoneId, setSelectedMilestoneId, filters }) => {
  const { data, loading, error, fetchData } = useApi.milestone.fetchMany(filters);

  const handleChange = (value) => {
    console.log("value selected in MilestoneDropdown:", value);
    setSelectedMilestoneId(value);
  };

  useEffect(() => {
    fetchData(filters);
  }, [filters]);

  return (
    <Select
      showSearch
      style={{ width: "150px" }}
      placeholder="Add"
      error={error}
      onChange={handleChange}
      value={selectedMilestoneId}
      filterOption={(input, option) =>
        (option?.label ?? '').toLowerCase().includes(input.toLowerCase())
      }
      options={data ? data.map(thing => ({
        label: thing.name,
        value: thing.id
      })) : []}
    />
  );
}


export default MilestoneDropdown;
