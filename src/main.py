from .cli import Cli
from .records.general_category import GeneralCategory

from .db.db_manager import DBManager

from .records.record_factory import RecordFactory


def main():
    general_category = GeneralCategory('category_name', 'category_description')
    db_manager = DBManager()
    db_manager.start_engine()
    record_factory = RecordFactory()
    cli = Cli(db_manager, general_category, record_factory)
    cli.start()
