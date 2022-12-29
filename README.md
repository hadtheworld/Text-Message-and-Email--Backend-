# Text-Message-and-Email--Backend-
This project is bakend program for messaging and email coded in Python Language. This allows the message to be sent in specified time slot only (10AM -5 PM). Email sent to verified mail id only.

This has Object oriented Design which encapsulated all related function in single class
  - only object of that class is needed to be clreated to run this code
  - read() function is called from the object of class which has file handling logic
  - Sample.csv is the input file to read the command from
  - output is stored in solutions.txt file

Working:
   - It read from input .csv file in form of dictionary using csv.DictRead() function
   - Applyes following conditions to determine if the message is ssent successfuly or not:
   -    A Message can be sent either as Email, Text Message or both.
   -    Message length should be > 1 and <=160 characters if it has to be sent as a Text Message.
   -    Phone number should be integer & length should be 10.
   -    Email can be sent only to a Valid email address.
   -    Text Messages can be sent only during the day (10AM to 5PM) in respective time zone
   -    Sending Email will not have time Restrictions.
   -    Duplicate messages should not be sent.
   -    Assume only 2 countries in the country field as USA or INDIA.
   -    Schedule messages for future date, if date is added in Schedule On column, if not then send a message immediately.
   -    Success or Failure needs to be written to a text file with the reason for Failed Message.
Memeber Functions:
   - read(self):
   -      Reads the input from .csv file and type in output file .txt based on abvove conditions
   - email_chk(self):
   -      Checks if the Email is valid or not
   - chk_schedule(self):
   -      Checks if the scheduled date is of past or not. If the date is of past it cannot be sent.
   - chk_message_leng(self):
   -      Checks if the message is in valid length or not 1-160 with 1 excluded
   - phone_chk(self):
   -      Checks if the phone number is of lenth 10 and is a numerical value
Every data members are Private in class and cannot be modified by the object of the class to apply data hiding and protection.

**API Integration:**
  - I have integrated the API of SMS Magic along with it
  -  API Endpoint being- https://api.txtbox.in/v1/sms/send
  -  API call is of "POST" Type which sends the sucessful message to user through API
