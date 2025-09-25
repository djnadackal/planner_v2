from . import controller
from datetime import datetime


def seed_database():
    """
    Seed the database with sample data for testing and development.
    Pseudocode:
    1. Create categories, capturing their IDs
    2. Create things linked to categories
    3. Create tickets linked to things and categories
    4. Create comments and actions linked to tickets
    5. Handle errors and print progress
    """
    try:
        # Seed Categories
        categories = [
            controller.Category(name="Assets", parent_id=None),
            controller.Category(name="Property", parent_id=None),
            controller.Category(
                name="First House", parent_id=2
            ),  # Child of Property
            controller.Category(
                name="Backyard", parent_id=3
            ),  # Child of First House
            controller.Category(
                name="Master Bathroom", parent_id=3
            ),  # Child of First House
            controller.Category(name="Electronics", parent_id=None),
            controller.Category(
                name="Vehicles", parent_id=1
            ),  # Child of Hardware
            controller.Category(name="Financial", parent_id=None),
        ]
        category_ids = []
        for cat in categories:
            cat_id = controller.CategoryManager.create(cat)
            category_ids.append(cat_id)
            print(f"Created category: {cat.name} (ID: {cat_id})")

        def getCategoryId(name):
            for i, cat in enumerate(categories):
                if cat.name == name:
                    return category_ids[i]
            return None

        # Seed Things
        things = [
            controller.Thing(
                name="Pool",
                category_id=getCategoryId("Backyard"),
                description="Outdoor swimming pool",
                docs_link="http://docs.pool.com",
            ),
            controller.Thing(
                name="Garden",
                category_id=getCategoryId("Backyard"),
                description="Vegetable garden",
                docs_link="http://docs.garden.com",
            ),
            controller.Thing(
                name="Laptop",
                category_id=getCategoryId("Electronics"),
                description="Personal mac laptop",
                docs_link="http://docs.laptop.com",
            ),
            controller.Thing(
                name="Truck",
                category_id=getCategoryId("Vehicles"),
                description="Pickup truck",
                docs_link="http://docs.truck.com",
            ),
            controller.Thing(
                name="Couch",
                category_id=None,
                description="Living room couch",
                docs_link="http://docs.couch.com",
            ),
        ]
        thing_ids = []
        for thing in things:
            thing_id = controller.ThingManager.create(thing)
            thing_ids.append(thing_id)
            print(f"Created thing: {thing.name} (ID: {thing_id})")

        # Seed Tickets
        tickets = [
            controller.Ticket(
                thing_id=thing_ids[0],
                category_id=category_ids[0],
                description="Laptop overheating issue",
                open=True,
                completed_at=None,
            ),
            controller.Ticket(
                thing_id=thing_ids[1],
                category_id=category_ids[1],
                description="Database query optimization needed",
                open=False,
                completed_at=datetime(2025, 9, 18, 10, 0),
            ),
            controller.Ticket(
                thing_id=None,
                category_id=category_ids[2],
                description="Network latency reported",
                open=True,
                completed_at=None,
            ),
        ]
        ticket_ids = []
        for ticket in tickets:
            ticket_id = controller.TicketManager.create(ticket)
            ticket_ids.append(ticket_id)
            print(
                f"Created ticket: {ticket.description[:20]}... (ID: {ticket_id})"
            )

        # Seed Comments
        comments = [
            controller.Comment(
                ticket_id=ticket_ids[0],
                content="Checked thermal paste, needs replacement",
            ),
            controller.Comment(
                ticket_id=ticket_ids[0],
                content="Scheduled maintenance for laptop",
            ),
            controller.Comment(
                ticket_id=ticket_ids[1],
                content="Optimized indexes, testing in progress",
            ),
        ]
        for comment in comments:
            comment_id = controller.CommentManager.create(comment)
            print(
                f"Created comment: {comment.content[:20]}... (ID: {comment_id})"
            )

        # Seed Actions
        actions = [
            controller.Action(
                ticket_id=ticket_ids[0], action_type="Diagnosed"
            ),
            controller.Action(
                ticket_id=ticket_ids[0], action_type="Repaired"
            ),
            controller.Action(
                ticket_id=ticket_ids[1], action_type="Updated"
            ),
        ]
        for action in actions:
            action_id = controller.ActionManager.create(action)
            print(
                f"Created action: {action.action_type} (ID: {action_id})"
            )

        print("Database seeding completed successfully!")
    except Exception as e:
        print(f"Error during seeding: {str(e)}")
        raise
