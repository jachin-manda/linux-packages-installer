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

    def print_option_1(self, table_data):
        pass

    def print_option_2(self):
        """
        Prints out text for option 2 in the command line interface.
        """
        console.print(
            Panel(
                f"""
                Follow the prompts:
                [bold ] 
                package_name e.g [i]VLC media player
                package_desc e.g [i]A media player
                slug e.g [i]vlc
                command_debian e.g [i]apt install vlc
                command_fedora e.g [i]dnf install vlc
                [/]
                """,
                style="#50CB93",
                title="[bold cyan]Add package to database[/]",
                box=box.HEAVY,
            )
        )

    def print_option_3(self):
        """
        Prints out text for option 3 in the command line interface.
        """
        console.print(
            Panel(
                """[bold underline reverse]Update Package values[/] \n
                [bold]
                1. To update all values
                2. To update the Package name
                3. To update the Package description
                4. To update the slug value
                5. To update the Package install command for Debian
                6. To update the Package install command for Fedora
                7. Main menu[/]
                """,
                style="#50CB93",
                title="[bold cyan r]Update package in the database[/]",
            )
        )

    def print_option_4(self):
        """
        Prints out text for option 5 in the command line interface.
        """
        console.print(
            Panel(
                """[bold underline reverse]Delete Package[/] \n
                [bold]1. To delete the Package, enter ID or Package name or Slug
                2. Main menu[/]
                """,
                style="#50CB93",
                title="[bold cyan r]Delete package in the database[/]",
            )
        )

    def print_option_5(self):
        """
        Prints out text for option 4 in the command line interface.
        """
        console.print(
            Panel(
                """[bold underline reverse]Select the system you are using[/] \n
                [bold]
                1. Debian
                2. Fedora
                """,
                style="#50CB93",
                title="[bold cyan r]Linux Distribution[/]",
            )
        )

    def print_option_6(self):
        """
        Prints out text for option 6 in the command line interface.
        """
        console.print(
            Panel(
                """[bold underline reverse]Are you sure you want to quit?[/] \n
                Type [b]yes[/] or [b]no[/]
                """,
                style="#50CB93",
                title="[bold cyan r]Go to Main Menu?[/]",
            )
        )
