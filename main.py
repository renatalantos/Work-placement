import subprocess
import os

def create_dir():
    cmd = "mkdir experiment"
    returned_value = subprocess.call(cmd, shell=True)
create_dir()

# def create_file():
#     cmd = "touch hello.txt"
#     returned_value = subprocess.call(cmd, shell=True)
# create_file()


def create_file_and_populate():
    cmd = open("hello.txt", "w")
    cmd.write('print("Hello World")')
    cmd.close()
create_file_and_populate()

def move_file_into_dir():
    cmd = "mv hello.txt experiment"
    returned_value = subprocess.call(cmd, shell=True)
move_file_into_dir()

# def create_file_and_populate():
#     cmd = open("hello.txt", "w")
#     cmd.write('print("Hello World")')
#     cmd.close()
# create_file_and_populate()
# This is where the process stops and there are errors
# Also, another hello.txt file is created, with the print("Hello, World") command in it
# There is nothing in the hello.txt file in the experiment directory
# returned_value = subprocess.call(cmd4, shell=True)

def run_file():
    cmd = "python3 experiment/hello.txt"
    returned_value = subprocess.call(cmd, shell=True)
run_file()

def delete_file():
    cmd = "rm experiment/hello.txt"
    returned_value = subprocess.call(cmd, shell=True)
delete_file()