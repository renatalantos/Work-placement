import subprocess
"""
We use Python subprocess module to execute system commands.
"""


def create_dir():
    """
    Creates a directory called experiment in the root directory.
    """
    cmd = "mkdir experiment"
    returned_value = subprocess.call(cmd, shell=True)
    print("1")
create_dir()


def create_file_and_populate():
    """
    Creates a file called hello.txt in root directory and populates it
    with print("Hello World") statement. Closes file after poulating.
    No use of subprocess module here.
    """
    cmd = open("hello.txt", "w")
    cmd.write('print("Hello World")')
    cmd.close()
    print("2")
create_file_and_populate()


def move_file_into_dir():
    """
    Moves file hello.txt into experiment directory.
    """
    cmd = "mv hello.txt experiment"
    returned_value = subprocess.call(cmd, shell=True)
    print("3")
move_file_into_dir()


def run_file():
    """
    Executes content of hello.txt file.
    """
    cmd = "python3 experiment/hello.txt"
    returned_value = subprocess.call(cmd, shell=True)
    print("4")
run_file()


def delete_file():
    """
    Deletes hello.txt from experiment directory.
    """
    cmd = "rm experiment/hello.txt"
    returned_value = subprocess.call(cmd, shell=True)
    print("5")
delete_file()