import os

# set environment variable before importing to suppress the
# init schema setup
os.environ["DB_MIGRATION"] = "true"
from src.db.migrations import add_users_and_milestones_tables


if __name__ == "__main__":
    add_users_and_milestones_tables()
