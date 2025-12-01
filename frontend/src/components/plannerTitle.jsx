import { Dropdown, Typography } from "antd";
import { useNavigate } from "react-router-dom";
import { useNavBarProps } from "./navbar";

const PlannerTitle = () => {
  const navigate = useNavigate();
  const navBarProps = useNavBarProps();
  return (
    <Dropdown
      menu={navBarProps}
      placement="bottomLeft"
      trigger={['hover']}>
      <Typography.Title
        style={{
          color: 'white',
          margin: 0,
          marginRight: '25px',
          cursor: 'pointer',
        }}
        level={3}
        onClick={() => navigate('/')}
      >
        Planner
      </Typography.Title>
    </Dropdown>
  )
}

export default PlannerTitle;
