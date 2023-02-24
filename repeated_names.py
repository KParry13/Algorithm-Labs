# Given a list of names, determine if any names are contained in the list more than once.
# The function should take in the list as a parameter and return a boolean value (True if there are any repeated names, False if there are no repeats).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

#   O(n)   time complexity

# names1 = ['Josh', 'Ben', 'Josh', 'Kayla', 'Sue']

# def repeat_name(names1):
#     names2 = []
#     for name in range(len(names1)):
#         if names1 == names2:
#             print('this list has duplicates')
#             return True
#     print ('this list has no repeated names')
#     return False
    
# repeat_name(names1)


def duplicate_name_checker(name_list: list):
    unique_names = []
    for name in name_list:
        if name not in unique_names:
            unique_names.append(name)
    if len(name_list) == len(unique_names):
        return False
    else:
        return True
        

result = duplicate_name_checker(['Josh', 'Ben', 'Josh', 'Kayla', 'Sue'])
print (result)

