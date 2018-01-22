__author__ = 'Quinton'
from LessonPlanComponents.ActivityType import ActivityType

class Activity:

    def __init__(self, name, description, type, materials, initial_procedures, middle_procedures, review_procedures):
        self.name = name
        self.description = description
        self.type = type
        self.materials = materials  # materials needed to complete the activity
        self.initial_procedures = initial_procedures   # procedure for initial day of teaching
        self.middle_procedures = middle_procedures  # procedure for middle teaching, but not final review
        self.review_procedures = review_procedures  # procedure for final review of activity
