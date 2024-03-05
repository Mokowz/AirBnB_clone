#!/usr/bin/python3
"""Defines an init file"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
