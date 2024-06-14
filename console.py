#!/usr/bin/python3
"""
This module defines the command interface that controls the console
"""

import cmd as c
import os
import uuid
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(c.Cmd):
    """implements the commandline intepereter
    """
    prompt = "(hbnb) "
    valid_classes = {
            'BaseModel',
            'User',
            'State',
            'City',
            'Amenity',
            'Place',
            'Review'
            }

    def do_EOF(self, line):
        """exits the program when ctrl + d is
        entered
        """
        print('')
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered.
        it shoud do nothing
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file)
        """
        command = self.parseline(line)[0]
        if command is None:
            print('** class name is missing **')

        elif command not in self.valid_classes:
            print('** class doesn\'t exist **')

        else:
            my_in = BaseModel()
            my_in.save()
            print(my_in.id)

    def do_show(self, line):
        """prints the string representation of an
        instance based on the class name and id
        """

        command = self.parseline(line)[0]
        args = self.parseline(line)[1]

        if command is None:
            print('** class name missing **')

        elif command not in self.valid_classes:
            print('** class doesn\'t exist **')

        elif args is None or len(args.split()) < 1:
            print('** instance id missing **')

        else:
            
            id = args.split()[0]

            key = f"{command}.{id}"
            instance = models.storage.all().get(key)
            if instance == None:
                print('** no instance found **')
            else:
                print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the 
        class name and id (save the change 
        into the JSON file)
        """

        command = self.parseline(line)[0] 
        args = self.parseline(line)[1]

        if command is None:
            print('** class name missing **')

        elif command not in self.valid_classes:
            print('** class doesn\'t exist **')

        elif args is None or len(args.split()) < 1:
            print('** instance id missing **')

        else:
            id = args.split()[0]
            key = f"{command}.{id}"
            instance = models.storage.all().get(key)
            if instance is None:
                print('** no instance is found **')
            else:
                print(instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
