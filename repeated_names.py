# Given a list of names, determine if any names are contained in the list more than once.
# The function should take in the list as a parameter and return a boolean value (True if there are any repeated names, False if there are no repeats).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

#   O(n)   time complexity

names1 = ['Josh', 'Ben', 'Josh', 'Kayla', 'Sue']

def repeat_name(names1):
    names2 = ['Josh', 'Ben', 'Kayla', 'Sue']
    for name in names1:
        if names1 != names2:
            print('this list has duplicates')
            return True
    print ('this list has no repeated names')
    return False
    
repeat_name(names1)

