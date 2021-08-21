from app import cli_actions
from app.cli_options import PrintCommandLineOptions
from app.cli_actions import CommandLineActions

cli_options = PrintCommandLineOptions()
cli_actions = CommandLineActions()


def main():
    cli_options.print_main_menu_panel()


if __name__ == "__main__":
    main()
