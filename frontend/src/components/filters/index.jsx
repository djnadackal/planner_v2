import { Button, Card, Dropdown, Flex, Input } from "antd";
import { FilterOutlined } from "@ant-design/icons";
import UserMultiDropdown from "../inputs/userMultiDropdown";
import useViewNavigation from "../../navigation";
import { useState } from "react";
import MilestoneMultiDropdown from "../inputs/milestoneMultiDropdown";
import TicketCategoryMultiDropdown from "../inputs/ticketCategoryMultiDropdown";

const Filters = () => {
  const navigation = useViewNavigation();
  const [searchValue, setSearchValue] = useState(navigation.getQueryParam.search || '');

  const onSearchChange = (e) => {
    const value = e.target.value;
    setSearchValue(value);
  };

  const onSearchBlur = (e) => {
    const value = e.target.value;
    console.log("Search input blurred, setting search to", value);
    navigation.setQueryParam.search(value || null);
  };

  const handleShowClosedToggle = () => {
    console.log("Setting showClosed to", !navigation.getQueryParam.showClosed);
    if (!navigation.getQueryParam.showClosed) {
      setShowToggleText("Hide Closed");
      navigation.setQueryParam.showClosed(true);
    } else {
      setShowToggleText("Show Closed");
      navigation.setQueryParam.showClosed(false);
    }
  };

  const [showClosedToggleText, setShowToggleText] = useState(
    navigation.getQueryParam.showClosed ? "Hide Closed" : "Show Closed",
  );


  return (
    <Dropdown
      overlay={
        <Card title="Filters">
          <Flex vertical gap="10px">
            <Input
              placeholder="Search"
              onBlur={onSearchBlur}
              style={{ width: 100 }}
              value={searchValue}
              onChange={onSearchChange} />
            <UserMultiDropdown
              selectedUserIds={navigation.getQueryParam.userIds}
              setSelectedUserIds={navigation.setQueryParam.userIds} />
            <MilestoneMultiDropdown
              selectedMilestoneIds={navigation.getQueryParam.milestoneIds}
              setSelectedMilestoneIds={navigation.setQueryParam.milestoneIds} />
            <TicketCategoryMultiDropdown
              selectedCategoryIds={navigation.getQueryParam.ticketCategoryIds}
              setSelectedCategoryIds={navigation.setQueryParam.ticketCategoryIds} />
            <Button
              onClick={handleShowClosedToggle}>
              {showClosedToggleText}
            </Button>
          </Flex >
        </Card>
      }
      trigger={['click']}
      placement="bottomLeft"
    >
      <Button
        icon={<FilterOutlined />}
        style={{ marginLeft: 'auto' }}
      />
    </Dropdown>
  )
}

export default Filters;
