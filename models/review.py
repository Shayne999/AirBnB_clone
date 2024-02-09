#!usr/bin/python3
"Defines Review class"

from model.base_model import BaseModel


class Review(BaseModel):
    """Represents reviews.

    Attributes:
        place_id (str): The ID of the place
        user_id (str): The users's ID
        text (str): The review
    """

    Place_id = ""
    User_id = ""
    text = ""
