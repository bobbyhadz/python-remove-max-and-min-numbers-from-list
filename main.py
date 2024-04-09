# Remove the Max and Min numbers from a List in Python

my_list = [1, 25, 50, 100]

# ✅ Remove max value from list
my_list.remove(max(my_list))
print(my_list)  # 👉️ [1, 25, 50]

# -----------------------------------

# ✅ Remove min value from list
my_list.remove(min(my_list))
print(my_list)  # 👉️ [25, 50]