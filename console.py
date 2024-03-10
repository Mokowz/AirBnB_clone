#!/usr/bin/python3
"""Initalize the console"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
