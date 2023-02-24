# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.


#    O(1) time comlpexity
def even_odd(n):
    
    if (n==0):
        print("num is even")
        return True    
    elif (n==1):
        print("num is odd")
        return False
    else:
        return even_odd(n-2)

even_odd(106)



#   O(1)  time complexity
def even_odd(num:int):
    if num % 2 == 0:
        return True
    else:
        return False
    
result = even_odd(100)
print(result)

 
