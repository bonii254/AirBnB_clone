#!/usr/bin/python3
# states class

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """initialize state instances"""
        super().__init__(*args, **kwargs)

    name = ""
