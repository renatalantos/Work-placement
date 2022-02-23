import subprocess

cmd1 = "mkdir experiment"
returned_value = subprocess.call(cmd1, shell=True)  # returns the exit code in unix


cmd2 = "touch hello.txt"
returned_value = subprocess.call(cmd2, shell=True)  # returns the exit code in unix

cmd9 = "mv hello.txt experiment"
returned_value = subprocess.call(cmd9, shell=True)  # returns the exit code in unix

cmd3 = open("hello.txt", "w")
cmd3.write('print("Hello World")')

# cmd3.close()
returned_value = subprocess.call(cmd3, shell=True)  # returns the exit code in unix

cmd4 = "python3 hello.txt"
returned_value = subprocess.call(cmd4, shell=True)  # returns the exit code in unix

cmd5 = "rm hello.txt experiment"
returned_value = subprocess.call(cmd5, shell=True)  # returns the exit code in unix






