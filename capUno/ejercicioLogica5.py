# security check for a website. 
# list of premium users, and banned users. 
# a user has access if it is on the premium_users and not on the banned_users.

premium_users = ["alice", "bob", "charlie"]

banned_users = ["dave","bob"]

current_user = "alice"

is_premium = current_user in premium_users

is_banned = current_user in banned_users

has_access = is_premium and not is_banned

print(f"Checking acces for user:  {current_user}")

print(f"Is premium user? {is_premium}")

print(f"Is banned user? {is_banned}")

print(f"Access granted? {has_access}")
