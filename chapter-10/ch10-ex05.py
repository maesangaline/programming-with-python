# Chapter 10
# Exercise 5

# Define the classes
class RetailItem:
    item_num = ''
    item_desc = ''
    item_inven = ''
    item_price = ''

# Create an object from the retail item class
item_obj_one = RetailItem()

# Assign values to obj one
item_obj_one.item_num = 'Item 1'
item_obj_one.item_desc = 'Jacket'
item_obj_one.item_inven = '12'
item_obj_one.item_price = '59.95'

# Create another object
item_obj_two = RetailItem()

# Assign values to obj two
item_obj_two.item_num = 'Item 2'
item_obj_two.item_desc = 'Designer Jeans'
item_obj_two.item_inven = '40'
item_obj_two.item_price = '34.95'

# Create another object
item_obj_three = RetailItem()

# Assign values to obj three
item_obj_three.item_num = 'Item 3'
item_obj_three.item_desc = 'Shirt'
item_obj_three.item_inven = '20'
item_obj_three.item_price = '24.95'

# Print the employee details
# Print item 1
print('Item 1 Details: ')
print('Item Description: ', item_obj_one.item_desc)
print('Item Units in Inventory: ', item_obj_one.item_inven)
print('Item Pricet: ', item_obj_one.item_price)


# Print item 2
print('Item 2 Details: ')
print('Item Description: ', item_obj_two.item_desc)
print('Item Units in Inventory: ', item_obj_two.item_inven)
print('Item Pricet: ', item_obj_two.item_price)

# Print item 3
print('Item 3 Details: ')
print('Item Description: ', item_obj_three.item_desc)
print('Item Units in Inventory: ', item_obj_three.item_inven)
print('Item Pricet: ', item_obj_three.item_price)
