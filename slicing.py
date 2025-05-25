# slicing

planet1 = "closest to sun"
print(planet1)

print(planet1[0])
print(planet1[1])

print(planet1[-1])
print(planet1[-2])

print(planet1[0:1]) 
print(planet1[0:2])  


print(planet1[0:7])  
print(planet1[8:11])  

print(planet1[0:])  
print(planet1[:7])  

print(planet1[:])  
print(planet1[0:11:2])  

# slicing a tuple
devops_tuple = ("Dev", "Ops", "Python", "Docker", "Kubernetes")
print(devops_tuple[0]) 
print(devops_tuple[-1])  
print(devops_tuple[1:3]) 
print(devops_tuple[:2]) 

print(devops_tuple[4][:5]) 



# slicing a list
devops_list = ["Dev", "Ops", "Python", "Docker", "Kubernetes"]
print(devops_list[0])  
print(devops_list[-1])  
print(devops_list[1:3]) 
print(devops_list[:2])  

print(devops_list[4][:5]) 


# slicing a dictionary
devops_dict = {
    "Dev": "Development",
    "Ops": "Operations",
    "Python": "Programming Language",
    "Docker": "Containerization",
    "Kubernetes": "Orchestration"
}

print(devops_dict["Dev"]) 
print(devops_dict["Python"])  
print(list(devops_dict.keys())[0])  
print(list(devops_dict.values())[0]) 

# skills dictionary
skills_dict = {
    "Programming": ["Python", "Java", "C++"],
    "DevOps": ["Docker", "Kubernetes", "CI/CD"],
    "Data Science": ["Pandas", "NumPy", "Scikit-learn"]
}

print(skills_dict["Programming"][0])  
print(skills_dict["DevOps"][1])  