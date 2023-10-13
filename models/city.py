#!/usr/bin/python3
"""This module defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
        Attributes:
            state_id (str): The ID of the state where the city is located.
            name (str): The name of the city.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new City instance."""
        super().__init__(*args, **kwargs)

    state_id = ""
    name = ""
