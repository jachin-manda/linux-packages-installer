from app import console
from app.cli_options import PrintCommandLineOptions
from app.cli_actions import CommandOptionActions

cli_options = PrintCommandLineOptions()
cli_action = CommandOptionActions()


def get_main_menu_input():
    running = True
    while running:
        cli_options.print_main_menu_panel()
        user_input = console.input("[bold #64C9CF]Select option:[/] \n [bold #64C9CF]>>> [/]")
        if user_input == "1":
            cli_action.option_1_action()

        elif user_input == "2":
            cli_action.option_2_action()

        elif user_input == "3":
            cli_action.option_3_action()

        elif user_input == "4":
            cli_action.option_4_action()

        elif user_input == "5":
            cli_action.option_5_action()

        elif user_input == "6":
            awaiting_input = True
            while awaiting_input:
                cli_options.print_option_6()
                quit_opt = console.input("[bold #64C9CF]type yes or no:[/] \n [bold #64C9CF]>>> [/]")
                if quit_opt == "yes":
                    running = False
                    break
                elif quit_opt == "no":
                    break
                else:
                    console.print(
                        f"[bold]Invalid option selected.[/]",
                        style="#FF4848 on black",
                    )
                    continue

        else:
            console.print(
                f"[bold]Invalid option selected.[/]",
                style="#FF4848 on black",
            )
            continue




def main():
    get_main_menu_input()


if __name__ == "__main__":
    main()
