# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

#   O(n)  time complexity
num = [20, 33, 10, 75, 96]
def less_than_100(num):
    
    n=100
    for i in num:
        if i >= n:
            print('this list has some numbers over or equal too 100')
            return False
    print('this list is all under 100')
    return True 
    

less_than_100(num)


def hundred_checker(num_list: list):
    for number in num_list:
        if number <= 100:
            return False
    return True

results =hundred_checker([20, 40, 101])
print (results)

    
    
    