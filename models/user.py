#!/usr/bin/python3

""" class User that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
