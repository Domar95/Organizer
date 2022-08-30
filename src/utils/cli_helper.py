import os

from functools import wraps


class CLIHelper:
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def title():
        print("--------  Organizer  --------")

    def separator():
        print("-----------------------------")

    def line_space():
        print("")

    def wrong_input():
        print("Wrong input. Try again.")
        CLIHelper.line_space()

    def goodbye(self):
        print("Goodbye!")

    def welcome_screen():
        CLIHelper.separator()
        CLIHelper.title()
        CLIHelper.separator()
        CLIHelper.line_space()

    def go_back_option():
        print("0. Go back")

    def user_choice_input():
        return input("Enter a number: ")

    def new_screen(function):
        """
        Creates a wrapper function for a new screen
        """

        @wraps(function)
        def decorator(self, *args, **kwargs):
            # Clear interpreter screen
            CLIHelper.clear_screen()
            CLIHelper.welcome_screen()
            function(self, *args, **kwargs)

        return decorator
