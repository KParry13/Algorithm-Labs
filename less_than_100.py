# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

#      time complexity
num = [20, 33, 109, 75, 96]
def less_than_100(num):
    
    n=100
    for i in num:
        if i >= n:
            print('this list has some numbers over or equal too 100')
            return False
      

less_than_100(num)

    
    
    