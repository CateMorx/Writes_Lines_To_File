#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 3 
#Write a method in python to write multiple line of text contents into a text file mylife.txt.

#Imports necessary elements
import PySimpleGUI as psg
import tkinter as tk

#Creates Method that allows user to write to "my_file.txt" text file
def write_file():
    #opens and writes to "my_file.txt"
    with open("my_file.txt", "w") as file: 
        #Prompts user for input
        line = input(str("Enter line: "))
        #Writes the input in the file
        file.write(line + "\n")
        #Asks user if they want to input more lines
        more_lines = input(str("Are there more lines y/n? "))
        #Does not accept invalid input and prompts user to only enter y or n
        while not more_lines or more_lines[0].lower() not in ['y', 'n']:
            more_lines=input(str("Invalid input, please only enter 'y', or 'n'"))
        #Allows user to input another line if Yes
        while more_lines[0].lower() == 'y':
            line = input(str("Enter line: "))
            file.write(line + "\n")
            more_lines = input(str("Are there more lines y/n? "))
            #Does not accept invalid input and prompts user to only enter y or n
            invalid_count = 0
            while not more_lines or more_lines[0].lower() not in ['y', 'n']:
                invalid_count += 1
                if invalid_count >= 2:
                    print("Invalid input, please only enter 'y', or 'n'")
                    invalid_count = 0
                else:
                    more_lines = input("Invalid input, please only enter 'y', or 'n'")
            #Ends the program if No
            if more_lines[0].lower() == 'n':
                break

#Calls Method
write_file()

#Creates a Method to Display the "my_file.txt" file with GUI
def GUI():
    #Opens and reads the "my_file.txt" file
    with open("my_file.txt", "r") as read_file:
        output_text = read_file.read()

#Calls Method
GUI()