import os

from functools import wraps


class Cli:
    def __init__(self, general_category):
        self.general_category = general_category
        self.check = 1

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

    @new_screen
    def print_general_categories(self):
        starting_index = 1
        for category in self.general_category.general_categories:
            print(f"{str(starting_index)}. {category}")
            starting_index += 1

    def main_menu(self):
        while True:
            self.print_general_categories()
            print("1. View categories")
            print("2. ")
            print("0. Exit")

            self.line_space()

            user_choice = input("Enter a number: ")
            self.line_space()

            if user_choice == "1":
                # to-do next: create tables (separate for each category) -> done, add models, after 1. 2. 3 etc chosen here, load a db. add a func to view records from that table, then add options
                # -> shows last 5 added recors (last 5 from table), options: 1. Search for record (by name) 2. View all 3. Add a record 4. Delete
                # eventually customnized (f.e. for projects print by most important (importance factor)
                pass
            elif user_choice == "2":
                pass
            elif user_choice == "3":
                pass
            elif user_choice == "4":
                pass
            elif user_choice == "5":
                pass
            elif user_choice == "6":
                pass
            elif user_choice == "0":
                self.goodbye()
                exit()

            else:
                self.wrong_input()

    def start(self):
        self.main_menu()


if __name__ == "__main__":
    cli = Cli()
    cli.start()
