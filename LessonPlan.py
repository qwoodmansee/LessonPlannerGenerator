__author__ = 'Quinton'
from LessonPlanComponents.Grades import Grades
from LessonPlanComponents.Objectives import Objective
class LessonPlan:

    def __init(self):
        self.name = ""
        self.number =  0
        self.description = ""
        self.preparing = ""
        self.presenting = ""
        self.practicing = ""
        self.grade = Grades.NONE
        self.objectives = []
        self.standards = []
        self.activities = []

    