import src

Ticket = src.Controller.Tables.Ticket
TicketParams = src.Controller.Params.Ticket
QueryBuilder = src.Controller.QueryBuilder

params = TicketParams(
    thing_ids=[1, 2, 3],
    category_id=5,
    open=True,
)

builder = QueryBuilder(Ticket, params)
builder.build_full()
print(builder.query)
print(builder.args)
