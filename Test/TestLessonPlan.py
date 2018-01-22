__author__ = 'Quinton'
from LessonPlan import LessonPlan
from LessonPlanComponents.Grades import Grades
from LessonPlanComponents.Objectives import Objective
from LessonPlanComponents.Activity import Activity
from LessonPlanComponents.ActivityType import ActivityType
from Standards.OhioStateStandards import OhioStateStandards

def generateTestLessonPlan():
    testObjectives = [
        Objective("Sing, read, write, and hear songs with fa", ""),
        Objective("Sing, read, write, and hear songs with  whole notes", "")
    ]

    testLessonPlan = LessonPlan()
    testLessonPlan.name = "TEST Fourth- Lesson 18 TEST"
    testLessonPlan.number = 18
    testLessonPlan.description = "a test lesson plan for 4th grade lesson 18"
    testLessonPlan.preparing = None
    testLessonPlan.presenting = "Whole note"
    testLessonPlan.practicing = "fa"
    testLessonPlan.grade = Grades.FOURTH
    testLessonPlan.objectives = testObjectives
    testLessonPlan.standards = buildTestStandards()
    testLessonPlan.activities = buildTestActivies()

    return testLessonPlan

def buildTestStandards():
    ohioStateStandards = OhioStateStandards()
    testStandards = ohioStateStandards.standards[Grades.FOURTH]
    testStandards["creating"][2].metByLesson = True
    testStandards["creating"][4].metByLesson = True
    testStandards["creating"][5].metByLesson = True
    testStandards["performing"][0].metByLesson = True
    testStandards["performing"][1].metByLesson = True
    testStandards["performing"][3].metByLesson = True
    testStandards["performing"][5].metByLesson = True
    testStandards["performing"][6].metByLesson = True
    testStandards["responding"][4].metByLesson = True
    return testStandards

def buildTestActivies():
    testActivies = []
    testActivies.append(Activity("Hello Song", "", ActivityType.REVIEW_ACTIVITY, [], [], [], ["Come in, go to seats, sing Hello Song"]))
    testActivies.append(Activity("I CAN statements", "", ActivityType.REVIEW_ACTIVITY, [], [], [], ["Review the goals for the day!"]))
    testActivies.append(Activity("Boots of Shining Leather", "", ActivityType.MIDDLE_ACTIVITY, [], [], ["Review this song for \"long\"", "Memorize this song by words disappearing", "Teach students the concentric circle singing game"], []))
    testActivies.append(Activity("Gypsy In the Moonlight", "", ActivityType.REVIEW_ACTIVITY, ["Scarves"], [], [], ["Sing this song and play the fun singing game"]))
    testActivies.append(Activity("Sing I Got A Letter while going back to seats on carpet", ["Envelope"],  ActivityType.TRANSITION, [], [], [], []))
    testActivies.append(Activity("I Got A Letter Whole Note Prep Board Work", "", ActivityType.MIDDLE_ACTIVITY, [], [], ["Play this fun letter finding game for long"], []))
    testActivies.append(Activity("INTRODUCE WHOLE NOTE", "", ActivityType.INITIAL_ACTIVITY, [], ["Introduce the whole note to students"], [], []))
    testActivies.append(Activity("I Got A Letter with whole note", "", ActivityType.INITIAL_ACTIVITY, ["Envelope"], ["Sing this song with on the rhythm with whole note"], [], []))
    testActivies.append(Activity("Divide into two rows for ball rolling activity", "", ActivityType.TRANSITION, [], [], [], []))
    testActivies.append(Activity("Ball rolling for whole note!", "", ActivityType.INITIAL_ACTIVITY, ["Tennis Balls"], ["Students sit in 2 lines and bounce the ball on beat and roll the ball on each whole note", "I Got A Letter", "Somebody's Knocking", "Epo i tai tai e", "Gypsy in the Moonlight"], [], []))
    testActivies.append(Activity("Recorders", "", ActivityType.REVIEW_ACTIVITY, ["Recorders"], [], [], ["Continue recorder unit!"]))
    testActivies.append(Activity("Additional Time", "", ActivityType.REVIEW_ACTIVITY, ["SmartBoard Files"], [], [], ["Son Macaron, Sarasponda, Early in the morning, Obwisanna, Love Somebody"]))
    return testActivies