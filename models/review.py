#!/usr/bin/python3
"""Defines a review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define a review class"""
    place_id = ""
    user_id = ""
    text = ""
