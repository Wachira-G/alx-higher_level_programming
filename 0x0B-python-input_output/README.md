# Concept: 0x0B. Python - Input/Output

## Resources

**Read or watch:**

- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/)
- [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)

## Learning Objectives

### General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Python Test Cases

- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__`)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## Tasks

- **0.** Read file: A function that reads a text file (`UTF8`) and prints it to stdout
- **1.** Write to a file: a function that writes a string to a text file (UTF8) and returns the number of characters written
- **2.** Append to a file: a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added
- **3.** To JSON string: a function that returns the JSON representation of an object (string)
- **4.** From JSON string to Object:  a function that returns an object (Python data structure) represented by a JSON string
- **5.** Save Object to a file: a function that writes an Object to a text file, using a JSON representation
- **6.** Create object from a JSON file: a function that creates an Object from a “JSON file”
- **7.** Load, add, save:  a script that adds all arguments to a Python list, and then save them to a file
- **8.** Class to JSON: a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
- **9.** Student to JSON: a class Student that defines a student
- **10.** Student to JSON with filter: a class Student that defines a student by: (based on `9-student.py`)
- **11.** Student to disk and reload: a class Student that defines a student by: (based on `10-student.py`)
- **12.** Pascal's Triangle - Technical interview preparation:a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
