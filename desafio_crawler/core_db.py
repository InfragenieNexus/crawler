import sqlite3
import pickle
from io import BytesIO
import logging


class QuoteDatabase:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.create_table()
        self.logger = logging.getLogger(__name__)

    def create_table(self) -> None:
        """Create the database table"""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY,
                pic BLOB,
                dataframe BLOB
            )
             """
        )
        self.conn.commit()

    def insert_quote(self, pic, dataframe) -> bool:
        """Insert a quote into the database"""
        cursor = self.conn.cursor()
        pic_binary = BytesIO(pic).getvalue()
        dataframe_binary = sqlite3.Binary(pickle.dumps(dataframe))

        try:
            cursor.execute(
                "INSERT INTO quotes (pic, dataframe) VALUES (?, ?)",
                (pic_binary, dataframe_binary),
            )
            self.conn.commit()
            self.logger.info("Citação inserida com sucesso no banco de dados.")
            self.close()
            return True
        except sqlite3.IntegrityError:
            self.logger.warning("Citação já existe no banco de dados.")
            self.close()
            return False

    def close(self):
        self.conn.close()
