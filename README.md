# schedule-generator
This is schedule generator for shift and set based employees


## What the project does
Schedule-generator is a program written on Python that generates schedule of shift-based employees and outputs .xlsx template ready to be uploaded to Microsoft Teams shifts plug-in. 

External libraries used:
* OpenPyXL
* SimplePyGUI

It coninsts of following .py files:
* sched-gen-gui.py
* functions.py
* schedule.py

#### sched-gen-gui.py
As the name of the file suggests it is a GUI file of a schedule-generator. It uses PySimpleGUI as a builder. It consists of a 4 input fields, calculate and exit buttons. 
![schedule-generator gui](https://user-images.githubusercontent.com/6499479/129482202-9ef2ab26-a474-4a07-98ad-1ed6038a4373.jpg)


2 out of 4 input fields take Excel file in, one of which should be .xlsx file that containt information about employees

![employees file - Excel](https://user-images.githubusercontent.com/6499479/129481895-3f9b8215-cd09-4404-82a4-79d33aff0fac.jpg)

