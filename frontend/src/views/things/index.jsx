import { useEffect, useState } from 'react';
import { Flex } from 'antd';
import api from '../../api/';

import components from '../../components/';
import { useLocation, useNavigate, useParams } from 'react-router-dom';

const {
  ThingTree,
  tables: { TicketTable, ChilrenTable },
  details: { ThingDetails, TicketDetails }
} = components;

const ThingView = () => {

  const {
    thingId,
    ticketId,
    selectedThingId,
    setSelectedThingId,
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
    <Flex
      gap="10px"
      style={{ height: '100%', width: '100%' }}>
      <ThingTree
        selectedThingId={selectedThingId}
        setSelectedThingId={selectThing} />
      <Flex gap="10px" style={{ height: '100%' }} wrap>
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
        <TicketTable
          selectedThingId={selectedThingId}
          tableMode={"compact"}
          onRow={navToTicket} />
        {ticketId && <TicketDetails
          ticket={ticketData}
          loading={ticketLoading}
          error={ticketError}
          refreshTicket={fetchTicket} />}
      </Flex>
    </Flex>
  </>);
}


const useThingViewHooks = () => {
  const [selectedThingId, setSelectedThingId] = useState(null);
  const [selectedTicketId, setSelectedTicketId] = useState(null);
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
      navigate(`/things/${thingId}`);
    } else {
      navigate(`/`);
    }
  }

  const navToTicket = (record) => {
    return {
      onClick: () => {
        setSelectedTicketId(record.id)
        navigate(`/things/${thingId}/tickets/${record.id}`)
      }
    }
  }

  return {
    thingId,
    ticketId,
    selectedThingId,
    setSelectedThingId,
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
