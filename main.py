from Test import TestLessonPlan
from LessonPlanWriters.WesthovenWriter import WesthovenWriter

def main():
    testLesson18()
    return 0

def testLesson18():
    testLessonPlan = TestLessonPlan.generateTestLessonPlan()
    testWesthovenWriter = WesthovenWriter()
    testWesthovenWriter.WriteFile(testLessonPlan.name + '.docx', testLessonPlan)

if __name__ == "__main__":
    main()