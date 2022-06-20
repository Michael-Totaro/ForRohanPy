# If you haven't read the README File for the ForRohan Java
# project yet, I suggest you do so as the information it it
# will be helpful for understanding how to run this program.

# Step 1: Download Python
#   Go to this link -> https://www.python.org/downloads/
#   click on the yellow "Download Python 3.10.5" button
#   Should be pretty straight foward from there.

# Step 2: Check if Python is installed
#   go to terminal and type the following command
#   python3
#   If the terminal outputs "Python3 3.10.5" and some
#   other stuff, your good.
#   Press "control d" on your keyboard to cancel the python
#   session

# Step 3: Text editor
#   Have "Atom" downloaded on your computer, if you
#   don't already have this, go to this Github repo ->
#   https://github.com/Michael-Totaro/ForRohan

# Step 4: Create Directories
#   Copy and paste the following commands into your
#   terminal in the following order:
#
#   mkdir ForRohanPy
#   cd ForRohanPy
#   touch Playground.py
#   touch mod.py
#   touch ex.py
#   cd ~
#   open -a "Atom" ForRohanPy
#
#   When you open it click on the folder on the left and open
#   the three blank files.

# Step 5: Copy and paste files
#   Go to this Github repo, while leaving Atom open. ->
#
#   Copy and paste the files in "ForRohanPy" into their corresponding
#   files in Atom and save by pressing "command s".

# Step 6: Run files
#   Go to your terminal and type the following commands to run:
#   cd ~
#   cd ForRohanPy
#   python3 Playground.py

# Step 7: Enjoy
#   Have fun!!!!!!

import mod

# Creates and returns a valid rohan object
def r2():
    return mod.Rohan("USC", "4/20/2021", "chicken thing", "football")

# Prints info on Rohan and allows the user to enter info to create a user object
# In a function for readibility purposes only.
def main():
    r = mod.Rohan("the University of South Carolina", "5/26/2022", "gamecock", "golf")
    nl = '\n'

    print(f"{nl}Rohan is a student at {r.school}. He is {r.age} years old. His school's mascot is a"
          f" {r.mascot}. His favorite sport is {r.sport}.{nl}")

    print(f"Rohan is a student at {r2().school}. He is {r2().age} years old."
          f" His school's mascot is a {r2().mascot}. His favorite sport is {r2().sport}.{nl}")

    school = input("What is Rohan's school: ")
    date = input("\nWhat is today's date (Format MM/DD/YYYY): ")
    mascot = input("\nWhat is Rohans schools mascot: ")
    sport = input("\nWhat is Rohans favorite sport: ")

    num = int(input("\nPress '0' to print information about Rohan. Press '1' to have no chance of an exception being thrown. : "))

    if num == 0:
        r3 = mod.Rohan(school, date, mascot, sport)

        print(f"{nl}Rohan is a student at {r3.school}. He is {r3.age} years old."
              f" His school's mascot is a {r3.mascot}. His favorite sport is {r3.sport}.{nl}")
    else:
        print("\nYou didn't want an exception to be thrown. Object creation canceled.\n")

main()
