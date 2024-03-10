#!/usr/bin/python3
"""Initalize the console"""
import cmd
from models import storage


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
            print(eval(argv[0])().id)
            storage.save()

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id.
        """
        argv = parse(arg)
        objdict = storage.all()
        if not argv:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argv[0], argv[1])])

    def do_destroy(self, arg):
        """Destory a class instance"""
        argv = parse(arg)
        objdict = storage.all()
        if not argv:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argv[0], argv[1])]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
