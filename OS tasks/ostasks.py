#!/usr/bin/python3

import os

userlist = ["alpha", "beta", "gamma"]

print("######################################")
print("Adding users to system...")
print("######################################")

for user in userlist:
    ec = os.system(f"id {user}")
    if ec == 0:
        print(f"User {user} already exists.")
    else:
        ec = os.system(f"useradd {user}")
        if ec == 0:
            print(f"User {user} added successfully.")
            print("")
        else:
            print(f"Failed to add user {user}.")
            print("")
    print("######################################")           

print("")
print("All users processed.")
print("")

print("")


# add groupname science

exitcode = os.system("grep science /etc/group")
if exitcode == 0:
    print("Group 'science' already exists.")
else:
    exitcode = os.system("groupadd science")
    if exitcode == 0:
        print("Group 'science' added successfully.")
    else:
        print("Failed to add group 'science'.")
        
print("")

# add users to group science

for user in userlist:
    ec = os.system(f"usermod -aG science {user}")
    if ec == 0:
        print(f"User {user} added to group 'science' successfully.")
    else:
        print(f"Failed to add user {user} to group 'science'.")
        
print("")

# add directory /ops/science_dir and give ownership to group science
print("########### creating directory ###############")
dir_path = "/ops/science_dir"
if(os.path.isdir(dir_path)):
    print(f"Directory {dir_path} already exists.")
else:
    os.mkdir(dir_path)
    print(f"Directory {dir_path} created successfully.")
print("")    

# change ownership of directory to group science
print("########### changing ownership and permissions ###############")
os.system(f"chown :science {dir_path}")
os.system(f"chmod 770 {dir_path}")
print(f"Ownership of {dir_path} changed to group 'science' with permissions 770.")
print("")

    


'''
# removing users 

print("######################################")
print("Removing users from system...")
print("######################################")

for user in userlist:
    ec = os.system(f"userdel {user}")
    if ec == 0:
        print(f"User {user} removed successfully.")
        print("")
    else:
        print(f"Failed to remove user {user}.")
        print("")
    print("######################################")
        
print("")
print("All users removed.")
print("")
'''

'''

# remove groupname science
exitcode = os.system("grep science /etc/group")
if exitcode == 0:
    exitcode = os.system("groupdel science")
    if exitcode == 0:
        print("Group 'science' removed successfully.")
    else:
        print("Failed to remove group 'science'.")
else:
    print("Group 'science' does not exist.")
    
print("")

'''
