import os


class Cli:
    def __init__(self):
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

    def new_screen(func):
        """
        Creates a wrapper function for a new screen
        """

        def wrapper(self, *args, **kwargs):
            while True:
                # Clear interpreter screen
                self.clear_screen()
                self.welcome_screen()
                func(self, *args, **kwargs)

        return wrapper

    @new_screen
    def main_menu(self):
        while True:
            print("0. Exit")
            self.line_space()

            user_choice = input("Enter a number: ")
            self.line_space()

            if user_choice == "1":
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
