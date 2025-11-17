# dictionaries. 

user_profile = {

    "username":"code_master_95",
    "age":28,
    "active_courses":["Python Basics", "Data Structures"],
    
    
}

print(f"user name: {user_profile.get('username')}")

user_profile.update({"is_verified":True})

user_profile["active_courses"].append("Machine learning")

print(f"total information: {user_profile}")

print(f"all the keys: {user_profile.items()}")