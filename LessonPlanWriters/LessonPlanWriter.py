__author__ = 'Quinton'
from abc import ABC, abstractmethod


class LessonPlanWriter(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def WriteFile(self, filename):
        pass