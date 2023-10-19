https://drive.google.com/file/d/1AN1_ogV7DrMxMMEdWf1HOMlxwH-fbyPm/view?usp=sharing

<p align="center"><img src="https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/teacherspet.png" alt="alt text" width=200 height=200>
  
  <h1 align="center"> Teacher's Pet </h1>
  
<h2 align="center"> Streamline Your Class Discord</h2>


[![DOI](https://zenodo.org/badge/429658277.svg)](https://zenodo.org/badge/latestdoi/429658277)
![Python](https://img.shields.io/badge/python-v3.7+-brightgreen.svg)
![GitHub](https://img.shields.io/github/license/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
![GitHub issues](https://img.shields.io/github/issues/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
![Lines of code](https://tokei.rs/b1/github/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
[![codecov](https://codecov.io/gh/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/branch/main/graph/badge.svg?token=QTKU51PZSO)](https://codecov.io/gh/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
[![GitHub Workflow Status](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/actions/workflows/test.yml/badge.svg)](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/actions/workflows/test.yml)

<!-- I am not sure about this parameter yet. Any idea what to do about this? -->
<!-- ![GitHub deployments](https://img.shields.io/github/deployments/Ashwinshankar98/TeachersPetBot/discord-bot-phase2)<br/> -->

## Contents
1. [ Description ](#desc)
2. [ New Features](#features)
3. [ Installation and Running ](#instrun)
4. [ Testing ](#testing)
5. [ Bot Commands ](#commands)
6. [ Future Scope ](#fscope)
7. [ Want to contribute? ](#contribute)
8. [ License ](#license)


<a name="desc"></a>
Click Below to Watch Our Video!

  

https://user-images.githubusercontent.com/60410421/143972105-f5aabb10-73e3-454a-96dc-9e9d0fe5b468.mp4


  
<h2>Software Engineering Project for CSC 510 : Phase III</h2>


Teacher's Pet is a Discord Bot for class instructors to streamline their Discord servers. Discord is a great tool for communication and its functionalities can be enhanced by bots and integrations. 

For 3.0, we created new tools for instructors and students to use to improve course communication. Some of our implemented features were partly suggested by iteration 2 such as regrade requests, project event, and live spam checking. We implemented other features we thought would be helpful such as email interactions, link saving, and data visualization. Our main objective for 3.0 was to add more organizational tools to make a course's discord channel more than just a messenger.

<hr />

<a name="features"></a>
<h2>Bot Features</h2>

<!-- Need to update this -->
[Click here to see the features of iterations I and II.](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/feature-history.md)

<!-- Need to update this -->
<h4>Charts</h4>
Instructors (like TAs, and Professors) can quickly make graphcs and charts directly in discord to share with students/users. Instructors can use this feature to share grade distributions, lecture participation/attendance, or other course statistics. All charts are named and stored into a json file when they are created. Students have acess to a command that allows them to view previously presented charts.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/charts.gif"></p>

<!-- Need to update this -->
<h4>Email Configuration</h4>

This feature enables users to configure their email address in the system to receive important notifications, attachments from professors, assignment reminders. Users can also update, view and unconfigure a configured email address through the system.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/email-address.gif"></p>

<!-- Need to update this -->
<h4>Email Interaction</h4>

This feature notifies all students regarding the next assignment deadline which is due for a day through email.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/email-reminder.gif"></p>

<!-- Need to update this -->
<h4>Re-Grading</h4>

This feature provides a way for students to submit regrade requests and Instructors can collect information of the requests submitted. There are various commands included to add, update, display and remove regrade requests.
This usecase was based on regrade request submission for CSE 510 SE FALL21 mid examination.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/Regrade.gif"></p>

<!-- Need to update this -->
<h4>Link Saving</h4>

This feature is helpful to save all the messages which contain important URLs. we have built a user command "!send_links"  This command lets users access all messages which contain URLs. The messages Containing URLs are automatically get appended in a file and the file is attached when the "!send_links" command is input.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/link-saving.gif"></p>

<!-- Need to update this -->
<h4>Project Event</h4>

This feature allows instructors or teaching assistants to create a project event by providing information such as description, link for project submission and deadline. The deadline reminder is taken care of Email Interaction feature.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/project-event.gif"></p>

<!-- Need to update this -->
<h4>Spam Detection</h4>
This feature is used to detect spam in message channels. When a user tries to send too many messages in the channel, it gives a warning. This is useful when multiple users are trying to send mutiple messages. The warning lets the student know that they have sent too many messages. 

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/Spam-Detection.gif"></p>

<hr />

<a name="instrun"></a>
<h2> Installation and Running </h2>

#### Tools and Libraries Used
In addition to the packages from [requirements.txt](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/requirements.txt) which need to be installed, please have the following installed on your machine:
<!-- Are there any changes here? -->
* [Python 3.9.7](https://www.python.org/downloads/)
* [Sqlite](https://www.sqlite.org/download.html)
<!-- Are there any changes here? -->
To install and run Teacher's Pet, follow instructions in the [Installation and Testing Guide](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/Installation.md).


<a name="testing"></a>
<!-- Are there any changes here? -->
<h2>Testing </h2>

To run tests on the Teacher's Pet, follow instructions in the [Installation and Testing Guide](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/Installation.md#Run-Tests).

<hr />
<!-- Are there any changes here? -->
<a name="commands"></a>
<h2> Bot Commands </h2>

<h3> Bot commands from iteration III </h3>


:open_file_folder: [!regrade-request command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!update-request command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!remove-request command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!display-requests command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!chart command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/charts/charts.md)

:open_file_folder: [!check_chart command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/charts/check_chart.md)

:open_file_folder: [!create_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/create_email.md)

:open_file_folder: [!view_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/view_email.md)

:open_file_folder: [!update_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/update_email.md)

:open_file_folder: [!remove_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/remove_email.md)

:open_file_folder: [!project_event command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/events/project_event.md)

<br>
<h3> Bot commands from iteration I and II </h3>

`!setInstructor <@member>` Set a server member to be an instructor (Instructor command)

`!removeInstructor <@member>` Remove a server member from the instructor role (Instructor command)

`!getInstructor` Get the current instructors in the server

`!attendance` Find attendance from voice channel (Instructor command)

`!ask "<question>"` Ask a question  

`!answer <question_number> "<answer>"` Answer a question

`!poll <command>` Run a poll for students (Instructor command)

`!create` Start creating an event (Instructor command) 

`!oh enter` Enter an office hour queue as an individual student  

`!oh enter <group_id>` Enter an office hour queue with a group of students  

`!oh exit` Exit the office hour queue  

`!oh next` Go to next student in queue as an instructor (Instructor command)

`!help` Gets the descriptions for all commands

`!help <command>` Describes a command in detail

`!ping` Find the latency of network

`!stats` Gets the statistics of system and softwares used

<hr />

<a name="fscope"></a>

<h2> Future Scope </h2>

This bot has endless possibilities for functionality. Features which we are interested in adding but did not have time for include but are not limited to:

  * Custom Events
  * Allow events to be edited
  * Show error information on discord
  * Make Instructor commands private
  * Add new roles
  * Track participation and user ranking
  * Refactor code to use cogs
  * Save data charts on DB rather than locally in json
  * Store data based on user emote reactions to instructor messages

For a detailed description of each of the above future enhancements listed visit [Future Scope](https://github.com/chandur626/TeachersPetBot/projects/2).

<hr />

<a name="contribute"></a>

<h2>How to Contribute? </h2>

Check out our [CONTRIBUTING.md](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/CONTRIBUTING.md) for instructions on contributing to this repo and helping enhance this Discord Bot, as well as our [Code of Conduct](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/CODE_OF_CONDUCT.md) guidelines.


<a name="license"></a>

<h2> License </h2>

The project is licensed under the [MIT License](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/LICENSE).

<hr />

<h3> Team Members </h3>

[Tanmay Pardeshi](https://github.com/tanmaypardeshi)

[Chandana Ray](https://github.com/cray94)

[Abhinav Sinha](https://github.com/abhinav110595)

[Sam Kwiatkowski-Martin](https://github.com/ExtremeMachine12)

<h3> Previous Authors </h3>


#### Sandesh Aladhalli Shivarudre Gowda
#### Chandatahas Reddy Mandapati
#### Sri Pallavi Damuluri
#### Niraj Lavani
#### Harini Bharata
#### Ashwin Shankar Umasankar
#### Itha Aswin
#### Kailash Singaravelu
#### Saikaushik Kalyanaraman
#### Shakthi Nandana Govindan

