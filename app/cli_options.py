from rich.panel import Panel
from rich.table import Table
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

    def option_1(self, table_data):
        """Print out a Table of all the Packages saved to the database.

        Args:
            table_data (list): A list containing the data for each package from the database
            for example: table_data =  [
                {
                    "id": 1,
                    "package_name": "VLC",
                    "package_desc": "A media player",
                    "slug": "vlc",
                    "command_debian": ["apt install vlc"],
                    "command_fedora": ["dnf install vlc"]
                }
            ]
        """
        table = Table()

        # Create table Headers. This could be dynamic by getting the database table column names, but will use static values for now.
        table.add_column("ID")
        table.add_column("Package Name")
        table.add_column("Package Description")
        table.add_column("Slug")
        table.add_column("Command Debian")
        table.add_column("Command Fedora")

        for row_data in table_data:
            table.add_row(
                str(
                    row_data["id"]
                ),  # convert to string to avoid NotRenderableError exception
                row_data["package_name"],
                row_data["package_desc"],
                row_data["slug"],
                row_data["command_debian"],
                row_data["command_fedora"],
            )
        console.print(table)

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
