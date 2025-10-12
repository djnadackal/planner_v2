import { Select } from "antd";
import { useEffect } from "react";
import api from "../../api/";

const ThingCategoryDropdown = ({ selectedThingCategoryId, setSelectedThingCategoryId }) => {
  const { data, loading, error, refetch } = api.useFetchThingCategories();

  const handleChange = (value) => {
    console.log("value selected in ThingCategoryDropdown:", value);
    setSelectedThingCategoryId(value);
  };

  return (
    <Select
      showSearch
      style={{ width: 200 }}
      placeholder="Select a category"
      optionFilterProp="children"
      error={error}
      onChange={handleChange}
      value={selectedThingCategoryId}
      allowClear
      filterOption={(input, option) =>
        (option?.label ?? '').toLowerCase().includes(input.toLowerCase())
      }
      options={data ? data.map(thingCategory => ({
        label: thingCategory.name,
        value: thingCategory.id
      })) : []}
    />
  );
}


export default ThingCategoryDropdown;
