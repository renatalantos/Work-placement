import subprocess
import os
import time

def create_new_file():
    """
    Creates new file test_11.html.
    """
    cmd = "touch test_11.html "
    returned_value = subprocess.call(cmd, shell=True)
    print("Create new file.")

create_new_file()

def move_file_into_dir():
    """
    Moves file test_11.html into test_results directory.
    """
    cmd = "mv test_11.html test_results/branch_name1"
    returned_value = subprocess.call(cmd, shell=True)
    print("Move file into test_results directory.")
move_file_into_dir()

def create_back_up_dir():
    """
    Creates backup directory.
  
    """
    cmd = "mkdir test_results_back_up"
    returned_value = subprocess.call(cmd, shell=True)
    print("Creates backup directory.")

create_back_up_dir()


def move_folder_into_dir():
    """
    Move test_results folder into backup directory.
    """
    cmd = "cp -r test_results test_results_back_up "
    returned_value = subprocess.call(cmd, shell=True)
    print("Test result folder moved into new backup directory.")


move_folder_into_dir()


def change_name_to_time():
    """
    Renames test_results folder to test_results + timestamp.
    """

    os.rename(
        "test_results_back_up/test_results",
        time.strftime("test_results_back_up/test_results_%Y-%m-%d %H:%M:%S"),
    )
    print("Folder test_results renamed with timestamp.")
change_name_to_time()