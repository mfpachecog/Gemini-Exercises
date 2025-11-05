# exercise managing sets 

# users can submit tags to the program, but we need to confirm that there's no duplicates

submitted_tags = ["python", "coding", "programming", "python", "best practices", "coding"]

unique_tags = set(submitted_tags)

unique_tags.add("developer")

#print(f"current set:  {unique_tags}")

# adding duplicate tag
unique_tags.add("python")

#checking if set changed
#print(f"current set:  {unique_tags}")

is_programming_tag_present = "programming" in unique_tags
print(f"Is \'programming\' tag present? {is_programming_tag_present}")

#final tags 

print(f"Final unique tags: {unique_tags}")
