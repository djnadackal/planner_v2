from datetime import datetime
from src.db.core import get_db_connection, DbCore


def backup_db(backup_filepath: str | None = None) -> str:
    # copy "data/database.db" to "data/database-bak-<current_timestamp>.db"
    src_path = DbCore.__db_filepath__
    if backup_filepath is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        dest_path = f"data/database-bak-{timestamp}.db"
    else:
        dest_path = backup_filepath
    with open(src_path, "rb") as src_file:
        with open(dest_path, "wb") as dest_file:
            dest_file.write(src_file.read())
    return dest_path


def diff_check(backup_path):
    from pprint import pprint

    with get_db_connection(backup_path) as backup_conn:
        backup_cursor = backup_conn.execute(
            "SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name"
        )
        backup_tables = backup_cursor.fetchall()
        # transform into a dict
        backup_tables = {
            table["name"]: table["sql"] for table in backup_tables
        }
    with get_db_connection(DbCore.__db_filepath__) as current_conn:
        current_cursor = current_conn.execute(
            "SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name"
        )
        current_tables = current_cursor.fetchall()
        # transform into a dict
        current_tables = {
            table["name"]: table["sql"] for table in current_tables
        }
    for table_name, ddl in [
        list(table) for table in backup_tables.items()
    ]:
        current_ddl = current_tables.get(table_name)
        if current_ddl is None:
            print(f"Table {table_name} not found in current database.")
            continue
        if current_ddl != ddl:
            print(f"Difference found in table {table_name}:")
            print("Backup DDL:")
            print(ddl)
            print("Current DDL:")
            print(current_ddl)
        # remove the table from current_tables to mark it as processed
        current_tables.pop(table_name)
    # call out any remaining tables in current_tables that are not in backup
    for table_name, ddl in [
        list(table) for table in current_tables.items()
    ]:
        print(
            f"Table {table_name} found in current database but not in backup."
        )
