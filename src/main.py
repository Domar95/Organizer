from .cli import Cli
from .records.general_category import GeneralCategory

def main():
    general_category = GeneralCategory('category_name', 'category_description')
    cli = Cli(general_category)
    cli.start()