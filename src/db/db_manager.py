import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


class DBManager:
    def __init__(self):
        self.db = None
        self.connected = False
        self.mycursor = None
        self.engine = None

    def start_engine(self):
        """Initialize the engine"""
        load_dotenv()
        USERNAME = os.getenv("db_username")
        PASSWORD = os.getenv("db_password")

        self.engine = create_engine(
            f"mysql://{USERNAME}:{PASSWORD}@127.0.0.1:3306/organizer", echo=True
        )


if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.start_engine()
    print(db_manager.engine)
