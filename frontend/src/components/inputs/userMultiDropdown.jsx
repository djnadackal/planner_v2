import { Select } from "antd";
import { useEffect } from "react";
import useApi from "../../api/";

const UserMultiDropdown = (
  { selectedUserIds, setSelectedUserIds, filters, placeholder = "Select Users" }
) => {
  const {
    data,
    loading,
    error,
    fetchData
  } = useApi.user.fetchMany({
    ...filters,
    page_size: filters?.page_size || 10000,
    page_number: 1
  });

  const handleChange = (value) => {
    console.log("value selected in UserMultiDropdown:", value);
    setSelectedUserIds(value);
  };

  useEffect(() => {
    fetchData(filters);
  }, [filters]);

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
      value={selectedUserIds || []}
      filterOption={(input, option) =>
        (option?.label ?? '').toLowerCase().includes(input.toLowerCase())
      }
      options={data ? [...data, { username: "No User", id: 0 }].map(user => ({
        label: user.username,
        value: user.id
      })) : []}
    />
  );
}


export default UserMultiDropdown;
