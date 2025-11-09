import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import useMutateUser from "../../components/details/userModal/mutateUserHooks";
import useApi from "../../api";

const useUserViewHooks = () => {
  const { userId } = useParams();
  const navigate = useNavigate();

  const [addUserModalOpen, setAddUserModalOpen] = useState(false);
  const [editUserModalOpen, setEditUserModalOpen] = useState(false);
  const mutateUser = useMutateUser();

  const selectUser = (id) => {
    if (id == userId) {
      navigate(`/users/`);
    } else {
      navigate(`/users/${id}`);
    }
  }
  const selectTicket = (id) => {
    navigate(`/tickets/${id}`);
  }

  const api = {
    user: {
      list: useApi.user.fetchMany(),
      selected: useApi.user.fetchOne(userId),
      create: useApi.user.create(),
      update: useApi.user.update(),
    },
    ticket: {
      list: useApi.ticket.fetchMany({ user_id: userId }),
    },
  };
  api.refreshAll = () => {
    api.user.list.fetchData();
    if (userId) {
      api.user.selected.fetchOne(userId);
      api.ticket.list.fetchData({ user_id: userId });
    }
  };

  // Modal State
  const modalControl = {
    add: {
      isOpen: addUserModalOpen,
      open: () => {
        mutateUser.reset();
        setAddUserModalOpen(true);
      },
      close: () => setAddUserModalOpen(false),
      submit: async () => {
        await api.user.create.create(
          {
            username: mutateUser.username,
          }
        );
        api.refreshAll();
        mutateUser.reset();
        setAddUserModalOpen(false);
      },
    },
    edit: {
      isOpen: editUserModalOpen,
      open: () => {
        mutateUser.set.username(api.user.selected.data.username);
        setEditUserModalOpen(true);
      },
      close: () => setEditUserModalOpen(false),
      submit: async () => {
        await api.user.update.update({
          id: userId,
          username: mutateUser.username,
        });
        api.refreshAll();
        mutateUser.reset();
        setEditUserModalOpen(false);
      },
    },
  }

  useEffect(() => {
    api.refreshAll();
  }, [userId]);

  return {
    userId,
    api,
    select: {
      user: selectUser,
      ticket: selectTicket,
    },
    modalControl,
    mutateUser,
  };
}


export default useUserViewHooks;
