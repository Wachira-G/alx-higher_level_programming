#!/usr/bin/python3

"""
A module containing a class that forms the base for all other classes.
It instantiates the id attribute for each instance.
"""

import json


class Base:
    """
    Is a base for all other classes of this project.
    Manages the id attribute in all the future classes
    to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        A class constructor that assigns an id to an instance
        and increments the number of instances in the class.

        Args:
            id (int): Identifies an instance uniquely.
        """

        if id is not None:
            self.id = id  # Assume id is an int and no need to test its type

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries:
        list_dictionaries is a list of dictionaries
        If list_dictionaries is None or empty, return the string: "[]"
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None\
                or not isinstance(list_dictionaries, list)\
                or bool(list_dictionaries) is False:
            return '[]'
        else:
            try:
                return json.dumps(list_dictionaries)
            except TypeError:
                return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """
         Writes the JSON string representation of list_objs to a file:
         list_objs is a list of instances who inherits of Base
           - example: list of Rectangle or list of Square instances
        If list_objs is None, save an empty list
        The filename must be: <Class name>.json - example: Rectangle.json
        You must use the static method to_json_string (created before)
        You must overwrite the file if it already exists
        """
        filename = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []

        json_str = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string:
        json_string is a string representing a list of dictionaries
        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set:

        Creates a “dummy” instance before:
          Creating a Rectangle or Square instance
           with 'dummy' mandatory attributes
          then calls update instance method
           to this 'dummy' instance to apply the real values
        """
        if cls.__name__ == 'Square':
            dummy_instance = cls(1)

        elif cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)

        else:
            # Handle other classes here if needed
            raise NotImplementedError(f"Class '{cls.__name__}' not supported.")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file:

        The filename must be: <Class name>.json - example: Rectangle.json
        If the file doesn't exist, return an empty list
        Otherwise, return a list of instances
        - the type of these instances depends on cls
          (current class using this method)
        You must use the from_json_string
          and create methods (implemented previously)
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_str = file.read()
        except FileNotFoundError:
            return []
        if json_str == '[]':
            return []
        return [
                cls.create(**dic) for dic in cls.from_json_string(json_str)
                ]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            list_objs (list): a list containing the instance description
        """
        import csv
        filename = cls.__name__ + '.csv'
        '''if list_objs is None:
            list_objs = []

        dicts = [obj.to_dictionary() for obj in list_objs]
        if cls.__name__ == "Rectangle":
            lines = ''
            for obj in dicts:
                lines += "{},{},{},{}\n".format(
                    ['id'], obj['width'], obj['height'], obj['x'], obj['y'])

        elif cls.__name__ == "Square":
            lines = ''
            for obj in dicts:
                lines += "{},{},{},{}\n".format(
                    obj['id'], obj['size'], obj['x'], obj['y'])

        else:
            lines = ''

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(lines)'''
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes from CSV
        """
        import csv
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        dictionary = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height': int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                    elif cls.__name__ == 'Square':
                        dictionary = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                            }
                    instances.append(cls.create(**dictionary))
            return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """static method def draw(list_rectangles, list_squares)

        Args:
            list_rectangles (list): A list of rectangle instances
            list_squares (list): A list of square instances
        """
        '''
        You must use the Turtle graphics module
        To install it: sudo apt-get install python3-tk
        To make the GUI available outside your vagrant machine,
          add this line in your Vagrantfile: config.ssh.forward_x11 = true
        No constraints for color, shape etc… be creative!

        Uncommented line in '/etc/ssh/ssh_config'
         that said '# ForwardX11 no' and change 'no' to 'yes'.
        Then added line 'config.ssh.forward_agent = true'
          to my Vagrantfile in addition to 'config.ssh.forward_x11 = true'.
        Halted my vm with 'vagrant halt'
         and started it back up with 'vagrant up --provision'
           then 'vagrant ssh'.
        If you get an error that looks like
            '/usr/bin/xauth: timeout in locking
              authority file /home/vagrant/.Xauthority',
          then enter 'rm .Xauthority' (you may have to 'sudo').
        Logout and restart the vm with 'vagrant up --provision'.
        Test with 'xeyes'. If Xquartz is installed on the Mac OS
          it should open in an Xquartz window.
        '''
        pass
