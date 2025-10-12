import { useEffect, useState } from 'react';
import { Flex } from 'antd';
import api from '../../api/';

import components from '../../components/';
import { useLocation, useNavigate, useParams } from 'react-router-dom';

const {
  ThingTree,
  CommentPanel,
  ActionPanel,
  tables: { TicketTable, ChilrenTable },
  details: { ThingDetails, TicketDetails }
} = components;

const ThingView = () => {

  const {
    thingId,
    ticketId,
    selectedThingId,
    setSelectedThingId,
    checkedThingIds,
    setCheckedThingIds,
    selectedTicketId,
    setSelectedTicketId,
    selectThing,
    thingData,
    thingLoading,
    thingError,
    fetchThing,
    ticketData,
    ticketLoading,
    ticketError,
    location,
    fetchTicket,
    navToTicket,
  } = useThingViewHooks()

  return (<>
    <Flex gap="10px" style={{ overflowY: 'hidden' }}>
      <ThingTree
        rorderable={true}
        checkedThingIds={checkedThingIds}
        setCheckedThingIds={setCheckedThingIds}
        selectedThingId={selectedThingId}
        setSelectedThingId={selectThing} />
      <Flex gap="10px" style={{ height: '100%', minHeight: 0 }} wrap>
        {selectedThingId && <>
          <Flex vertical gap="10px">
            <ThingDetails
              thing={thingData}
              loading={thingLoading}
              error={thingError}
              refreshThing={fetchThing} />
            <ChilrenTable
              selectedThingId={selectedThingId}
              setSelectedThingId={setSelectedThingId} />
          </Flex>
        </>}
        <Flex vertical>
          <Flex style={{
            maxHeight: selectedThingId ? '50%' : '100%',
            minHeight: selectedThingId ? '50%' : '100%'
          }}>
            <TicketTable
              checkedThingIds={selectedThingId ? undefined : checkedThingIds}
              selectedThingId={selectedThingId}
              tableMode={selectedTicketId ? "compact" : "full"}
              onRow={navToTicket} />
          </Flex>
          {ticketId && <TicketDetails
            ticket={ticketData}
            loading={ticketLoading}
            error={ticketError}
            refreshTicket={fetchTicket} />}
        </Flex>
        {selectedTicketId && <Flex
          vertical
          gap="10px"
          style={{ flex: 1, height: "100%" }}>
          <Flex style={{
            maxHeight: '50%',
            minHeight: '50%'
          }}>
            <CommentPanel ticketId={selectedTicketId} />
          </Flex>
          <Flex style={{
            maxHeight: '50%',
            minHeight: '50%'
          }}>
            <ActionPanel ticketId={selectedTicketId} />
          </Flex>
        </Flex>
        }
      </Flex>
    </Flex>
  </>);
}


const useThingViewHooks = () => {
  const [selectedThingId, setSelectedThingId] = useState(null);
  const [selectedTicketId, setSelectedTicketId] = useState(null);
  const [checkedThingIds, setCheckedThingIds] = useState([]);
  const { thingId, ticketId } = useParams();
  console.log({ thingId, ticketId });
  const {
    data: thingData,
    loading: thingLoading,
    error: thingError,
    getThing
  } = api.useFetchThing(thingId);
  const {
    data: ticketData,
    loading: ticketLoading,
    error: ticketError,
    getTicket
  } = api.useFetchTicket(ticketId);
  const navigate = useNavigate();
  const location = useLocation();

  const fetchThing = () => {
    if (selectedThingId) {
      getThing(selectedThingId);
    }
  }

  const fetchTicket = () => {
    if (selectedTicketId) {
      getTicket(selectedTicketId);
    }
  }

  useEffect(() => {
    fetchThing();
  }, [selectedThingId]);

  // Effect to handle route params
  useEffect(() => {
    setSelectedThingId(null);
    setSelectedTicketId(null);

    if (thingId && /^\d+$/.test(thingId)) {
      setSelectedThingId(thingId);
      if (ticketId && /^\d+$/.test(ticketId)) {
        setSelectedTicketId(ticketId);
      }
    }
    // For /things (no params), both remain null
  }, [thingId, ticketId]); // Depend on actual params, not pathname


  const selectThing = (thingId) => {
    setSelectedThingId(thingId);
    if (thingId) {
      navigate(`/${thingId}`);
    } else {
      navigate(`/`);
    }
  }

  const navToTicket = (record) => {
    return {
      onClick: () => {
        setSelectedTicketId(record.id)
        navigate(`/${thingId}/tickets/${record.id}`)
      }
    }
  }

  return {
    thingId,
    ticketId,
    selectedThingId,
    setSelectedThingId,
    selectedTicketId,
    setSelectedThingId,
    checkedThingIds,
    setCheckedThingIds,
    selectThing,
    thingData,
    thingLoading,
    thingError,
    fetchThing,
    ticketData,
    ticketLoading,
    ticketError,
    location,
    fetchTicket,
    navToTicket
  }

}


export default ThingView;
