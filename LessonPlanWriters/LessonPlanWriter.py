from abc import ABC, abstractmethod
__author__ = 'Quinton'


class LessonPlanWriter(ABC):
    @abstractmethod
    def WriteFile(self, filename, lessonPlan):
        pass