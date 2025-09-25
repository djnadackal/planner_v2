from contextlib import contextmanager
import sqlite3


@contextmanager
def get_db_connection(db_path: str = "data/database.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
