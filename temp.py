import src

Ticket = src.Controller.Tables.Ticket

t = Ticket.get_by_id(8)

print(t)
