# Lesson Plan Generator

Developed by qwoodmansee, currently in very early stages.

## Summary
Tool to generate lesson plans based on a variety of inputs


### Basic Instructions
To export lesson plans, a valid instance of the LessonPlan class must be
created. An crude example can be seen in the Test/TestLessonPlan.py
file.

After an instance of the class is created, a Writer and Template should
be created. A template is a .docx file which uses {{}} syntax to relay
variables to the code, which code fills in using strings stored in the
LessonPlan instance.

#### Templates can be created using the following strategy:
    
    - Open a word doc with an existing lesson plan, or create one.
    
    - Any variables which are included in the Lesson Plan can be replaced
        in your word document. For example, a list of materials can be
        replaced with the tag {{ MATERIALS}}
    - If you would like custom (not the default for your document) styling:
        - Highlight the text you are replacing (e.g. list of materials)
        - Click Home -> Styles -> New Style
        - CHANGE THE TYPE TO "CHARACTER STYLE"
        - Name the style something which makes sense (e.g. MaterialStyle)
        - Change the tag in your Word Document to {{r MATERIALS}}
            - note the addition of the "r"

#### Lesson Plan Writers can be written by doing the following:

    - Create a valid implementation of the LessonPlanWriter base class
    - Use the doxctpl library to read in the template.docx file from above
    - Create a context Dictionary which maps each variable in the
        template to a string (or R() if applicable)
    - If custom styling is desired (very common):
        - Instead of just using a string in your writer's context variable,
            use R(string, style="styleName"), where styleName is the
            name of the style created by the document creator


#### Gotcha's:

    - When creating styles, if the user accidentally creates a "Paragraph
        Style", it won't be applied correctly when using the "style=" tag.
