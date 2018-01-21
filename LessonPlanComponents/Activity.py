__author__ = 'Quinton'
from LessonPlanComponents.ActivityType import ActivityType

class Activity:

    def __init__(self):
        self.name = ""
        self.description = ""
        self.type = ActivityType.NONE
        self.materials = []
        self.initial_procedure = []   # procedure for initial day of teaching
        self.middle_procedure = []  # procedure for middle teaching, but not final review
        self.review_procedure = []  # procedure for final review of activity

    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type
        self.materials = []  # materials needed to complete the activity
        self.initial_procedure = []   # procedure for initial day of teaching
        self.middle_procedure = []  # procedure for middle teaching, but not final review
        self.review_procedure = []  # procedure for final review of activity
