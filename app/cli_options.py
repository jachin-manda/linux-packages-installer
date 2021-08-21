from rich import print
from rich.panel import Panel
from rich import box
from app import console


class PrintCommandLineOptions:
    def print_main_menu_panel(self):
        """
        Prints text for the command line main menu.
        """
        console.print(
            Panel(
                f"""
                [bold green]Main Menu[/]

                [#ECEFA4]Select option below[/]
                [bold ]
                1. View all saved [i]Packages and Commands
                2. Add a Package to the Database
                3. Update a Package values from the database
                4. Delete a Package from the database
                5. Run Package Installer
                6. Exit application
                [/]
                """,
                style="#50CB93",
                title="[bold cyan]Welcome[/]",
                box=box.HEAVY,
            )
        )

    def option_1(self):
        """
        Prints out text for option 1 in the command line interface.
        """
        pass

    def option_2(self):
        """
        Prints out text for option 2 in the command line interface.
        """
        pass

    def option_3(self):
        """
        Prints out text for option 3 in the command line interface.
        """
        pass

    def option_4(self):
        """
        Prints out text for option 4 in the command line interface.
        """
        pass

    def option_5(self):
        """
        Prints out text for option 5 in the command line interface.
        """
        pass

    def option_6(self):
        """
        Prints out text for option 6 in the command line interface.
        """
        pass
