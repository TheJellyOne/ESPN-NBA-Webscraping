#Data-Science-Project-Group

#Instructions to set-up github
#Download Bash "https://git-for-windows.github.io":


#STEP 1)THIS PART WILL LET YOU ACCESS AND MAKE CHANGES TO THE REPOSITORY

#Open Git Bash

#Setting up SSH Key

>ssh-keygen -t rsa

#enter password

>clip < ~/.ssh/id_rsa.pub   

#Copies password to clipboard

#go to github account settings and enter SSH, will give you ability to push changes

#Using Github
#Get to directory you want files

>cd desktop

#Clone the repository

>git clone https://github.com/TheJellyOne/Data-Science-Project-Group


#STEP 2)BASIC COMMANDS, DOWNLOAD AND UPLOAD CHANGES
#Go into Data-Science-Project-Group folder

>cd Data-Science-Project-Group

#Create a newFile

>touch randomFileName.txt

#Update Data-Science-Project-Group folder

>git pull

#After changing files in Data-Science-Project-Group, upload onto github

>git add changedFileInFolder   

#or use "git add ." to add all changes 

>git commit -m "anyRandomComments"

>git push origin master
