#!/usr/bin/python3
"""Initalize the console"""
import cmd
from models import storage
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command proc class

    Args:
        cmd: description
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Creates new basemmodel

        Args:
            arg: class name
        """
        args = arg.split()

        if not args:
            print("** class name missing")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id.
        """
        args = arg.split()
        objdict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Destory a class instance"""
        args = arg.split()
        objdict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()
    
    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name.
        """
        args = arg.split()
        all_objects = storage.all()
        lst = []
        if len(args) == 0:
            # print all classes
            for value in all_objects.values():
                lst.append(str(value))
        elif args[0] in self.classes_list:
            # print just arg[0] class instances
            for (key, value) in all_objects.items():
                if args[0] in key:
                    lst.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(lst)

    def do_update(self, line):
        """ Updates an instance based on the class name
        """
        act = ""
        for argv in line.split(','):
            act = act + argv
        args = shlex.split(act)
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        if not self.attribute_verification(args):
            return
        all_objects = storage.all()
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip('"'):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(value, args[2], args[3])
                    storage.save()
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
