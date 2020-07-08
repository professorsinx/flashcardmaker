#SCRAPE ALL .HTML FILES TO GET THE QUESTIONS OPTIONS 
#
#  "QUESTION WITH OPTIONS FORMATTED(keep the formatting)","ANSWER"
#   
#   MAKE A CSV FILE -- ITERATE THROUGH ALL .HTML FILES
#
#
#==================================================================

from bs4 import BeautifulSoup
import csv
import fnmatch
import os
import re

'''     #*************_____ MATCHES ALL FILES WHOSE NAME STARTS WITH i _______*********# (reuse for looping through the html files)
for filename in os.listdir("/home/user/Documents/RBI 2020/Current Affairs/JUNE/index_files"): 
        if fnmatch.fnmatch(filename,'i*'):
            print(filename)
'''
#----------VARIABLE DEFINITIONS--------------
deck_name="june.csv"
working_directory = "/home/user/Documents/RBI 2020/Current Affairs/JUNE/index_files" 
#-------------------------------------------
for filename in os.listdir(working_directory): 
        if fnmatch.fnmatch(filename,'i*'):
            print(filename)
            html=open(working_directory+"/"+filename).read()
            soup = BeautifulSoup(html,"html5lib") 
            question_list = soup.find_all('ol')
            current_affairs_questions = question_list[0]
            static_questions=question_list[1]
            # ADD ENTRIES TO THE CSV FILE HERE

            for tag in current_affairs_questions.find_all('li'):
                question_text = str(tag)
                curr_ques=question_text.split("<div>")[0]
                curr_ans=question_text.split("Answer")[2] 
                with open(deck_name,'a',newline='') as csvfile:      #Opening a file with the 'a' parameter allows you to append to the end of the file instead of simply overwriting the existing content
                    fieldnames = ['question','answer']
                    writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
                    writer.writerow({'question':curr_ques, 'answer':curr_ans})

            for tag in static_questions.find_all('li'):
                question_text = str(tag)
                curr_ques=question_text.split("<div>")[0]
                curr_ans=question_text.split("Answer")[2] 
                with open(deck_name,'a',newline='') as csvfile:
                    fieldnames = ['question','answer']
                    writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
                    writer.writerow({'question':curr_ques, 'answer':curr_ans})   
        continue 

print("PROGRAM RAN 100%")