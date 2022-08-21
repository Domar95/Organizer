from .cli import Cli
from .records.general_category import GeneralCategory

from .db.db_manager import DBManager


def main():
    general_category = GeneralCategory('category_name', 'category_description')
    db_manager = DBManager()
    db_manager.start_engine()
    cli = Cli(db_manager, general_category)
    cli.start()
