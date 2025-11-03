# movie requierement. You must be 18 years old or older.
# a 17 year old is allowed if they are accompanied by someone 21 or older.

my_age = 17

companion_age = 25

is_old_enough = my_age >= 18

family_day_rule_met = my_age == 17 and companion_age >= 21

can_watch_movie = is_old_enough or family_day_rule_met

print(f"Am i old enough on my own? {is_old_enough}" )

print(f"Is the family Day rule met? {family_day_rule_met}")

print(f"Can i watch the movie? {can_watch_movie}")

