from ..core.get_connection import get_db_connection


def add_users_and_milestones_tables():
    # initialize the core
    with get_db_connection() as conn:
        # add the milestones table
        milestones_table_sql = """
        CREATE TABLE IF NOT EXISTS milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            due_date DATETIME
        );
        """
        conn.execute(milestones_table_sql)
        print("Milestones table added.")
        # add the users table
        users_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE
        );
        """
        conn.execute(users_table_sql)
        print("Users table added.")
        # add the ticket_milestones table
        ticket_milestones_table_sql = """
        CREATE TABLE IF NOT EXISTS ticket_milestones (
            ticket_id INTEGER,
            milestone_id INTEGER,
            PRIMARY KEY(ticket_id, milestone_id),
            FOREIGN KEY(ticket_id) REFERENCES tickets(id),
            FOREIGN KEY(milestone_id) REFERENCES milestones(id)
        );
        """
        conn.execute(ticket_milestones_table_sql)
        print("Ticket milestones table added.")
        # add the user_id foreign key to the tickets table
        add_user_id_to_tickets_sql = """
        ALTER TABLE tickets
            ADD COLUMN user_id INTEGER
            REFERENCES users(id);
        """
        conn.execute(add_user_id_to_tickets_sql)
        print("User ID column added to tickets table.")
