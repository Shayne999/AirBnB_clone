#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.

    Attributes:
        email (str): User email.
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
