#! /usr/bin/env python3

import os
import requests

INPUTFOLDER="/data/feedback"
CORPWEBIP="x.x.x.x"


url = "http://{}/feedback".format(CORPWEBIP)

#search text file in the folder
for textfile in os.listdir(INPUTFOLDER):

    #create full path of a text file
    textfilepath = os.path.join(INPUTFOLDER, textfile)

    #operate each file
    with open(textfilepath, "r") as f:
        #read text file
        title = f.readline()
        name = f.readline()
        date = f.readline()
        feedback = f.read()

        #create request data
        data = {
            "title":title
            ,"name":name
            ,"date":date
            ,"feedback":feedback
        }

        #throw request
        response = requests.post(url,json=data)

        #analyze response
        print("--response--")
        print("text: {} \nstatus_code: {} \ntext(response): {}".format(
            textfile, response.status_code, response.text))



