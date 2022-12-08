# cs5800-finalProj

## Before Running the Program
*   The user of the program must open MySQL Workbench and run the `create.sql` and then the `insert.sql` files in order for the program to work.
    *   These are located in the `SQL` directory
    *   If these files are not ran first, then the program may not output any data.
* The user must have the following packages installed:
    *   `tabular` via `pip3 install tabular`
    *   `pandas` via `pip3 install pandas`
    *   `mysql` via `pip3 install mysql`
    *   **NOTE** Please use your computer's appropriate version of `pip` to insure installation goes correctly.
*   In `dbConnector.py` please make sure that the info on lines 7 through 10 are correct for your device. **If you do not have a password for your SQL, comment out line 9** (for password). 
    *   Line 9 should be the only thing you need to change if you are like most users.

## The Entry Point to the Program
*   The entry point to the program is `main.py` located in `Optional/`

## Running `main.py`
*   `python3` is probably how you use `python` on your command line, if this is not the case, enter in your computer's python command to run `main.py`
    *   Ex: `python3 main.py`
*   There is an on screen menu telling you what part of the program you are in and what options you can select. The options are numbers, just enter a valid number to pick an option.
*   `INPUT` or `YOUR INPUT` is asking for a valid input from the user (what does the user want to see)
*   a valid `USAGE MESSAGE` will pop up with relevant information if an error occurs
    *   If you don't see output, it's probably working right.
*   *PLEASE NOTE* The program is case sensitive. Please check your spelling and capitalization appropriately and any other syntax.

## DeveloperView
*   The password is `password`
    *   You only need to enter this once per program run
*   Typing `X` can back you out to the main menu from this password screen