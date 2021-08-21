from app import console, session
from app.models import PackagesAndCommands


class CommandLineActions:
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

        # execption that might occur when you getting field_names but the data_objects list is empty(nothing in the database)
        except IndexError:
            return {}
