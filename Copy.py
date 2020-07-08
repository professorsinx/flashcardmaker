import os
import shutil
src="/home/user/websites/RBI CA May/affairscloud.com"
#dest="/home/user/Documents/RBI 2020/Current Affairs/MAY"

#==============OPEN FILE CONTAINING LINKS TO INDEX.HTML===========
fileNumber =1
index_file_path = open("/home/user/Documents/RBI 2020/Current Affairs/MAY/index_file_paths","r")

with index_file_path as f:
    lines =[line.rstrip() for line in f]

for line in lines:
    print(line)
    filePath=""+line
    dest = "/home/user/Documents/RBI 2020/Current Affairs/MAY/index_files/index"+str(fileNumber)
    shutil.copy(filePath,dest)
    fileNumber=fileNumber+1
#==================================================================

## PROGRAM WORKS
# WHAT DOES IT DO ?
# IT COPIES THE FILES LISTED IN THE index_file_path TEXT FILE(WHERE SOURCE IS WRITTEN)
# IT PASTES IN A NEW FOLDER WITH NEW FILE NAME INDEXED.
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list