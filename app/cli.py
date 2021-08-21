import json
from rich.panel import Panel
from rich.table import Table
from app import console, session
from app.models import PackagesAndCommands
from app.cmd_processor import CommandInstaller


class Crud:
    def get_all_pkgs(self):
        data = session.query(PackagesAndCommands).all()
        return data

    def get_one_pkg(self, id=None, pkg_name=None):
        data = (
            session.query(PackagesAndCommands).filter_by(package_name=pkg_name).first()
        )
        if data:
            return True
        return False

    def add_packages(self, data):
        new_pkg = PackagesAndCommands(**data)
        session.add(new_pkg)
        session.commit()

    def update_pkg(self, id=None, pkg_name=None, data={}):
        pkg_to_update = (
            session.query(PackagesAndCommands).get(id)
            if id
            else session.query(PackagesAndCommands)
            .filter_by(package_name=pkg_name)
            .first()
        )

        if pkg_to_update:
            console.print(f"[bold blue]DATA: {data}[/]")
            for column, value in data.items():
                setattr(pkg_to_update, column, value)
            session.commit()
            console.print("[bold]Successfully updated[/]", style="black on green")
        return False

    def delete_pkg(self, id=None, pkg_name=None):
        session.query(PackagesAndCommands).filter_by(package_name=pkg_name).delete()
        session.commit()
        console.print("[bold]Successfully deleted[/]", style="black on red")


class CliInputDataCollect:
    def get_option_2_data(self):
        while True:
            pkg_name = console.input(
                "[bold cyan]Enter the Application/Package name [i]option[/i][/]? "
            )
            pkg_desc = console.input(
                "[bold cyan]Enter the Application/Package description [i]option[/i][/]? "
            )
            cmd_deb = console.input(
                "[bold cyan]Enter the command for Debian. [i]option[/i][/] [yellow]If it's more than one command, seperate them with '&&'. For example 'apt update && apt upgrade'[/] \n"
            )
            cmd_rpm = console.input(
                "[bold cyan]Enter the command for Fedora [i]option[/i][/]. [yellow]If it's more than one command, seperate them with '&&'. For example 'apt update && apt upgrade'[/] \n"
            )

            return {
                "package_name": pkg_name,
                "package_desc": pkg_desc,
                "command_debian": json.dumps(cmd_deb.split("&&")),
                "command_fedora": json.dumps(cmd_rpm.split("&&")),
            }

    def get_option_4_data(self):
        while True:
            user_input = console.input(
                "[bold]Enter the name of the package you want to update.....[/] \n"
            )
            if self.get_one_pkg(pkg_name=user_input):
                pkg_to_update = user_input
            else:
                console.print(
                    "Not found. Maybe you entered a wrong name.",
                    style="red on black",
                )
                continue
            option = console.input(
                """[bold cyan]
                [bold]What do you want to update?:[/]
                1. Update all values
                2. Update the package name
                3. Update the package description
                4. Update the command for debian
                5. Update the command for fedora
                [/]
                """
            )

            if option == "1":
                new_name = console.input(
                    "[bold cyan]Enter the Application/Package name [i]option[/i][/]? \n"
                )
                new_desc = console.input(
                    "[bold cyan]Enter the Application/Package description [i]option[/i][/]? \n"
                )
                new_cmd_deb = console.input(
                    "[bold cyan]Enter the install command on Debian. [i]option[/i][/] [bold cyan]If it's more than one command, seperate the with '&&'. For example 'apt update && apt upgrade'[/] \n "
                )
                new_cmd_rpm = console.input(
                    "[bold cyan]Enter the install command on Fedora [i]option[/i][/]. [bold cyan]If it's more than one command, seperate the with '&&'. For example 'apt update && apt upgrade'[/] \n "
                )
                return pkg_to_update, {
                    "package_name": new_name,
                    "package_desc": new_desc,
                    "command_debian": json.dumps(new_cmd_deb.splt("&&")),
                    "command_fedora": json.dumps(new_cmd_rpm.splt("&&")),
                }
            elif option == "2":
                new_name = console.input(
                    "[bold yellow]Enter the new Application/Package name [i]option[/i][/]? \n"
                )
                return pkg_to_update, {"package_name": new_name}

            elif option == "3":
                new_desc = console.input(
                    "[bold yellow]Enter the new Application/Package description [i]option[/i][/]? \n"
                )
                return pkg_to_update, {"package_desc": new_desc}

            elif option == "4":
                new_cmd_deb = console.input(
                    "[bold yellow]Enter the newApplication/Package command Debian [i]option[/i][/]? \n"
                )
                return pkg_to_update, {
                    "command_debian": json.dumps(new_cmd_deb.split("&&"))
                }

            elif option == "5":
                new_cmd_rpm = console.input(
                    "[bold yellow]Enter the new Application/Package command Fedora [i]option[/i][/]? \n"
                )
                return pkg_to_update, {
                    "command_fedora": json.dumps(new_cmd_rpm.split("&&"))
                }
            else:
                console.print(
                    "[bold]Invalid option. Try again[/]", style="red on black"
                )
                continue


class CliActions(CliInputDataCollect, Crud):
    def __init__(self):
        super().__init__()

    def option_1(self):
        linux_sys = ""
        while True:
            user_input = console.input(
                "[bold cyan]Which system are you using?[/][yellow]type debian or fedora[/] \n >>>\t"
            )
            if user_input in ("debian", "fedora"):
                linux_sys = user_input
                break
            else:
                console.print("[bold] Invalid option[/]", style="black on red")
                continue

        data = self.get_all_pkgs()
        cmd_installer = CommandInstaller(data, linux_system=linux_sys)
        cmd_installer.install_packages()

    def option_2(self):
        data = self.get_option_2_data()
        self.add_packages(data)
        console.print("[bold]Package was saved.[/]", style="green on black")

    def option_3(self):
        table = Table(title="All Packages")

        data = self.get_all_pkgs()

        table.add_column("ID")
        table.add_column("Package Name")
        table.add_column("Package Description")
        table.add_column("Command Debian")
        table.add_column("Command Fedora")

        for row in data:
            table.add_row(
                str(row.id),
                row.package_name,
                row.package_desc,
                row.command_debian,
                row.command_fedora,
            )
        console.print(table)

    def option_4(self):
        pkg_to_update, data = self.get_option_4_data()
        self.update_pkg(pkg_name=pkg_to_update, data=data)

    def option_5(self):
        running = True
        while running:
            user_input = input(
                "What package do you want to delete? enter thepackage_name....."
            )
            if self.get_one_pkg(pkg_name=user_input):
                pkg_to_delete = user_input
                self.delete_pkg(pkg_name=pkg_to_delete)
                running = False
            else:
                console.print(
                    "[bold]Not found. Maybe you entered a wrong name[/]",
                    style="black on red",
                )
                continue


class CliInterface:
    def __init__(self, logo):
        self.logo = logo

    def print_logo(self):
        with open(self.logo, "r") as f:
            console.print(f.read())

    def print_main_menu(self):
        console.print(
            Panel(
                """
            [bold green]SELECT ACTION TO PERFORM[/bold green]

            1. Install Application and Packages
            2. [cyan]Add Application/Package install command to db[/cyan]
            3. [cyan]View all Application/Package[/cyan]
            4. [cyan]Update Application/Package[/cyan]
            5. [cyan]Delete Application/Package[/cyan]
            6. [yellow]Exit program[/yellow]
            """,
                title="[bold]WELCOME[/bold]",
            )
        )


#     def print_option_2_menu(self):
#         console.print(
#             Panel(
#                 """
#             [bold green]PROVIDE DATA OF THE APPLICATION/PACKAGE[/bold green]
#             """,
#                 title="[bold]Application/Package atrributes[/bold]",
#             )
#         )

#     def print_option_3_menu(self):
#         console.print(
#             Panel(
#                 """
#             [bold green]TABLE OF SAVE APPLICATION PACKAGES[/bold green]
#             """,
#                 title="[bold]Applications/Packages [/bold]",
#             )
#         )

#     def print_option_4_menu(self):
#         console.print(
#             Panel(
#                 """
#             [bold green]ENTER ID OR NAME OF THE APPLICATION/PACKAGE TO UPDATE[/bold green]
#             """,
#                 title="[bold]Delete Application/Package[/bold]",
#             )
#         )

#     def print_option_5_menu(self):
#         console.print(
#             Panel(
#                 """
#             [bold green]ENTER ID OR NAME OF THE APPLICATION/PACKAGE TO DELETE[/bold green]
#             """,
#                 title="[bold]Delete Application/Package[/bold]",
#             )
#         )

#     def print_option_6_menu(self):
#         pass
