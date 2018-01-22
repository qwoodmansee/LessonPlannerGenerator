__author__ = 'Quinton'
from enum import Enum
class Grades(Enum):
    NONE = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5


    def __str__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:  returns the grade in form "[value] Grade" ex. "First Grade"
        """
        return self.name.title() + " Grade"

