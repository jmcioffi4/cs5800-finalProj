from terminal import terminal, usageMessage
from menu import menu

if __name__ == "__main__":
    # TODO: Implement the menu here
    
    # Repeat the terminal until the user enters "exit" or uses keyboard interrupt
    try:
        terminal()
    except KeyboardInterrupt:
        usageMessage("!!GoodBye!!")