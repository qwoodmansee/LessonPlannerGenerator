from __future__ import print_function
from docxtpl import DocxTemplate, R
from LessonPlanWriters.LessonPlanWriter import LessonPlanWriter
from LessonPlanComponents.ActivityType import ActivityType
__author__ = 'Quinton'

class WesthovenWriter(LessonPlanWriter):
    def __init__(self):
        super().__init__()

    def WriteFile(self, filename, lessonPlan):
        template = "WesthovenLessonPlanTemplate.docx"
        document = DocxTemplate(template)
        activitiesAndProceduresLists = self._buildActivitiesAndProceduresRichTextLists(lessonPlan.activities)
        context = {
            'GRADE' : R(str(lessonPlan.grade), style="GradeStyle"),
            'LESSONNUMBER': R(str(lessonPlan.number), style="LessonNumberStyle"),
            'PREPARING': R(lessonPlan.preparing, style="PPPStyle"),
            'PRESENTING': R(lessonPlan.presenting, style="PPPStyle"),
            'PRACTICING': R(lessonPlan.practicing, style="PPPStyle"),
            'OBJECTIVES': self._buildObjectivesRichTextString(lessonPlan.objectives),
            'CESTANDARDS': self._buildStandardsRichTextString(lessonPlan.standards["creating"]),
            'PRSTANDARDS': self._buildStandardsRichTextString(lessonPlan.standards["performing"]),
            'RESTANDARDS': self._buildStandardsRichTextString(lessonPlan.standards["responding"]),
            'MATERIALS': self._buildMaterialsRichTextList(lessonPlan),
            'items' : activitiesAndProceduresLists
        }
        document.render(context)
        document.save(filename)

    def _buildObjectivesRichTextString(self, objectives):
        retVal = []
        for objective in objectives:
            retVal.append("~ " + objective.name)
        return R("\n".join(retVal), style="ObjectiveStyle")

    def _buildStandardsRichTextString(self, standards):
        rtRetVal = R()
        for standard in standards:
            if standard.metByLesson:
                rtRetVal.add(standard.label + " " + standard.name + "\n", bold=True, style="StandardStyle")
            else:
                rtRetVal.add(standard.label + " " + standard.name + "\n", style="StandardStyle")
        return rtRetVal

    def _buildMaterialsRichTextList(self, lessonPlan):
        retVal = []
        materials = set()
        for activity in lessonPlan.activities:
            for material in activity.materials:
                if material not in materials:
                    materials.add(material)
                    retVal.append(material)
        return R(", ".join(retVal))

    def _buildActivitiesAndProceduresRichTextLists(self, activitiesWithProcedures):
        retVal = []
        i=0

        for activityWithProcedures in activitiesWithProcedures:

            # get the related procedures depending on activity type
            if activityWithProcedures.type == ActivityType.INITIAL_ACTIVITY:
                relatedProcedures = activityWithProcedures.initial_procedures
            elif activityWithProcedures.type == ActivityType.MIDDLE_ACTIVITY:
                relatedProcedures = activityWithProcedures.middle_procedures
            elif activityWithProcedures.type == ActivityType.REVIEW_ACTIVITY:
                relatedProcedures = activityWithProcedures.review_procedures
            else:
                relatedProcedures = []

            # always add the name, bold if normal activity, italics if transition
            if activityWithProcedures.type == ActivityType.TRANSITION:
                retVal.append({"activity": R(activityWithProcedures.name, style="TransitionStyle"), "procedures": ""})
            else:
                retVal.append({"activity": R(activityWithProcedures.name, style="ActivityStyle"), "procedures": ""})

            #FIXME(quinton): add numbering to internal procedure list
            internalProcedureList = []
            for procedure in relatedProcedures:
                internalProcedureList.append(procedure)
            retVal[i]["procedures"] = R("\n".join(internalProcedureList), style="ProcedureStyle")
            i += 1

        return retVal

