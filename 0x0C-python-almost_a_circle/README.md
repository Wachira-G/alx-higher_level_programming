# Concept: 0x0C. Python - Almost a circle

## Background Context

The AirBnB project is a big part of the Higher level curriculum.
This project helps one get ready for it.

In this project, we review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

We also learn about:

- args and kwargs
- Serialization/Deserialization
- JSON

## Resources

**Read or watch:**

- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives

### General

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Python Unit Tests

- We use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- The file organization in the tests folder is the same as in the project: ex: for `models/base.py`, unit tests are in: `tests/test_models/test_base.py`
- All tests executed by using this command: `python3 -m unittest discover tests`
- We can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py` for the `test_base.py` file

## How to use

- The `_-main.py` files are the main files for each task that demonstrate the output for each task. We can run each - example `./0-main.py`.
- The basic functionality is defined in the `modules/`

## Tasks

0. **If it's not tested it doesn't work** - the task holds the test cases for all the mandatory tasks

1. **Base class** - creates the `Base` class

2. **First Rectangle** - creates the class `Rectangle` that inherits from Base

3. **Validate attributes** - updates the class `Rectangle` by adding the validation of all setter methods and instantiation

4. **Area first** - updates the class `Rectangle` by adding the public method `area` that returns the area value of the Rectangle instance.

5. **Display #0** - updates the class `Rectangle` by adding the public method `display` that prints in stdout the `Rectangle` instance with the character `#`.

6. **__str__** - updates the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.

7. **Display #1** - updates the class `Rectangle` by improving the public method `display` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`.

8. **Update #0** - updates the class `Rectangle` by adding the public method `update(self, *args)` that assigns an argument to each attribute: `id`, `width`, `height`, `x`, and `y`.

9. **Update #1** - updates the class `Rectangle` by updating the public method `update` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes

10. **And now, the Square!** - Writes the class `Square` that inherits from `Rectangle`

11. **Square size** - updates the class `Square` by adding the public getter and setter `size`

12. **Square update** - updates the class `Square` by adding the public method `update(self, *args, **kwargs)` that assigns attributes

13. **Rectangle instance to dictionary representation** - updates the class `Rectangle` by adding the public method `to_dictionary` that returns the dictionary representation of a `Rectangle`. The dictionary contains `id`, `width`, `height`, `x`, and `y`.

14. **Square instance to dictionary representation** - updates the class `Square` by adding the public method `to_dictionary` that returns the dictionary representation of a `Square` with the attributes `id`, `size`, `x`, and `y`.

15. **Dictionary to JSON string** - updates the class `Base` by adding the static method `to_json_string(list_dictionaries)` that returns the JSON string representation of `list_dictionaries`( a list of dictionaries).

16. **JSON string to file** - updates the class `Base` by adding the class method `save_to_file(cls, list_objs)` that writes the JSON string representation of `list_objs` to a file. The `list_objs` is a list of instances that inherits from `Base` - for example, a list of `Rectangle` or list of `Square` instances

17. **JSON string to dictionary** - update the class `Base` by adding the static method `from_json_string(json_string)` that returns the list of the JSON string representation `json_string`. The `json_string` is a string representing a list of dictionaries.

18. **Dictionary to Instance** - updates the class `Base` by adding the class method `create(cls, **dictionary)` that returns an instance with all attributes already set.

19. **File to instances** - updates the class `Base` by adding the class method `load_from_file(cls)` that returns a list of instances. The filename is `<Class name>.json` - example: `Rectangle.json`.

20. **JSON ok, but CSV?** *#advanced* - updates the class `Base` by adding the class methods `save_to_file_csv(cls, list_objs)` and `load_from_file_csv(cls)` that serializes and deserializes in CSV. The filename is `<Class name>.csv` - example: `Rectangle.csv`.

21. **Let's draw it** *#advanced* - updates the class `Base` by adding the static method `draw(list_rectangles, list_squares)` that opens a window and draws all the `Rectangles` and `Squares` using the module [Turtle Graphics Module](https://docs.python.org/3.0/library/turtle.html).
