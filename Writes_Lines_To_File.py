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
        #Allows user to input another line if Yes
        while more_lines[0].lower() == 'y':
            line = input(str("Enter line: "))
            file.write(line + "\n")
            more_lines = input(str("Are there more lines y/n? "))
            #Ends the program if No
            if more_lines[0].lower() == 'n':
                break

#Calls Method

#Creates a Method to Display the "my_file.txt" file with GUI

#Calls Method