from app import cli_actions
from app.cli_options import PrintCommandLineOptions

cli_options = PrintCommandLineOptions()


def main():
    cli_options.print_main_menu_panel()


if __name__ == "__main__":
    main()
