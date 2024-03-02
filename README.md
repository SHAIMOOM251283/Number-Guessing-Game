Number Guessing Game

Number Guessing Game is a simple and entertaining Python game where players attempt to guess a sequence of randomly generated numbers within a limited number of attempts.

Features

    Randomly generated target numbers between 1 and 100.
    Three target numbers to guess sequentially.
    Limited number of attempts to guess each number.
    Timer to keep track of the remaining time to complete the game.
    Feedback on each guess indicating whether the guess is too high, too low, or correct.
    Score calculation based on the number of attempts and time taken to complete the game.
    Restart option available at any time during the game.
    Standalone executable for easy and convenient gameplay.

How to Play

    Run the standalone executable (number_guessing_game.exe on Windows) located in the dist directory.
    Enter your guess for the current target number between 1 and 100.
    Press Enter to submit your guess.
    Receive feedback on your guess and continue guessing until you correctly guess all three target numbers or exhaust the maximum number of attempts.
    After correctly guessing each number, 70 seconds are deducted from the remaining time, intensifying the challenge.
    Upon correctly guessing all three numbers, the time remaining is used to calculate the time bonus score. Each second remaining contributes to your bonus score, multiplied by 30.
    Optionally, press Space to restart the game at any time.

Requirements

    Python 3.x
    Pygame library

Using the Repository

    Clone the repository: git clone https://github.com/your-username/number-guessing-game.git
    Navigate to the project directory: cd number-guessing-game
    Ensure you have Python installed.
    Install Pygame library: pip install pygame
    To generate the dist folder and executable file, run the appropriate build command (e.g., PyInstaller) on your local machine.

.gitignore

The .gitignore file in this repository excludes the following folders from version control:

    dist/: Contains generated executable files.
    build/: Contains build artifacts.
    venv/: Contains virtual environment files.
    
    Users are encouraged to generate the dist folder themselves by running the appropriate build command (e.g., PyInstaller) on their local machine. This ensures that the executable file is generated based on their specific
    environment and needs.

Building Standalone Executables

To create standalone executables for the game, you can use PyInstaller, a Python packaging tool that bundles Python applications into standalone executables. Two common commands are provided below:

    Using --noconsole flag: pyinstaller --noconsole number_guessing_game.py
    This command creates a standalone executable from the number_guessing_game.py script without displaying a console window. If your game does not require user input or output to the console, this flag can be useful to
    hide the console window when the game is running.

    Without --noconsole flag: pyinstaller number_guessing_game.py
    This command creates a standalone executable from the number_guessing_game.py script. If your game logic is contained within this script, this command will generate an executable for your game.

After running one of these commands, PyInstaller will create the dist folder containing the standalone executables for your game. You can then distribute these executables to users who want to play your game without needing to install Python or any dependencies.


Credits

    Developed by Shaimoom Shahriar

License

This project is licensed under the MIT License - see the LICENSE file for details.
