import { useEffect, useState } from 'react';
import { Tree } from 'antd';
import useTreeData from './thingTreeHook';


const ThingTree = ({ selectedThingIds, setSelectedThingIds }) => {
  const [keysChanged, setKeysChanged] = useState(false);
  const {
    data, allIds, loading, error
  } = useTreeData();
  useEffect(() => {
    if (allIds.length > 0 && selectedThingIds.length === 0 && !keysChanged) {
      setSelectedThingIds(allIds);
    }
  }, [allIds]);
  const onCheck = (checkedKeys) => {
    setKeysChanged(true);
    setSelectedThingIds(checkedKeys);
  };
  return (
    <Tree
      checkable
      checkedKeys={selectedThingIds}
      onCheck={onCheck}
      defaultExpandAll={true}
      error={error}
      loading={loading}
      treeData={data}
      style={{
        height: '100%',
        padding: '10px',
        minWidth: '250px',
      }}
    />
  );
};
export default ThingTree;
