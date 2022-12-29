# import time
import csv
# datetime is used for checking chedule related and 10AM to 5PM related logic
from datetime import datetime
import re
# import requests  # unable to find working key for your API
# Assumptions:
#    USA and India are the only 2 countries in the csv File
#    sending same messages again is the users choice and no duplicate messages will be created by the Code
#    I have made Some Changes in Sample.csv to add more test cases plese refer to it first

# OOD of the problem statement
# class Messaging encapsulates the whole logic with every data member private so that no one else can change there values 
class Messaging:
    def __init__(self,file,ans_file):
        self.__Message=""
        self.__email=""
        self.__Phone=0
        self.__country=""
        self.__schedule=None
        self.__file=file
        self.__now=datetime.now()
        self.__source=ans_file
        self.__regx=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    def read(self):
        File=open(self.__file,'r')
        File2=open(self.__source,"a")
        for i in csv.DictReader(File):
            self.__Message=i[list(i.keys())[0]]
            self.__email=i["Email"]
            self.__Phone=i["Phone"]
            self.__country=i["Country"]
            self.__schedule=i["Schedule On"]
            if self.__country=="USA":
                if self.__schedule ==None:
                    if self.email_chk():
                        File2.write("Failed to sent email: Invalid email address\n")
                    else:
                        File2.write("Success: email sent on "+self.__now.strftime("%H hr-%M min-%S sec")+"\n")
                    if self.phone_chk():
                        File2.write("Failed: wrong phone number\n")
                    elif int(self.__now.strftime("%H")) > 3 or (int(self.__now.strftime("%H"))==3 and int(self.__now.strftime("%M"))>30):
                        File2.write("Failed: it is not day time in "+self.__country+"\n")
                    elif int(self.__now.strftime("%H")) <20 or (int(self.__now.strftime("%H"))==20 and int(self.__now.strftime("%M"))<30):
                        File2.write("Failed: It is not day time in "+self.__country+"\n")
                    elif self.chk_message_leng():
                        File2.write("Failed: message length in not in correct range 1-160 excluding 1\n")
                    else:
                        File2.write("Success: "+self.__Message+" sent on "+self.__Phone+" on "+self.__now.strftime("%H-%M-%S"))
                else:
                    if self.email_chk():
                        File2.write("Failed to sent email: Invalid email address\n")
                    elif self.chk_schedule():
                        File2.write("Failed: Scheduled Email date is of a past date\n")
                    else:
                        File2.write("Success: Email:- "+self.__Message+" scheduled to be sent on "+self.__schedule+"\n")
                    if self.phone_chk():
                        File2.write("Failed: wrong phone number\n")
                    elif self.chk_message_leng():
                        File2.write("Failed: message length in not in correct range 1-160 excluding 1\n")
                    elif self.chk_schedule():
                        File2.write("Failed: Scheduled Message date is of a past date\n")
                    else:
                        File2.write("Success: "+self.__Message+" is scheduled to be sent on "+self.__schedule+" on phone-"+self.__Phone+"\n")
            else:
                if self.__schedule==None:
                    if self.email_chk():
                        File2.write("Failed to sent email: Invalid email address\n")
                    else:
                        File2.write("Success: email sent on "+self.__now.strftime("%H hr-%M min-%S sec")+"\n")
                    if self.phone_chk():
                        File2.write("Failed: wrong phone number\n")
                    elif int(self.__now.strftime("%H")) > 17 or (int(self.__now.strftime("%H"))==17 and int(self.__now.strftime("%M"))>30):
                        File2.write("Failed: it is not day time in "+self.__country+"\n")
                    elif int(self.__now.strftime("%H")) <10 or (int(self.__now.strftime("%H"))==10 and int(self.__now.strftime("%M"))<30):
                        File2.write("Failed: It is not day time in "+self.__country+"\n")
                    elif self.chk():
                        File2.write("Failed: message length in not in correct range 1-160 excluding 1\n")
                    else:
                        File2.write("Success: "+self.__Message+" sent on "+self.__Phone+" on "+self.__now.strftime("%H-%M-%S"))
                else:
                    if self.email_chk():
                        File2.write("Failed to sent email: Invalid email address\n")
                    elif self.chk_schedule():
                        File2.write("Failed: Scheduled Email date is of a past date\n")
                    else:
                        File2.write("Success: Email:- "+self.__Message+" scheduled to be sent on "+self.__schedule+"\n")
                    if self.phone_chk():
                        File2.write("Failed: wrong phone number\n")
                    elif self.chk_message_leng():
                        File2.write("Failed: message length in not in correct range 1-160 excluding 1\n")
                    elif self.chk_schedule():
                        File2.write("Failed: Scheduled Message date is of a past date\n")
                    else:
                        File2.write("Success: "+self.__Message+" is scheduled to be sent on "+self.__schedule+" on phone-"+self.__Phone+"\n")
        File.close()
        File2.close()

    # below function verifies for the valid email address
    def email_chk(self):
        if(re.fullmatch(self.__regx, self.__email)):
            return False
        return True
    # Below function checks if the entered scheduled date is valid or not i.e not from a past date
    def chk_schedule(self):
        d,m,y=list(map(int,self.__schedule.split('/')))
        if d<int(self.__now.strftime("%d")) and m==int(self.__now.strftime("%m")) and y==int(self.__now.strftime("%y")):
            return True
        elif m<int(self.__now.strftime("%m")) and y==int(self.__now.strftime("%y")):
            return True
        elif y<int(self.__now.strftime("%y")):
            return True
        return False
    # Below function checks for the valid length of message to be sent i.e from 1-160 with 1 excluded
    def chk_message_leng(self):
        n=len(self.__Message)
        if n<=1 or n>160:
            return True
        return False
    # checks for the phone numbe and veifies it length and numerical value
    def phone_chk(self):
        if len(self.__Phone)!=10:
            return True
        for i in self.__Phone:
            if ord(i)<ord('0') or ord(i)>ord('9'):
                return True
        return False

# simply create object of class Messaging and use read function to go through input file to generate result 
obj=Messaging("Sample.csv","solution.txt")
obj.read()
# It is to be noted that i tried using SMS Magic API but was unable to find working key
# It shower Forbidden-key error every time