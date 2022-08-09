#! /bin/bash

#Function is ask for username, password and groupname
adduser(){

    #Input Username   
    echo "Enter username to add:"
    read name

    #Input Password for user
    echo "Enter password for user:"
    read password

    #Input groupname to add user in
    echo "Enter groupname you want to add user to:"
    read groupname

    #Adding new user
    useradd $name

    #Checking if group exist
    if grep -q $groupname /etc/group
    then
        #If exist add user to the group
        echo "Adding to existing group"
        usermod -aG $groupname $name
    else
        #If does not exist, create group and add user
        echo "New group Created"
        groupadd $groupname
        usermod -aG $groupname $name
    fi
}

#Creating flag for loop
flag='y'

#Loop to ask for new user while condition is met
while [ $flag = 'y' ]
do
    adduser
    echo "Do you want to add another user: y or n?"
    read flag
done



