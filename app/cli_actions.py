from rich.table import Table
from app import console, session
from app.models import PackagesAndCommands


class ConsoleInputData:
    """
    Performs actions according to the option selected.
    """

    def get_option_1_table_data(self):
        """
        Queries the data of all the packages saved in the database, then create a dictionary with data that will be used in rendering a table.
        returns: list
        for example data = [
            {"id": ..., "package_name": ..., "package_desc": ..., "slug": ..., "command_debian": ..., "command_fedora": ...}
        ]
        """
        # query all data
        data_objects = session.query(PackagesAndCommands).all()

        try:
            # get names of the database Table column/field names to be used as key in the row_data dict
            field_names = (
                data_objects[0].metadata.tables["packages_and_commands"].columns.keys()
            )

            data = []
            row_data = {}

            for obj in data_objects:
                for field_name in field_names:
                    row_data[field_name] = getattr(obj, field_name)
                data.append(row_data)
            console.print(data)

            return data

        # excecption that might occur when you getting field_names but the data_objects list is empty(nothing in the database)
        except IndexError:
            return {}

    def package_is_in_db(self, pkg):
        """
        Check if the package exists in the database.
        @param pkg: attribute used to query the package in the database
        @type pkg: string
        @return: package data if exists in database else False
        @rtype: bool
        """
        query = session.query(PackagesAndCommands)
        try:
            package_data = query.get(int(pkg))

        # Catch error raised when converting pkg param to int to use as an id in the query fails, meaning pkg param is a
        # package name or slug.
        except ValueError:
            package_data = (
                query.filter_by(package_name=pkg).first()
                or query.filter_by(slug=pkg).first()
            )
        if package_data:
            return package_data
        return False

    def validate_console_input(self, console_message=None, value=None, min=1, max=25):
        while True:
            user_input = console.input(console_message)
            if user_input == "":
                console.print(
                    f"[bold]{value} cannot be empty string. Try again[/]",
                    style="#FF4848 on black",
                )
                continue
            elif len(user_input) < min or len(user_input) > max:
                console.print(
                    f"[bold #FF4848]{value} must be between f{min} - {max} characters long. Try again[/]",
                    style="#FF4848 on black",
                )
                continue
            return user_input

    def get_option_2_data(self):
        """
        Runs when option 2 is selected to Collect data from console input.
        @return: A python dictionary containing key/value pair of the package data to save to the database.
        @rtype: dict
        """
        package_name = self.validate_console_input(
            value="package_name",
            console_message="[bold #64C9CF]Enter the name of the Package:[/] \n [bold #64C9CF]>>> [/]",
            min=2,
            max=20,
        )
        package_desc = self.validate_console_input(
            value="package_desc",
            console_message="[bold #64C9CF]Enter a brief description of the Package:[/] \n [bold #64C9CF]>>> [/]",
            min=5,
            max=50,
        )
        slug = self.validate_console_input(
            value="package_name",
            console_message="[bold #64C9CF]Enter the slug to refer the Package:[/] \n [bold #64C9CF]>>> [/]",
            min=2,
            max=20,
        )
        command_debian = self.validate_console_input(
            value="command_debian",
            console_message=f"[bold #64C9CF]Enter the command for installing {package_name} on [i]Debian[/i]:[/] \n [bold #64C9CF]>>> [/]",
            min=2,
            max=20,
        )
        command_fedora = self.validate_console_input(
            value="command_debian",
            console_message=f"[bold #64C9CF]Enter the command for installing {package_name} on [i]Fedora[/i]:[/] \n [bold #64C9CF]>>> [/]",
            min=2,
            max=20,
        )
        return {
            "package_name": package_name,
            "package_desc": package_desc,
            "slug": slug,
            "command_debian": command_debian,
            "command_fedora": command_fedora,
        }

    def get_option_3_data(self):
        """
        Runs when option 3 is selected to Collect data from console input.
        @return: A python dictionary containing key/value pair of the package data to save to the database.
        @rtype: dict
        """
        while True:
            pkg_to_query = console.input(
                "Package name, ID or slug \n [bold #64C9CF]>>> [/]"
            )
            if not self.package_is_in_db(pkg_to_query):
                console.print(
                    f"[bold]{pkg_to_query} could not be found in the database. Try again[/]",
                    style="#FF4848 on black",
                )
                continue
            break
        while True:
            option = console.input("\n [bold #64C9CF]>>> [/]")

            if option == "1":
                return self.get_option_2_data()

            elif option == "2":
                package_name = self.validate_console_input(
                    value="package_name",
                    console_message="[bold #64C9CF]Enter the name of the Package:[/] \n [bold #64C9CF]>>> [/]",
                    min=2,
                    max=20,
                )
                return {"package_name": package_name}

            elif option == "3":
                package_desc = self.validate_console_input(
                    value="package_desc",
                    console_message="[bold #64C9CF]Enter a brief description of the Package:[/] \n [bold #64C9CF]>>> [/]",
                    min=5,
                    max=50,
                )
                return {"package_desc": package_desc}

            elif option == "4":
                slug = self.validate_console_input(
                    value="package_name",
                    console_message="[bold #64C9CF]Enter the slug to refer the Package:[/] \n [bold #64C9CF]>>> [/]",
                    min=2,
                    max=20,
                )
                return {"slug": slug}

            elif option == "5":
                command_debian = self.validate_console_input(
                    value="command_debian",
                    console_message=f"[bold #64C9CF]Enter the command for installing the package on [i]Debian[/i]:[/] \n [bold #64C9CF]>>> [/]",
                    min=2,
                    max=20,
                )
                return {"command_debian": command_debian}

            elif option == "6":
                command_fedora = self.validate_console_input(
                    value="command_debian",
                    console_message=f"[bold #64C9CF]Enter the command for installing the package on [i]Fedora[/i]:[/] \n [bold #64C9CF]>>> [/]",
                    min=2,
                    max=20,
                )
                return {"command_fedora": command_fedora}

            elif option == "7":
                break
            else:
                console.print(
                    f"[bold]Invalid option selected. Try again[/]",
                    style="#FF4848 on black",
                )
                continue

    def get_option_4_data(self):
        """
        Runs when option 4 is selected to Collect data from console input.
        @return: class
        @rtype: <class 'PackagesAndCommands'>
        """
        while True:
            pkg_to_query = self.validate_console_input(
                value="package to delete",
                console_message="[bold #64C9CF]Package name, ID or slug:[/] \n [bold #64C9CF]>>> [/]"
            )
            if not self.package_is_in_db(pkg_to_query):
                console.print(
                    f"[bold]{pkg_to_query} could not be found in the database. Try again[/]",
                    style="#FF4848 on black",
                )
                continue
            return self.package_is_in_db(pkg_to_query)


class CommandOptionActions(ConsoleInputData):
    """
    Execute actions based on option selected
    """
    def create_table(self):
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
        table_data = self.get_option_1_table_data()
        table = Table()

        # Create table Headers. This could be dynamic by getting the database table column names, but will use static
        # values for now.
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
        return table

    def option_1_action(self):
        """
        Print a table of all Packages saved int he database.
        @return: None
        @rtype: None
        """
        table = self.create_table()
        console.print(table)

    def option_2_action(self):
        """
        Saves package data to database
        @return: None
        @rtype: None
        """
        data = self.get_option_2_data()
        pkg_to_add = PackagesAndCommands(**data)
        session.add(pkg_to_add)
        session.commit()