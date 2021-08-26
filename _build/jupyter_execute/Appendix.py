#!/usr/bin/env python
# coding: utf-8

# (Appendix)=
# # Appendix

# ## Goals for improving this portfolio
# Here are unsorted thoughts from the author of things to do to improve this document in the future.
# 
# ### Sliders for grade checks
# Below is a tool that uses ipywidgets to create slide values. The goal is to provide students with the ability to come to a webpage and use the sliders to determine their class grade. The only issue is that one must make the html page run python. 
# 
# This slider feature works in Jupyterlab but not in the HTML document. This is an active area of development for Jupyterbook. Current solutions are 
# - [MyBinder](https://mybinder.org/)
# - [Thebe](https://github.com/executablebooks/thebe)
# - Remake tool in javascript and natively run in html (must be hosted on another site and embedded as an Iframe)

# In[1]:


import ipywidgets as widgets

test1=widgets.FloatSlider(
    value=100,
    min=0,
    max=100,
    step=.01,
    description='Test 1:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f'
)
test2=widgets.FloatSlider(
    value=100,
    min=0,
    max=100,
    step=.01,
    description='Test 2:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f'
)
test3=widgets.FloatSlider(
    value=100,
    min=0,
    max=100,
    step=.01,
    description='Test 3:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f'
)
Lab=widgets.FloatSlider(
    value=100,
    min=0,
    max=100,
    step=.01,
    description='Lab:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f'
)
Participation=widgets.FloatSlider(
    value=100,
    min=0,
    max=100,
    step=.01,
    description='Participation:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f'
)
Homework=widgets.FloatSlider(
    value=100,
    min=0,
    max=100,
    step=.01,
    description='Homework:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f'
)
FinalExam=widgets.FloatSlider(
    value=100,
    min=0,
    max=100,
    step=.01,
    description='Final Exam:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f'
)

CourseGrade=widgets.Text(
    value='%.2f'%100,
    placeholder='Type something',
    description='Grade:',
    disabled=True
)

def on_value_change(change):
    CourseGrade.value='%.2f'%(
        .15*Lab.get_interact_value()+
        .10*Participation.get_interact_value()+
        .10*Homework.get_interact_value()+
        .20*(np.sum([test1.get_interact_value(),
                    test2.get_interact_value(),
                    test3.get_interact_value()
                    ]
                )-
            np.min([test1.get_interact_value(),
                    test2.get_interact_value(),
                    test3.get_interact_value()
                    ]
                  )
            )
            +
        .25*FinalExam.get_interact_value()
    )
    
Lab.observe(on_value_change)
Participation.observe(on_value_change)
Homework.observe(on_value_change)
test1.observe(on_value_change)
test2.observe(on_value_change)
test3.observe(on_value_change)
FinalExam.observe(on_value_change)

left_box = widgets.VBox([Lab,Participation,Homework,test1,test2,test3,FinalExam])
right_box = widgets.VBox([CourseGrade])
widgets.VBox([left_box, right_box])

