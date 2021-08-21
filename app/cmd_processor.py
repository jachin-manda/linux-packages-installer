from app import console
import subprocess
import json


class CommandInstaller:
    def __init__(self, instances, linux_system=None):
        self.instances = instances
        self.linux_system = linux_system

    def prepare_all_packages(self):
        columns = (
            self.instances[0].metadata.tables["packages_and_commands"].columns.keys()
        )
        data = []
        dictionary = {}
        for instance in self.instances:
            for column in columns:
                dictionary[column] = getattr(instance, column)
            data.append(dictionary)
        return data

    def install_packages(self):
        for pkg in self.prepare_all_packages():
            install_cmds = json.loads(
                pkg[
                    "command_debian"
                    if self.linux_system == "debian"
                    else "command_fedora"
                ]
            )
            for cmd in install_cmds:
                console.print(
                    f"[bold]Installing package {pkg['package_name']}[/]",
                    style="#28FFBF",
                )
                with console.status("", spinner="moon"):
                    subprocess.run(cmd, shell=True)
                    console.print(
                        f"[bold]Finnished[/]",
                        style="#BCFFB9",
                    )
