# FeedbackApp

# Introduction & Working:
- The user as they enter the home page will have a button to take them to the feedback button.
- Now in the feedback page, the user has to enter their name, their email address and the feedback message and enter submit, they have an option to submit the feedback. 
- The webpage displays success upon successful submission of feedback.
- The submission if the name is of inappropriate length (>100) or email is not valid. 
- The administration of the website can view these feedback along with the name, email address of the user in the database.

# Images:
- Home Page: </br>
![image](https://github.com/Aasrish/feedbackApp/assets/76608418/1494c2b3-919d-41ab-a605-6ba052272568)

- Feedback page: </br>
![image](https://github.com/Aasrish/feedbackApp/assets/76608418/5c5a76fb-757e-4375-9dd8-fcf8c141a35b)

- Failed Feedback: </br>
![image](https://github.com/Aasrish/feedbackApp/assets/76608418/fb455a14-c017-48a5-91d0-4a44ecd92949)

- Successful Feedback: </br>
![image](https://github.com/Aasrish/feedbackApp/assets/76608418/aedf9678-c3b1-49a0-af0c-1fb8ea21cb87)

- Admin View: </br>
![image](https://github.com/Aasrish/feedbackApp/assets/76608418/1d6e3ce7-323a-4939-ad44-ed4949e52bcb)
![image](https://github.com/Aasrish/feedbackApp/assets/76608418/0b891220-4791-4be8-8592-b2ba877c094b)

# How to run?
- To run this program on your computer, download all the files and then, open the command prompt as an administrator. And enter the program directory.
- Enter the following command and run:
```
python3 manage.py createsuperuser
```
- Now enter the details as per your wish, these details will serve as admin credentials to look at the feedback.
- Run the following command to create the database.
```
python3 manage.py migrate
```
- Now run the following command:
```
python3 manage.py runserver
```
- The server is running! 
# Stack:
- Programming Language: Python and Django for BackEnd and HTML CSS and Javascript for the Front End

