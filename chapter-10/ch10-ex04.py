# Chapter 10
# Exercise 4

# Define the classes
class employee:
    emp_name = ''
    id_num = ''
    emp_dept = ''
    emp_title = ''

# Create an object from the employee class
emp_obj_one = employee()

# Assign values to obj one
emp_obj_one.emp_name = 'Susan Meyers'
emp_obj_one.id_num = '47899'
emp_obj_one.emp_dept = 'Accounting'
emp_obj_one.emp_title = 'Vice President'

# Create another object
emp_obj_two = employee()

# Assign values to obj two
emp_obj_two.emp_name = 'Mark Jones'
emp_obj_two.id_num = '39119'
emp_obj_two.emp_dept = 'IT'
emp_obj_two.emp_title = 'Programmer'

# Create another object
emp_obj_three = employee()

# Assign values to obj two
emp_obj_three.emp_name = 'Joy Rogers'
emp_obj_three.id_num = '81774'
emp_obj_three.emp_dept = 'Manufacturing'
emp_obj_three.emp_title = 'Engineer'

# Print the employee details
# Print employee 1
print('Employee 1 details: ')
print('Employee Name: ', emp_obj_one.emp_name)
print('Employee ID Number: ', emp_obj_one.id_num)
print('Employee Department: ', emp_obj_one.emp_dept)
print('Employee Job Title: ', emp_obj_one.emp_title)

# Print employee 2
print('Employee 2 details: ')
print('Employee Name: ', emp_obj_two.emp_name)
print('Employee ID Number: ', emp_obj_two.id_num)
print('Employee Department: ', emp_obj_two.emp_dept)
print('Employee Job Title: ', emp_obj_two.emp_title)

# Print employee 3
print('Employee 2 details: ')
print('Employee Name: ', emp_obj_three.emp_name)
print('Employee ID Number: ', emp_obj_three.id_num)
print('Employee Department: ', emp_obj_three.emp_dept)
print('Employee Job Title: ', emp_obj_three.emp_title)
