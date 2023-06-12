'''
This program downloads a specific folder from server,
checks for duplicates and send out automatic emails after download is done

'''

#! python3

# Used log debugging method
# Used Regular expressions for matching expressions
# Check for duplicates
# Send out download email
# Show complete percentage

# Current issues?
    # Compare the source and destination sizes
    

import pyperclip        # To be able to use copy and paste
import re               # To be able to use regular expressions for finding text or numbers
import shutil           # For copying, renaming folders
import logging          # To see the logs on the screen
import os               # To make the program OS independent and changing directories
import time             # To be able to use time to run the program few times a day automatically
import progressbar      # To be able to show the download progress
import smtplib          # To be able to send automatic emails
import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # To see the logs on the screen
logging.basicConfig(filename='DailyFolderDownloadLogs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # To store loggs in a file called DailyBildLogs

# *****************************************************     copy with progress bar function     ***********************************************


# **************************************************************************************************************************************************







RemoteDataBase = 'D:\\Source\\Directory\\Path'      # os.path.exists('\\Patch\To\Be\Verified')  # To check if a path already exist
LocalPath = 'D:\\Destination\\Local\\Path'
SoftwareToBeDownloaded = r'^Release_D_For_Example'     #Keyword to search for on source path

logging.info('Start of program.')

logging.debug('The path is: ' + RemoteDataBase)

# lOOP THE WHOLE PROGRAM FROM HERE

while True:


    logging.info('Check the current time.')
    currenTime = time.ctime()
    logging.debug(currenTime)

    #       Complete time format 2018-09-16 11:25:26,130
    currenTimeRegEx = re.compile(r'''^\w\w\w\s\w\w\w\s\d\d\s(
04:00|04:10|04:20|04:30|04:40|04:50|
05:00|05:10|05:20|05:30|05:40|05:50|
06:00|06:10|06:20|06:30|06:40|06:50|
07:00|07:10|07:20|07:30|07:40|07:50|
08:00|08:10|08:20|08:30|08:40|08:50|
09:00|09:10|09:20|09:30|09:40|09:50|
10:00|10:10|10:20|10:30|10:40|10:50|
11:00|11:10|11:20|11:30|11:40|11:50|
12:00|12:10|12:20|12:30|12:40|12:50|
13:00|13:10|13:20|13:30|13:40|13:50)''')
    isTheTimeRight = currenTimeRegEx.search(currenTime)
    logging.debug(isTheTimeRight)
    if (isTheTimeRight == None):
        print(currenTime)

    else:
        os.chdir(LocalPath)

        logging.debug('Current directory is: ')
        logging.debug(os.getcwd())


        logging.debug('Local list directory is: ')
        LocallistDirectory = os.listdir()

        SizeOfLocalPath = len(LocallistDirectory)

        for i in range (SizeOfLocalPath):
            logging.debug(LocallistDirectory[i])

        logging.debug('Size Of local Path is: ')
        logging.debug(SizeOfLocalPath)

                # os.walk('')         # To go throu a tree
        # os.walk('D:\\Directory\\To\\Go\\To')    
        os.chdir(RemoteDataBase)


        logging.debug('Current directory is: ')
        logging.debug(os.getcwd())


        logging.debug('DataBase list directory is: ')
        DataBaselistDirectory = os.listdir()


        SizeOfRemoteDataBase = len(DataBaselistDirectory)

        for i in range (SizeOfRemoteDataBase):
            logging.debug(DataBaselistDirectory[i])

        logging.debug('Size Of DataBase Path is: ')
        logging.debug(SizeOfRemoteDataBase)

        logging.info('CHECKING FOR NEW SW!')

        for i in range (SizeOfRemoteDataBase):
            logging.debug('Start of loop: ' + str(i))
            os.chdir(RemoteDataBase)
            logging.debug(os.getcwd())

            if DataBaselistDirectory[i] in LocallistDirectory:
                print(DataBaselistDirectory[i] + ' Is not a match!')
              

            else:
                logging.info('Adding the SW to be downloaded in here.')
                NewSWRegex = re.compile(SoftwareToBeDownloaded)
                result = NewSWRegex.search(DataBaselistDirectory[i])
                logging.debug(result)
                if (result == None):
                    continue
                logging.info('Found one!')

                logging.info('A SW is availble')
                logging.debug('Inside SW loops')
                logging.info('Adding the new SW to local list')
                os.walk(DataBaselistDirectory[i])
                logging.debug(DataBaselistDirectory[i])
                logging.debug(os.getcwd())

                logging.debug(os.getcwd())
  #              logging.debug(os.path.exists('D:\\Check\\If\\Local\\Path\\Already\\Exist)) # To check if a path already exist
                os.chdir(DataBaselistDirectory[i])
                try:
                    os.chdir('Folder where new data should be downloaded')
                    os.chdir('New Data')
                    logging.debug(os.getcwd())

                    SWPath = LocalPath + '\\' + DataBaselistDirectory[i] + '\\' + 'Folder where new data should be downloaded' + '\\' + 'New Data'
                    logging.debug(LocalPath)
                    logging.debug(SWPath)
                    print(SWPath)

                    shutil.copytree(os.getcwd(),SWPath)
                    logging.info(DataBaselistDirectory[i] + '***   SW has been copied to local path   ***')

                                                        # 5. Send out an email once the download is done
                    conn = smtplib.SMTP('smtpcg.gmail.com', 25)   # Creating a connection object stored in a variable named conn
                    conn.ehlo()             # Connecting to the server
                    conn.starttls()         # Starting tls encryption the connection
                    conn.login('dehno.kaveh', 'EmailPasswordHere')     # Logging in
                    Subject = 'Subject: [Automated Email Generation] ' + DataBaselistDirectory[i] + ' has been added to local path'
                    conn.sendmail('dehno.kaveh@gmail.com', 'dehno.kaveh@gmail.com', Subject)
                    conn.quit()             # Disconnecting from smtp server

                except FileNotFoundError:
                        print('Error: No new data are available at the moment.')

        # ******************************************************






        # To copy the whole tree use the following section
        # ******************************************************
        '''
                shutil.copytree(DataBaselistDirectory[i], 'New_SW')
                shutil.move('New_SW', LocalPath)
                os.chdir(LocalPath)
                shutil.move('New_SW', DataBaselistDirectory[i])

                logging.info(DataBaselistDirectory[i] + '***   SW has been copied to local path   ***')
        '''
        # ******************************************************



        LocallistDirectory = os.listdir()
        SizeOfLocalPath = len(LocallistDirectory)

        logging.debug('New local path:')
        logging.debug(SizeOfLocalPath)

        for i in range (SizeOfLocalPath):
            logging.debug(LocallistDirectory[i])
          




