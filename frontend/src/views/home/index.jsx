import { useState } from 'react';
import { Flex } from 'antd';
import ThingTree from './thingTree';
import IssueTable from './ticketTable';

const HomeView = () => {
  const [selectedThingIds, setSelectedThingIds] = useState([]);

  return (<>
    <Flex
      gap="10px"
      style={{ height: '100%', width: '100%' }}>
      <ThingTree
        selectedThingIds={selectedThingIds}
        setSelectedThingIds={setSelectedThingIds} />
      <IssueTable selectedThingIds={selectedThingIds} />
    </Flex>
  </>);
}


export default HomeView;
