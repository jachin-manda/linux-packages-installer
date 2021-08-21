from app import console
from app.cli import CliActions, CliInterface

cli_interface = CliInterface("banner.txt")
cli_action = CliActions()


def get_and_validate_user_input(options):
    running = True
    while running:
        user_input = console.input("[bold yellow]Select [i]option[/i][/]? :smiley: ")
        if user_input not in options:
            console.print("[bold]Invalid option or input[/bold]", style="black on red")
            continue
        return user_input


def main():
    cli_interface.print_logo()
    running = True
    while running:
        cli_interface.print_main_menu()
        option = get_and_validate_user_input(["1", "2", "3", "4", "5", "6"])
        if option == "1":
            cli_action.option_1()
        elif option == "2":
            cli_action.option_2()
        elif option == "3":
            cli_action.option_3()
        elif option == "4":
            cli_action.option_4()
        elif option == "5":
            cli_action.option_5()
        elif option == "6":
            running = False


if __name__ == "__main__":
    main()
