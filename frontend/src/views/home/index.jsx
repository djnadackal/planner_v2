import { useEffect, useState } from 'react';
import { Flex } from 'antd';
import ThingTree from './thingTree';
import IssueTable from './ticketTable';
import ThingDetails from './thingDetails';
import useGetThing from "./getThing";

const HomeView = () => {
  const [checkedThingIds, setCheckedThingIds] = useState([]);
  const [selectedThingId, setSelectedThingId] = useState(null);
  const { data, loading, error, getThing } = useGetThing();

  console.log("selectedThingId in HomeView:", selectedThingId);

  useEffect(() => {
    if (selectedThingId) {
      getThing(selectedThingId);
    }
  }, [selectedThingId]);

  return (<>
    <Flex
      gap="10px"
      style={{ height: '100%', width: '100%' }}>
      <ThingTree
        checkedThingIds={checkedThingIds}
        setCheckedThingIds={setCheckedThingIds}
        selectedThingId={selectedThingId}
        setSelectedThingId={setSelectedThingId} />
      <Flex gap="10px" style={{ height: '100%' }}>
        {selectedThingId &&
          <ThingDetails
            thing={data}
            loading={loading}
            error={error} />
        }
        <IssueTable
          checkedThingIds={checkedThingIds}
          selectedThingId={selectedThingId} />
      </Flex>
    </Flex>
  </>);
}


export default HomeView;
