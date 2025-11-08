import { Card, Flex, List } from "antd";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import components from "../../components";
import { useEffect, useState } from "react";
import useApi from "../../api";

const {
  CommentPanel,
  ActionPanel,
  tables: { TicketTable },
  details: { TicketDetails },
  inputs: { MilestoneDropdown }
} = components;

const TicketView = () => {
  const {
    ticketId,
    thingData,
    ticketData,
    ticketLoading,
    ticketError,
    milestonesData,
    milestonesLoading,
    fetchTicket,
    onRow,
    beginAddTicket,
    setBeginAddTicket,
    addMilestone,
  } = useTicketViewHooks()
  return (<>
    <Flex gap="10px" style={{ overflowY: 'hidden' }}>
      <Flex gap="10px" style={{ height: '100%', minHeight: 0, overflowX: 'auto' }}>
        <Flex vertical>
          <Flex style={{
            height: ticketId || beginAddTicket ? '50%' : '100%',
          }}>
            <TicketTable
              tableMode={ticketId ? "compact" : "full"}
              selectedTicketId={ticketId}
              beginAddTicket={() => setBeginAddTicket(true)}
              scrollHeight={ticketId || beginAddTicket ? 110 : 400}
              onRow={onRow} />
          </Flex>
          {(ticketId || beginAddTicket) && <TicketDetails
            addMode={beginAddTicket}
            setAddMode={setBeginAddTicket}
            ticket={beginAddTicket ? {} : ticketData}
            thing={thingData}
            loading={ticketLoading}
            error={ticketError}
            refreshTicket={fetchTicket} />}
        </Flex>
        {ticketId && <>
          <Flex
            vertical
            gap="10px"
            style={{ flex: 1, height: "100%" }}>
            <Flex style={{
              maxHeight: '50%',
              minHeight: '50%'
            }}>
              <CommentPanel ticketId={ticketId} />
            </Flex>
            <Flex style={{
              maxHeight: '50%',
              minHeight: '50%'
            }}>
              <ActionPanel ticketId={ticketId} />
            </Flex>
          </Flex>
          <Card
            title="Milestones"
            style={{ width: '300px', height: '100%' }}
            extra={<MilestoneDropdown
              setSelectedMilestoneId={(milestoneId) => addMilestone(ticketId, milestoneId)} />}
          >
            <List
              loading={milestonesLoading}
              dataSource={milestonesData || []}
              renderItem={(milestone) => (
                <List.Item
                  style={{
                    padding: '10px',
                  }}
                >
                  {milestone.name}
                </List.Item>
              )}
            />
          </Card>
        </>}
      </Flex>
    </Flex>
  </>)
}


const useTicketViewHooks = () => {
  // initialize state
  const { thingId, ticketId } = useParams();
  const [beginAddTicket, setBeginAddTicket] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  // custom hooks
  const {
    data: ticketData,
    loading: ticketLoading,
    error: ticketError,
    getTicket
  } = useApi.ticket.fetchOne(ticketId);
  const {
    data: milestonesData,
    loading: milestonesLoading,
    error: milestonesError,
    fetchData: fetchMilestones
  } = useApi.milestone.fetchMany({ ticket_id: ticketId });
  const {
    data: createMilestoneData,
    loading: createMilestoneLoading,
    error: createMilestoneError,
    addMilestone
  } = useApi.ticket.addMilestone();

  // helpers for fetching data
  const refreshTicket = () => {
    if (ticketId) {
      getTicket(ticketId);
    }
  }
  const refreshMilestones = () => {
    if (ticketId) {
      fetchMilestones({ ticket_id: ticketId });
    }
  }

  useEffect(() => {
    if (ticketId) {
      refreshTicket()
      refreshMilestones()
    }
  }, [ticketId])

  useEffect(() => {
    if (createMilestoneData) {
      refreshMilestones();
    }
  }, [createMilestoneLoading])

  const selectTicket = (newTicketId) => {
    if (!newTicketId || newTicketId === ticketId) {
      navigate(`/`);
      return;
    }
    navigate(`/tickets/${newTicketId}`);
  }

  const onRow = (record) => {
    return {
      onClick: () => {
        if (record.id != ticketId) {
          if (thingId) {
            navigate(`/${thingId}/tickets/${record.id}`)
          } else {
            navigate(`/tickets/${record.id}`)
          }
        } else {
          // Clicking the same ticket deselects it
          if (thingId) {
            navigate(`/${thingId}`);
          } else {
            navigate(`/`);
          }
        }
      }
    }
  }

  return {
    ticketId,
    selectTicket,
    onRow,
    ticketData,
    ticketLoading,
    ticketError,
    milestonesData,
    milestonesLoading,
    milestonesError,
    location,
    fetchTicket: refreshTicket,
    onRow: onRow,
    beginAddTicket,
    setBeginAddTicket,
    addMilestone,
  }

}

export default TicketView;
