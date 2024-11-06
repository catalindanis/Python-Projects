from UserInterface.Console import showMenu

def main():
    """
    Main function of the application that coordinates the behaviour of the program
    :return:
    """
    exit_requested = False
    while not exit_requested:
        if showMenu() == False:
            exit_requested = True

if __name__ == "__main__":
    main()
