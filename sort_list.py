# Given a list of unsorted, manually sort the list into ascending order (may not use built in .sort() method).
# Suggested strategy:
# Starting with the first two unsorted, compare them to see which is larger. 
# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of unsorted one at a time.
# Repeat from the start until the entire list is sorted.
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

#     time complexity

# def sort_list(arr):
#     for j in range(len(arr)-1):
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i]+1:
#                 temp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = temp
               

#     return arr
# unsorted = [6,8,3,4,7,2]
# sorted = sort_list(unsorted)
# print(sorted)

#   O(n^2) -Quadratic time complexity

def sort_list(num_list: list):
    for j in range(len(num_list)-1):
        for i in range(len(num_list)-1):
            current_number = num_list[i]
            next_number = num_list[i + 1]
            if current_number > next_number:
                num_list[i] = next_number
                num_list[i+1] = current_number

    return num_list
    

sorted = sort_list([6,8,3,4,7,2])
print(sorted)



    