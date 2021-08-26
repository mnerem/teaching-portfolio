#!/usr/bin/env python
# coding: utf-8

# (2018-Spring-PHYS112-SOS)=
# # Student Opinion Surveys
# 
# # PHYS112 (2018-Spring)

# ## SOS for CRN 20136 (TR Lectures)

# In[1]:


import pandas as pd
sos=pd.read_excel('../../../../Student-Opinion-Surveys/201720-PHYS112-20136-SOS.xlsx',sheet_name='sos')
sosmdtable=sos.to_markdown(index=False)
print(sosmdtable)


# | Topic      |   -- | Questions                                                                                                                                                                   |   1 |   2 |   3 |   4 |   5 |   NA |   N |   NR |   Mean |   Instructor Mean |
# |:-----------|-----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|----:|----:|----:|----:|-----:|----:|-----:|-------:|------------------:|
# | Course     |    1 | The course materials, exams, projects and/or papers in this class required me to think critically.                                                                          |   1 |   1 |   0 |   6 |   9 |    0 |  17 |    0 |   4.24 |              4.02 |
# | Course     |    2 | In order to get good grades on tests and assignments, I had to know the course materials outlined in the syllabus and discussed in class.                                   |   1 |   1 |   0 |   4 |  11 |    0 |  17 |    0 |   4.35 |              4.26 |
# | Course     |    3 | Overall, I have learned or benefited from this class.                                                                                                                       |   2 |   4 |   0 |   5 |   6 |    0 |  17 |    0 |   3.53 |              3.73 |
# | Instructor |    4 | In the first week of class, the instructor provided documents and information that clearly explained the course content, assignments, grading and other important policies. |   0 |   1 |   1 |   9 |   6 |    0 |  17 |    0 |   4.18 |              4.28 |
# | Instructor |    5 | The instructor welcomed questions and other class participation.                                                                                                            |   1 |   0 |   1 |   7 |   8 |    0 |  17 |    0 |   4.24 |              4.45 |
# | Instructor |    6 | The instructor was enthusiastic with respect to the subject matter.                                                                                                         |   0 |   0 |   0 |   5 |  12 |    0 |  17 |    0 |   4.71 |              4.62 |
# | Instructor |    7 | The instructor was available for consultation and helpful.                                                                                                                  |   0 |   0 |   1 |   8 |   7 |    1 |  17 |    0 |   4.38 |              4.18 |
# | Instructor |    8 | The instructor used the full time period allotted for the class.                                                                                                            |   0 |   0 |   0 |   7 |  10 |    0 |  17 |    0 |   4.59 |              4.56 |
# | Instructor |    9 | The instructor's presentations were informative.                                                                                                                            |   0 |   1 |   3 |   7 |   6 |    0 |  17 |    0 |   4.06 |              4.09 |
# | Instructor |   10 | Overall, the instructor is an effective teacher.                                                                                                                            |   0 |   2 |   3 |   7 |   5 |    0 |  17 |    0 |   3.88 |              3.86 |

# ### Essay Responses

# In[2]:


essay=pd.read_excel('../../../../Student-Opinion-Surveys/201720-PHYS112-20136-SOS.xlsx',sheet_name='Essay-Responses')

QUESTIONS = [
    'What changes, if any, could be made to the class that would have helped you to learn more? What could the instructor have done to make the course an even better learning experience?',
    'What could you have done to make the course an even better learning experience?',
    'What did you like most about the class and your instructor?',
    'What factors about this class contributed the most to your learning? What aspects of this class helped you to learn to think critically?',
    'What factors about your own performance helped you learn the most? What did you do to facilitate your learning?',
]

first_toggle=True
for response in essay['Essay Questions:'].tolist():
    if response in QUESTIONS:
        if first_toggle:
            first_toggle=False
        else:
            print('\n```\n')
        print('**'+response+'**')
        print('\n```{toggle}')
    else:
        print('* '+response)
    
print('\n```{toggle}')


# **What changes, if any, could be made to the class that would have helped you to learn more? What could the instructor have done to make the course an even better learning experience?**
# 
# ```{toggle}
# * Honestly, I just wasn't interested in this course. I don't understand why I am required to take two semesters of physics. 
# * I cant think of any changes to improve the course.
# * I would have reduced the confusion of some of the homework assignments. 
# * made the homework more like the exams or the exams more like the homework. they aren't compatible with each other
# * Mastering physics is semi-effective at helping prepare for tests. I wish there was more guidance throughout the homework since sometimes it feels as if the homework is a test, and not practicing the steps of completing a physics problem. 
# * More practice problems during lecture
# * SLOW DOWN, the instructor seemed to rush through alot of material so it was sometimes hard to follow along or understand because we moved at such a high speed. 
# * Sometimes it was hard to follow along with really long examples on the chalk board.  Maybe organize these examples better, or find another medium to present them on.  Maybe chalk board isn't the best place to write out super long problems.
# * The instructor needs to take more time to explain the material & not rush through it. He's all over the place when teaching
# 
# ```
# 
# **What could you have done to make the course an even better learning experience?**
# 
# ```{toggle}
# * allow students to create their own formula sheets or at least include units on the provided formula sheet
# * Gone over the powerpoints again after class and stayed ahead with the reading.
# * I could have actually studied. 
# * I could have attended all of the classes, and taken more extensive notes.
# * I could have spend more time with the material and also utilized going to office hours for help. 
# * I could have taken better notes during lecture
# * If I did practice problems in the textbook, I may have understood the content just a little better.
# * studied more
# * Studied more. 
# 
# ```
# 
# **What did you like most about the class and your instructor?**
# 
# ```{toggle}
# * He obviously loves the subject 
# * He was enthusiastic and welcomed all questions
# * his involvement
# * How helpful the professor was if you needed it.
# * My instructor was very nice and approachable.  I was never scared to ask a question when I was confused.  My instructor also presents visual representations of the topics, such as using parallel and series circuits to show differences in light to the lightbulbs connected to the circuit.  Visual representations helped me better understand the topics.
# * The enthusiasm of the taught material. This professor was a step above others here as he explained physics with demonstrations and other real world applications. Lectures were interesting and informative. 
# * The instructor was very engaging, with multiple demonstrations to help better understand the material.
# * The instructor was very enthusiastic about what he was teaching with alot of visual examples in lecture that helped me stay focused and interested during the class. 
# 
# ```
# 
# **What factors about this class contributed the most to your learning? What aspects of this class helped you to learn to think critically?**
# 
# ```{toggle}
# * Homework
# * its interesting
# * Taking detailed notes, doing all the homework, and reviewing lecture slides most helped me think critically and learn the material. 
# * The demonstrations and workin problem after problem out in class
# * The homework's and tests required me to think critically.
# * The mastering physics homework, the examples helped with the tests and being able to connect concepts. 
# * The material in class was presented in a clear and concise manner on how it related to the course direction.
# * The PowerPoints, the examples done in class, some of the homework, and review sessions for tests.
# 
# ```
# 
# **What factors about your own performance helped you learn the most? What did you do to facilitate your learning?**
# 
# ```{toggle}
# * Going to class, forcing yourself to focus and take notes. It's almost impossible not to kindof understand the material after fully listening to it. I probably would have done better if I went over the powerpoints again after class.
# * I did all homework and attended most lectures. I also did all practice tests and reviewed the material constantly. 
# * I really tried to look over the chapter summaries and use all of my resources when it came to trying to do well in the course. Again redoing homework problems also helped alot. 
# * Looking over practice problems and always coming to class helped me learn the best.
# * my interest in the subject
# * Paying attention in class and taking notes
# * Taking my time through the homework helped me the most.
# * The homework and the lab portion. 
# 
# ```{toggle}

# ## SOS for CRN 22895 (MWF Lectures)

# In[3]:


sos=pd.read_excel('../../../../Student-Opinion-Surveys/201720-PHYS112-22895-SOS.xlsx',sheet_name='sos')
sosmdtable=sos.to_markdown(index=False)
print(sosmdtable)


# | Topic      |   -- | Questions                                                                                                                                                                   |   1 |   2 |   3 |   4 |   5 |   NA |   N |   NR |   Mean |   Instructor Mean |
# |:-----------|-----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|----:|----:|----:|----:|-----:|----:|-----:|-------:|------------------:|
# | Course     |    1 | The course materials, exams, projects and/or papers in this class required me to think critically.                                                                          |   0 |   0 |   1 |   2 |   4 |    0 |   7 |    0 |   4.43 |              4.02 |
# | Course     |    2 | In order to get good grades on tests and assignments, I had to know the course materials outlined in the syllabus and discussed in class.                                   |   0 |   0 |   0 |   2 |   5 |    0 |   7 |    0 |   4.71 |              4.26 |
# | Course     |    3 | Overall, I have learned or benefited from this class.                                                                                                                       |   0 |   0 |   1 |   0 |   6 |    0 |   7 |    0 |   4.71 |              3.73 |
# | Instructor |    4 | In the first week of class, the instructor provided documents and information that clearly explained the course content, assignments, grading and other important policies. |   0 |   0 |   0 |   1 |   6 |    0 |   7 |    0 |   4.86 |              4.28 |
# | Instructor |    5 | The instructor welcomed questions and other class participation.                                                                                                            |   0 |   0 |   0 |   1 |   6 |    0 |   7 |    0 |   4.86 |              4.45 |
# | Instructor |    6 | The instructor was enthusiastic with respect to the subject matter.                                                                                                         |   0 |   0 |   0 |   0 |   7 |    0 |   7 |    0 |   5    |              4.62 |
# | Instructor |    7 | The instructor was available for consultation and helpful.                                                                                                                  |   0 |   0 |   0 |   1 |   6 |    0 |   7 |    0 |   4.86 |              4.18 |
# | Instructor |    8 | The instructor used the full time period allotted for the class.                                                                                                            |   0 |   0 |   0 |   1 |   6 |    0 |   7 |    0 |   4.86 |              4.56 |
# | Instructor |    9 | The instructor's presentations were informative.                                                                                                                            |   0 |   0 |   1 |   1 |   5 |    0 |   7 |    0 |   4.57 |              4.09 |
# | Instructor |   10 | Overall, the instructor is an effective teacher.                                                                                                                            |   0 |   0 |   0 |   2 |   5 |    0 |   7 |    0 |   4.71 |              3.86 |

# ### Essay Responses

# In[4]:


essay=pd.read_excel('../../../../Student-Opinion-Surveys/201720-PHYS112-22895-SOS.xlsx',sheet_name='Essay-Responses')

QUESTIONS = [
    'What changes, if any, could be made to the class that would have helped you to learn more? What could the instructor have done to make the course an even better learning experience?',
    'What could you have done to make the course an even better learning experience?',
    'What did you like most about the class and your instructor?',
    'What factors about this class contributed the most to your learning? What aspects of this class helped you to learn to think critically?',
    'What factors about your own performance helped you learn the most? What did you do to facilitate your learning?',
]

first_toggle=True
for response in essay['Essay Questions:'].tolist():
    if response in QUESTIONS:
        if first_toggle:
            first_toggle=False
        else:
            print('\n```\n')
        print('**'+response+'**')
        print('\n```{toggle}')
    else:
        print('* '+response)
    
print('\n```{toggle}')


# **What changes, if any, could be made to the class that would have helped you to learn more? What could the instructor have done to make the course an even better learning experience?**
# 
# ```{toggle}
# * None
# * nothing
# * The equations to be more like the homework since some of the questions on the homework were a bit more challenging. Also Professor Nerem knows that some questions on the homework, answer wise were wrong but he was more than willing to help with the situation.
# 
# ```
# 
# **What could you have done to make the course an even better learning experience?**
# 
# ```{toggle}
# * I could have done more of the homework and been more attentive.
# * I guess not despise the subject of physics.
# * None
# * Probably more attention to what he says and explains rather than just writing lots of notes.
# 
# ```
# 
# **What did you like most about the class and your instructor?**
# 
# ```{toggle}
# * I like my instructor be because he took the time to help me learn the material. he had demos to actually show the concepts of what we would be learning.  Physics on the other hand isn't my thing so I am not too fond of the class it self.
# * I liked that he was helpful in and out of lecture.
# * My professor was enthusiastic about teaching physics.
# * Professor Nerem is very enthusiastic about physics and gives many examples and demonstrations so that we understand the practical applications.
# 
# ```
# 
# **What factors about this class contributed the most to your learning? What aspects of this class helped you to learn to think critically?**
# 
# ```{toggle}
# * The clicker questions
# * The equations done in class helped the most.
# * The homework and in-class reviews helped practice the content.
# * the homework and test contributed to me learning the most and helped me to think critically.
# 
# ```
# 
# **What factors about your own performance helped you learn the most? What did you do to facilitate your learning?**
# 
# ```{toggle}
# * I did most of the homework and followed along in class.
# * the help center and my professors offices hours
# * The masteringphysics homework made me critically think about the topics we learned in lecture.
# 
# ```{toggle}
