# Leetcode problem 1: Two Sum
l = [8, 3, 1, 7, 2, 5]
t = 10

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == t:
            print([i, j])

# Leetcode problem 2: sliding window maximum
p = [1, 4, 5, 6, 2, 3]
maxprof = 0
minprice = float('inf')

for i in p:
    minprice = min(i, minprice)  # Update the minimum price
    prof = i - minprice  # Calculate the profit if sold at price 'i'
    maxprof = max(prof, maxprof)  # Update the maximum profit

print(maxprof)


# Leetcode problem 3: Contains Duplicate
l = [1, 2, 3, 1, 3]
seen = []

for i in l:
    if i in seen:
        print("true")
        break  # Exit the loop after finding the duplicate
    seen.append(i)
else:
    print("false")




# Leetcode problem 4: Product of Array Except Self
import numpy as np

nums = np.array([1, 2, 3, 4])
total_product = np.prod(nums)  # Multiply all elements

output = total_product // nums  # Divide total product by each element
print(output)



# Leetcode problem 5: Maximum Subarray
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = nums[0]
curr_sum = nums[0]

for i in nums[1:]:
    curr_sum = max(i, curr_sum + i)
    max_sum = max(max_sum, curr_sum)

print(max_sum)

# Leetcode problem 6: Maximum Product Subarray
nums = [2, 3, -2, 4]

max_prod = nums[0]
curr_max = nums[0]
curr_min = nums[0]

for i in nums[1:]:
    temp = curr_max
    curr_max = max(i, curr_max * i, curr_min * i)
    curr_min = min(i, temp * i, curr_min * i)
    max_prod = max(max_prod, curr_max)

print(max_prod)

#dropped



#leetcode python easy problems

# move zeroes

l = [1, 0, 3, 0, 3, 4, 5]

nz = 0  # Pointer to track the position of non-zero elements

# Loop through the array
for i in range(len(l)):
    if l[i] != 0:
        # Swap non-zero element with the element at 'nz'
        l[nz], l[i] = l[i], l[nz]
        nz += 1

print(l)


# Invert a binary tree
# Representing the tree as a nested list
root = [4, [2, None, None], [7, None, None]]

# Invert the tree
stack = [root]

while stack:
    node = stack.pop()
    if node:
        # Swap the left and right children
        node[1], node[2] = node[2], node[1]
        # Add the left and right children to the stack
        stack.append(node[1])
        stack.append(node[2])

# The tree is now inverted
print(root)

