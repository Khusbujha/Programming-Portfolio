"""This program demostrates a function named update_weekly_sales that takes a dictionary of weekly sales data, a day name, and a sale amount.
If the day already exists, update the sale amount by adding the new amount.
If the day does not exist, add it to the dictionary.
Return the updated dictionary.
"""


def update_weekly_sales(weekly_sales, day, amount):
    if day in weekly_sales:
        weekly_sales[day] += amount
    else:
        weekly_sales[day] = amount
    return weekly_sales


sales_data = {"Monday": 1000, "Tuesday": 1200, "Friday": 800}
print("Original data:", sales_data)
print(update_weekly_sales(sales_data, "Monday", 500))
print(update_weekly_sales(sales_data, "Wednesday", 700))
