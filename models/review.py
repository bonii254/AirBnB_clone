#!/usr/bin/python3
"""This module defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Attributes:
        place_id (str): The ID of the place associated with the review.
            user_id (str): The ID of the user who wrote the review.
            text (str): The text content of the review.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance."""
        super().__init__(*args, **kwargs)

    place_id = ""
    user_id = ""
    text = ""
