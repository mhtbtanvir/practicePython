total = 0
Total_list = []
number_list = []
for number in range(1, 11, 2):

    total += number

    Total_list.append(total)
    number_list.append(number)
print(f'Even numbers are:{number_list} \n')
print("Total of even numbers is:", Total_list)
