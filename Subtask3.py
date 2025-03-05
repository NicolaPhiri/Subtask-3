# Name : Nicola
# Surname: Phiri
# Date: 5/03/2025
# Project: Inventory Logging at Big Wig Electronics Subtask 3
# Purpose: Calculating Costs

# Importing and creating logging
import logging
logging.basicConfig(
    filename='Inventory_log.txt',                # log file name
    level=logging.INFO,                          # Set logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
    filemode='a',      # Allows the log to not be overridden but for the logs to be appended.

)
# Prompts
strproduct_name = input("Please enter the product name: " + " ")
intquantity = int(input("Please enter the quantity of products: " + " "))
strsupplier_name = input("Please enter the supplier's name: " + " ")
# The cost needs to be in float, not int
fltcost_per_unit = float(input("Please enter the cost per unit in rands: " + " "))
# Calculations
flttotal_cost = round(float(intquantity) * fltcost_per_unit, 2)

# Convert to binary then display the binary representation
print("The total cost is: " + str(bin(int(flttotal_cost))))
# Create data saving function


def collect_data():
    data = {"Product": strproduct_name, "Quantity": intquantity,

            "Supplier Name": strsupplier_name, "Total Cost": flttotal_cost}
    return data
# Collect and log the data


data = collect_data()  # Store the collected data in 'data'

# Creating condition to save to log
if flttotal_cost > 500:
    logging.info("Mark as large order")
    logging.info(f"Product: {data['Product']}, Quantity: {data['Quantity']}, "
                 f"Supplier Name: {data['Supplier Name']}, Total Cost: {data['Total Cost']}")
    # Print log data to the console
    print(f"Product: {data['Product']}, Quantity: {data['Quantity']}, "
          f"Supplier Name: {data['Supplier Name']}, Total Cost: {data['Total Cost']}"), print("(Large Order)")

else:
    logging.info(f"Collected data: Product: {data['Product']}, Quantity: {data['Quantity']}, "
                 f"Supplier Name: {data['Supplier Name']}, Total Cost: {data['Total Cost']}")
# Print log data to the console
    print(f"Product: {data['Product']}, Quantity: {data['Quantity']}, "
        f"Supplier Name: {data['Supplier Name']}, Total Cost: {data['Total Cost']}")
