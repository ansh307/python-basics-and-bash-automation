print("This IT orginization has various skill sets")
print("Find out your matching skill set")

print("Enter Captalised value : ")

# Devops list
devops_list = ["Dev", "Ops", "Python", "Docker", "Kubernetes"]
# development tuple
development_tuple = ("nodejs", "reactjs", "python", "java", "golang", "vuejs")
cntr_emp1 = {"Name": "John", "Age": 30, "skill": "Blockchain"}
cntr_emp2 = {"Name": "Alice", "Age": 28, "skill": "AI"}

usr_skill = input("Enter your skill: ")

# check if the skill is in devops_list
if usr_skill in devops_list:
    print(f"{usr_skill} is a DevOps skill.")
elif usr_skill in development_tuple:
    print(f"{usr_skill} is a Development skill.")
    
elif (usr_skill == cntr_emp1["skill"] or usr_skill == cntr_emp2["skill"]):
    print(f"{usr_skill} is a skill of one of the employees.")
else:
    print(f"{usr_skill} Skill not found")