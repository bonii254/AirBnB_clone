#!/usr/bin/python3
"""Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Attributes:
        name (str): The name of the amenity.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity instance."""
        super().__init__(*args, **kwargs)

    name = ""
