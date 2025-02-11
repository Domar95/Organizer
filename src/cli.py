import time

from .utils.cli_helper import CLIHelper


class Cli:
    def __init__(self, db_manager, general_category, record_factory):
        self.db_manager = db_manager
        self.general_category = general_category
        self.record_factory = record_factory
        self.table = None
        self.dummy_object = None

    def print_for_loop(self, request: list):
        if request:
            for i in request:
                print(i)
        else:
            print("No data was retrieved.")

    def get_table_name(self):
        return self.table.__name__

    @CLIHelper.new_screen
    def print_table_with_recent_records(self):
        table_name = self.get_table_name()
        print(f"Most recent records for {table_name}:")
        request = self.db_manager.query_select_table_ordered_desc(self.table, 5)
        self.print_for_loop(request)
        CLIHelper.separator()

    def print_table_with_all_records(self):
        # might add sortings + eventually customnized sort by (f.e. for projects print by most important (importance factor) | or do this as additional option in the menu, like view most important records, so I can choose f.e. which project to do now
        # in this case I might specific submenus specific to each class (or a general one (like view all, search for, add, delete, update) + specific)
        table_name = self.get_table_name()
        print(f"All records for {table_name}:")
        request = self.db_manager.query_select_table_ordered_asc(self.table)
        self.print_for_loop(request)
        CLIHelper.separator()

    def print_record_by_id(self, record_id):
        table_name = self.get_table_name()
        print(f"Following data was found in {table_name} with ID {record_id}:")
        request = self.db_manager.find_record_by_id(self.table, record_id)
        if request:
            print(request)
        else:
            print("No data was retrieved.")
        CLIHelper.separator()

    def print_record_by_name(self, data):
        table_name = self.get_table_name()
        print(
            f"Following data was found in {table_name} with record_name containing {data}:"
        )
        request = self.db_manager.find_record_by_name(self.table, data)
        self.print_for_loop(request)
        CLIHelper.separator()

    def print_general_categories(self):
        starting_index = 1
        for category in self.general_category.general_categories:
            print(f"{str(starting_index)}. {category}")
            starting_index += 1

    def record_screen(self):
        print("1. View all records")
        print("2. Search for record")
        print("3. Add new record")
        print("4. Update a record")
        print("5. Delete a record")
        CLIHelper.go_back_option()
        CLIHelper.line_space()

    def input_form_create(self):
        for attribute in self.dummy_object.__dict__:
            if attribute.startswith("record"):
                if attribute != "record_general_category_id":
                    user_input = input(f"Enter {attribute}: ")
                    if type(self.dummy_object.__dict__[attribute]) == int:
                        user_input = int(user_input)
                    self.dummy_object.__dict__[attribute] = user_input

    def input_form_update(self, record):
        new_record = {}
        for attribute in record.__dict__:
            if attribute.startswith("record"):
                if attribute != "record_general_category_id":
                    print(f"Current {attribute} is {record.__dict__[attribute]}")
                    user_input = input(
                        f"Input new {attribute} or press 'enter' to pass: "
                    )
                    if user_input != "":
                        if type(record.__dict__[attribute]) == int:
                            user_input = int(user_input)
                        new_record[attribute] = user_input
                    else:
                        new_record[attribute] = record.__dict__[attribute]
                    CLIHelper.line_space()
        return new_record

    def load_record(self, record_category):
        self.table = self.record_factory.get_record_class(record_category)
        self.dummy_object = self.record_factory.get_record_object(record_category)

    @CLIHelper.new_screen
    def general_categories_menu(self):
        while True:
            self.print_general_categories()
            print("0. Exit")
            CLIHelper.line_space()

            user_choice = CLIHelper.user_choice_input()
            CLIHelper.line_space()

            if user_choice == "1":
                self.load_record("daily_goal")
                break
            elif user_choice == "2":
                self.load_record("programming_project")
                break
            elif user_choice == "3":
                self.load_record("idea")
                break
            elif user_choice == "4":
                self.load_record("info")
                break
            elif user_choice == "5":
                self.load_record("reflection")
                break
            elif user_choice == "6":
                self.load_record("other_record")
                break
            elif user_choice == "0":
                CLIHelper.goodbye()
                exit()
            else:
                CLIHelper.wrong_input()
                continue

    @CLIHelper.new_screen
    def main_functions_menu(self):
        while True:
            self.print_table_with_recent_records()
            self.record_screen()
            user_choice = CLIHelper.user_choice_input()
            if user_choice == "1":
                self.view_all_records_menu()
            elif user_choice == "2":
                self.search_for_record_menu()
            elif user_choice == "3":
                self.add_new_record_menu()
            elif user_choice == "4":
                self.update_record_menu()
            elif user_choice == "5":
                self.delete_record_menu()
            elif user_choice == "0":
                break
            else:
                CLIHelper.wrong_input()

    @CLIHelper.new_screen
    def view_all_records_menu(self):
        self.print_table_with_all_records()
        CLIHelper.go_back_option()
        CLIHelper.line_space()
        while True:
            user_choice = CLIHelper.user_choice_input()
            if user_choice == "0":
                break
            else:
                CLIHelper.wrong_input()

    @CLIHelper.new_screen
    def search_for_record_menu(self):
        while True:
            self.print_search_options()
            user_choice = CLIHelper.user_choice_input()
            if user_choice == "1":
                self.search_by_id_menu()
            elif user_choice == "2":
                self.search_by_name_menu()
            elif user_choice == "0":
                break
            else:
                CLIHelper.wrong_input()

    @CLIHelper.new_screen
    def print_search_options(self):
        print("1. Search by ID")
        print("2. Search by name")
        CLIHelper.go_back_option()
        CLIHelper.line_space()

    @CLIHelper.new_screen
    def search_by_id_menu(self):
        record_id = input(f"Enter record_id: ")
        record_id_int = int(record_id)
        self.print_record_by_id(record_id_int)
        CLIHelper.go_back_option()
        CLIHelper.line_space()
        while True:
            user_choice = CLIHelper.user_choice_input()
            if user_choice == "0":
                break
            else:
                CLIHelper.wrong_input()

    @CLIHelper.new_screen
    def search_by_name_menu(self):
        record_name = input(f"Enter record_name: ")
        self.print_record_by_name(record_name)
        CLIHelper.go_back_option()
        CLIHelper.line_space()
        while True:
            user_choice = CLIHelper.user_choice_input()
            if user_choice == "0":
                break
            else:
                CLIHelper.wrong_input()

    @CLIHelper.new_screen
    def add_new_record_menu(self):
        self.input_form_create()
        print(repr(self.dummy_object))
        user_confirmation = input("Do you want to confirm? (y/n): ")
        CLIHelper.line_space()
        if user_confirmation == "y":
            self.db_manager.add_record(self.dummy_object)
            print("Data saved.")
            time.sleep(2)
        else:
            print("Data was not saved.")
            time.sleep(2)
        CLIHelper.line_space()

    @CLIHelper.new_screen
    def update_record_menu(self):
        record_id = input(f"Enter record_id: ")
        record_id_int = int(record_id)
        CLIHelper.line_space()
        record = self.db_manager.find_record_by_id(self.table, record_id_int)
        print(f"Updating a following record:")
        print(repr(record))
        CLIHelper.line_space()
        updated_record_data = self.input_form_update(record)
        print(f"Data will be updated as follows:")
        print(repr(record))
        user_confirmation = input("Do you want to confirm? (y/n): ")
        CLIHelper.line_space()
        if user_confirmation == "y":
            self.db_manager.update_record(
                self.table, record_id_int, updated_record_data
            )
            print("Data saved.")
            time.sleep(2)
        else:
            print("Data was not saved.")
            time.sleep(2)
        CLIHelper.line_space()

    @CLIHelper.new_screen
    def delete_record_menu(self):
        record_id = input(f"Enter ID of item to delete in {self.get_table_name()}: ")
        record_id_int = int(record_id)
        record = self.db_manager.find_record_by_id(self.table, record_id_int)
        print(f"Following data will be deleted:")
        print(repr(record))
        user_confirmation = input("Do you want to confirm? (y/n): ")
        CLIHelper.line_space()
        if user_confirmation == "y":
            self.db_manager.delete_record(self.table, record_id_int)
            print("Data deleted.")
            time.sleep(2)
        CLIHelper.line_space()

    @CLIHelper.new_screen
    def main_menu(self):
        while True:
            self.general_categories_menu()
            self.main_functions_menu()

    def start(self):
        self.main_menu()


if __name__ == "__main__":
    cli = Cli()
    cli.start()
