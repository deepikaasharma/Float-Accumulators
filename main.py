# num_list = [1.6, -2.25, 3.61, 4.01, 5.93]

# num_sum = 0.0
# for num in num_list:
#     num_sum += num

# print(num_sum)


"""Float Accumulators Challenge

For this challenge:

    Instantiate an empty list called running_total
    Instantiate a new float accumulator called total

Then iterate through num_list accumulating the sum in total as you go. Append the current value of total to running_total after the value of total is updated."""

# # Leave this line alone
# num_list = [1.1, 1.1, 2.2, 3.3, 5.5, 8.8]

# # Write your code here

# running_total = []

# total = 0.0

# for num in num_list:
#   total += num
#   running_total.append(total)


# print(total)

# print(running_total)


"""Sum up the absolute value of only the floating point numbers in mixed_data using an accumulator called abs_sum."""

# # Leave this line alone
# mixed_data = [1.1, -1.1, 5, 2.2, -3.3, "oops I'm not a number!", 98532334, 5.5, 8.8, True, True, -0.512]

# # Write your code here

# abs_lst =[]
# abs_sum = 0.0

# for num in mixed_data:
#   if isinstance(num, float):
#     abs_sum += abs(num)


# print(abs_sum)


"""For this challenge, write code that will calculate the final average of num_list. Also track the rolling average of the values in num_list. The variable for the final average should be called num_avg, and the rolling average variable should be a list called rolling_avg."""

# Leave this line alone
num_list = [0.136, 0.082, 2.691, 1.175, 4.737, 0.083, 0.082, 1.161, 2.41, 0.0, 7.421, 6.496, 5.012, 1.145, 6.512, 4.547, 4.245, 2.093, 3.511, 3.059, 1.247, 1.882, 7.155, 8.881, 5.095]

# Write your code here
num_avg = 0.136

rolling_avg = []


num_sum =0.0
current_length = 0.0

for idx, num in enumerate(num_list, 0):
  num_sum +=num

  current_length = idx+1

  num_avg = num_sum/current_length

  rolling_avg.append(num_avg)

 
print(num_avg)

print(rolling_avg)