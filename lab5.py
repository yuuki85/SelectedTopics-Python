#1. Open file 
with open('test1.txt', 'w') as f: 
    for i in range(1, 5):
        f.write(str(i))
with open('test1.txt', 'r') as f: 
    print(f.read())


#2. Read file
#1st read
with open('test.txt') as f: 
    lines = list(f) 
 
#2nd read
with open('test.txt') as f: 
    lines = f.readlines()


#3. File handling
import os

def create_file(filename):
    try: 
        with open(filename, 'w') as f: 
            f.write('Hello, world!\n') 
        print("File " + filename + "created successfully.") 
    except IOError: 
        print("Error: could not create file " + filename) 

def read_file(filename):
    try: 
        with open(filename, 'r') as f: 
            contents = f.read()
            print(contents) 
    except IOError:
        print("Error: could not read file " + filename) 

def append_file(filename, text):
    try: 
        with open(filename, 'a') as f: 
            f.write(text) 
        print("Text appended to file "+ filename + " successfully.") 
    except IOError: 
        print("Error: could not append to file " + filename) 

def rename_file(filename, new_filename):
    try: 
        os.rename(filename, new_filename) 
        print("File " + filename + " renamed to " + new_filename + " successfully.") 
    except IOError: 
        print("Error: could not rename file " + filename) 

def delete_file(filename):
    try: 
        os.remove(filename) 
        print("File " + filename + " deleted successfully.") 
    except IOError: 
        print("Error: could not delete file " + filename) 


if __name__ == '__main__': 
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename) 
    read_file(filename) 
    append_file(filename, "This is some additional text.\n") 
    read_file(filename) 
    rename_file(filename, new_filename)
    read_file(new_filename) 
    #delete_file(new_filename)

#4. File path
import os
if os.path.isfile('test.txt'):
 print("It's a file") 
# Path
path = 'C:/Users/Norhaidah/Documents/pyenv/lab5/test.txt'
 
# Check whether the 
# specified path is 
# an existing file
isFile = os.path.isfile(path) 
print(isFile)

#6. Append a file
with open('test.txt', 'w') as f: 
    for i in range(1, 5):
        f.write(f'Number {i}\n') 
# Now add some extra lines using append mode
with open('test.txt', 'a') as f: 
    for i in range(5, 8):
        f.write(f'Append number {i}\n') 
with open('test.txt') as f: 
    print(f.read())

#7. Various ways to read file
# Program to show various ways to
# read data from a file.
# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Malaysia \n", "This is Singapore \n", "This is Indonesia \n"]

# Writing data to a file
file1.write("Hello Asean\n")
file1.writelines(L)
file1.close() # to change file access modes
file1 = open("myfile.txt", "r+")
print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))
print()

file1.seek(0)

# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

#6. Using contextlib
from contextlib import contextmanager

class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename
    
    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()
# usage
message_writer = MessageWriter('hello.txt')
with message_writer.open_file() as my_file:
    my_file.write('hello world')

#7. Append and write file
# Python program to illustrate
# Append vs write mode
file1 = open("myfile1.txt", "w")
L = ["This is Apple \n", "This is Strawberry \n", "This is Orange \n"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile1.txt", "a") # append mode
file1.write("Fruits \n")
file1.close()

file1 = open("myfile1.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile1.txt", "w") # write mode
file1.write("Citrus Type \n")
file1.close()

file1 = open("myfile1.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()


#TryThis1
import os

def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

if __name__ == '__main__':
    filename = "ImamSyafie.txt"
    read_file(filename)

#TryThis2
import os

def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            contents = f.readline()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

if __name__ == '__main__':
    filename = "ImamSyafie.txt"
    read_file(filename)

#TryThis3
import os

def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            for i in range(5):
                contents = f.readline()
                print(contents)
    except IOError:
        print("Error: could not read file " + filename)

if __name__ == '__main__':
    filename = "ImamSyafie.txt"
    read_file(filename)

#TryThis4
import os

def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            last_line = lines[-1]
            print(last_line)
    except IOError:
        print("Error: could not read file " + filename)

if __name__ == '__main__':
    filename = "ImamSyafie.txt"
    read_file(filename)

#TryThis5
import os

def count_character(filename, char):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            contents = f.read()
            count = contents.count(char)
            print(f"The character '{char}' appears {count}.")
    except IOError:
        print("Error: could not read file " + filename)

if __name__ == '__main__':
    filename = "ImamSyafie.txt"
    char = 'I'
    count_character(filename, char)

#TryThis6
import os

def copy_file(source_filename, dest_filename):
    try:
        with open(source_filename, 'r', encoding="utf-8") as source_file:
            contents = source_file.read()

        with open(dest_filename, 'w', encoding="utf-8") as dest_file:
            dest_file.write(contents)

        print(f"Successfully copied content.")
    except IOError:
        print("Error: could not read file " + source_filename)

if __name__ == '__main__':
    source_filename = "ImamSyafie.txt"
    dest_filename = "ImamSyafieCopy.txt"
    copy_file(source_filename, dest_filename)