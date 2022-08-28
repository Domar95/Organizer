import os

from functools import wraps

# from .db.models import *


class Cli:
    def __init__(self, db_manager, general_category, record_factory):
        self.db_manager = db_manager
        self.general_category = general_category
        self.record_factory = record_factory
        self.table = None
        self.dummy_object = None

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def title(self):
        print("--------  Organizer  --------")

    def separator(self):
        print("-----------------------------")

    def line_space(self):
        print("")

    def wrong_input(self):
        print("Wrong input. Try again.")
        self.line_space()

    def goodbye(self):
        print("Goodbye!")

    def welcome_screen(self):
        self.separator()
        self.title()
        self.separator()
        self.line_space()

    def new_screen(function):
        # does not work (does not clear screen + welcome_screen on main screen (i.e. when wrong input))
        """
        Creates a wrapper function for a new screen
        """

        @wraps(function)
        def decorator(self, *args, **kwargs):
            # Clear interpreter screen
            self.clear_screen()
            self.welcome_screen()
            function(self, *args, **kwargs)

        return decorator

    def print_for_loop(self, request):
        for i in request:
            print(i)

    def get_table_name(self):
        return self.table.__name__

    def print_table_with_recent_records(self):
        table_name = self.get_table_name()
        print(f"Most recent records for {table_name}:")
        request = self.db_manager.query_select_table_ordered_desc(
            self.table, 5)
        self.print_for_loop(request)
        self.separator()

    def print_table_with_all_records(self):
        # might add sortings + eventually customnized sort by (f.e. for projects print by most important (importance factor) | or do this as additional option in the menu, like view most important records, so I can choose f.e. which project to do now
        # in this case I might specific submenus specific to each class (or a general one (like view all, search for, add, delete, update) + specific)
        table_name = self.get_table_name()
        print(f"All records for {table_name}:")
        request = self.db_manager.query_select_table_ordered_asc(
            self.table)
        self.print_for_loop(request)
        self.separator()

    def print_record_by_id(self, record_id):
        table_name = self.get_table_name()
        print(
            f"Following result was found in {table_name} with ID {record_id}:")
        request = self.db_manager.find_record_by_id(
            self.table, record_id)
        print(request)
        self.separator()

    def print_record_by_name(self, data):
        table_name = self.get_table_name()
        print(
            f"Following result was found in {table_name} with record_name containing {data}:")
        request = self.db_manager.find_record_by_name(self.table, data)
        self.print_for_loop(request)
        self.separator()

    # @new_screen

    def print_general_categories(self):
        starting_index = 1
        for category in self.general_category.general_categories:
            print(f"{str(starting_index)}. {category}")
            starting_index += 1

    def print_go_back_option(self):
        print("0. Go back")

    def record_screen(self):
        print("1. View all records")
        print("2. Search for record")
        print("3. Add new record")
        # update record by id?
        print("4. Update a record")
        print("5. Delete a record")
        self.print_go_back_option()
        self.line_space()

    def user_choice_input(self):
        return input("Enter a number: ")

    def input_form_create(self):
        for attribute in self.dummy_object.__dict__:
            if attribute.startswith("record"):
                if attribute != 'record_general_category_id':
                    user_input = input(f"Enter data for {attribute}: ")
                    if type(self.dummy_object.__dict__[attribute]) == int:
                        user_input = int(user_input)
                    self.dummy_object.__dict__[attribute] = user_input

    def input_form_update(self, record):
        new_record = {}
        for attribute in record.__dict__:
            if attribute.startswith("record"):
                if attribute != 'record_general_category_id':
                    print(
                        f"Current value ({attribute}: {record.__dict__[attribute]})")
                    user_input = input(
                        f"Input a new value for {attribute} or press 'enter' to pass: ")
                    if user_input != '':
                        if type(record.__dict__[attribute]) == int:
                            user_input = int(user_input)
                        new_record[attribute] = user_input
                    else:
                        new_record[attribute] = record.__dict__[attribute]
        return new_record

    def main_menu(self):
        while True:
            self.print_general_categories()
            print("0. Exit")
            self.line_space()

            user_choice = self.user_choice_input()
            self.line_space()

            if user_choice == "1":
                self.table = self.record_factory.get_record_class('daily_goal')
                self.dummy_object = self.record_factory.get_record_object(
                    'daily_goal')
            elif user_choice == "2":
                self.table = self.record_factory.get_record_class(
                    'programming_project')
                self.dummy_object = self.record_factory.get_record_object(
                    'programming_project')
            elif user_choice == "3":
                self.table = self.record_factory.get_record_class(
                    'idea')
                self.dummy_object = self.record_factory.get_record_object(
                    'idea')
            elif user_choice == "4":
                self.table = self.record_factory.get_record_class(
                    'info')
                self.dummy_object = self.record_factory.get_record_object(
                    'info')
            elif user_choice == "5":
                self.table = self.record_factory.get_record_class(
                    'reflection')
                self.dummy_object = self.record_factory.get_record_object(
                    'reflection')
            elif user_choice == "6":
                self.table = self.record_factory.get_record_class(
                    'other_record')
                self.dummy_object = self.record_factory.get_record_object(
                    'other_record')
            elif user_choice == "0":
                self.goodbye()
                exit()

            else:
                self.wrong_input()
                continue

            while True:
                self.print_table_with_recent_records()
                self.record_screen()
                user_choice = self.user_choice_input()
                if user_choice == '1':
                    self.print_table_with_all_records()
                    self.print_go_back_option()
                    self.line_space()
                    pass
                elif user_choice == '2':
                    while True:
                        print('1. Search by ID')
                        print('2. Search by name')
                        self.print_go_back_option()
                        user_choice = self.user_choice_input()
                        if user_choice == '1':
                            record_id = input(
                                f"Enter record_id: ")
                            record_id_int = int(record_id)
                            self.print_record_by_id(record_id_int)
                        elif user_choice == '2':
                            record_name = input(f"Enter record_name: ")
                            self.print_record_by_name(record_name)
                        elif user_choice == '0':
                            break
                        else:
                            self.wrong_input
                elif user_choice == '3':
                    self.input_form_create()
                    print(repr(self.dummy_object))
                    user_confirmation = input(
                        'Do you want to confirm? (y/n): ')
                    self.line_space()
                    if user_confirmation == 'y':
                        self.db_manager.add_record(self.dummy_object)
                        print('Data saved.')
                    print('Data was not saved.')
                    self.line_space()
                elif user_choice == '4':
                    record_id = input(
                        f"Enter record_id: ")
                    record_id_int = int(record_id)
                    record = self.db_manager.find_record_by_id(
                        self.table, record_id_int)
                    print(f"Updating a following record:")
                    print(repr(record))
                    updated_record_data = self.input_form_update(record)
                    print(f"Data will be updated as follows:")
                    print(repr(record))
                    user_confirmation = input(
                        'Do you want to confirm? (y/n): ')
                    self.line_space()
                    if user_confirmation == 'y':
                        self.db_manager.update_record(
                            self.table, record_id_int, updated_record_data)
                        print('Data saved.')
                    print('Data was not saved.')
                    self.line_space()
                elif user_choice == '5':
                    record_id = input(
                        f"Enter ID of item to delete in {self.get_table_name()}: ")
                    record_id_int = int(record_id)
                    print(f"Following data is going to be deleted:")
                    self.print_record_by_id(record_id_int)
                    user_confirmation = input(
                        'Do you want to confirm? (y/n): ')
                    self.line_space()
                    if user_confirmation == 'y':
                        self.db_manager.delete_record(
                            self.table, record_id_int)
                        print('Data deleted.')
                    self.line_space()
                elif user_choice == '0':
                    break
                else:
                    self.wrong_input()

    def start(self):
        self.main_menu()


if __name__ == "__main__":
    cli = Cli()
    cli.start()
