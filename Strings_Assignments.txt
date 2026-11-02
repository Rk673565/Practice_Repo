#  101  Remove the unwanted spaces and display the cleaned name.

employee_name = "   VENKAT REDDY   "
print(len(employee_name))
cleaned_name = employee_name.strip()
print(cleaned_name)
print(len(cleaned_name))

# 102 Convert the customer email address into lowercase before storing it in the database.

email = "VENKAT@GMAIL.COM"
print(email.lower())

# 103 Convert the employee name so that the first character of each word is uppercase.

employee_name = "venkat reddy"
print(employee_name.title())

# 104 Replace spaces in an incoming data file name with underscores.

file_name = "employee data november.csv"
print(file_name.replace(" ", "_"))

# 105 Check whether an incoming file name ends with the CSV extension.

file_name = "employees.csv"

print(file_name.endswith("csv"))

# 106 Extract the email provider domain from the customer email address.

email = "venkat@gmail.com"
print(email.split("@")[1])

# 107 Convert the transaction status into uppercase before generating a transaction report.

status = "success"

print(status.upper())

#  108 Remove unwanted spaces from the customer location.

location = "     Bangalore     "

print (location.strip())

# 109 Check whether the employee ID contains only numeric characters.

employee_id = "102345"

print(employee_id.isnumeric())

#  110 Check whether the employee ID starts with the prefix EMP.

employee_id = "EMP101"

print(employee_id.startswith("EMP"))

#  111 Generate an employee information message using employee details.

employee_id = 101
employee_name = "Venkat"
designation = "Python Developer"
print ("Employee ID :", employee_id)
print("Employee Name:", employee_name)
print("Designation:", designation)

print(f"Employee ID: {employee_id}, Employee Name: {employee_name}, Designation: {designation}")

#  112 Generate an employee salary report using dynamic employee information.

employee_name = "Venkat"
salary = 50000
department = "IT"

print(f"Employee Name: {employee_name}, Salary: {salary}, Department: {department}")

# 113 Generate a transaction message using transaction ID, amount and status.

transaction_id = 1001
amount = 25000
status = "SUCCESS"

print(f"Transaction ID {transaction_id} processed successfully. Amount: {amount}")

#  114 Generate a pipeline execution status message.

pipeline_name = "Customer_ETL"
status = "SUCCESS"

print(f"Pipeline {pipeline_name} execution status: {status}")

#  115 Generate a filename using a table name and processing date.

table_name = "employees"
processing_date = "2026-11-02"

print(f"{table_name}_{processing_date}.csv")

#  116 Generate an API response message using API name and response code.

api_name = "Customer API"
response_code = 200
status = "OK"

print(f"{api_name} returned {response_code} - {status}")

#  117 Generate a data quality message using total and invalid record counts.

total_records = 1000
invalid_records = 50

print("Total Records: ", total_records)
print("Invalid Records: ", invalid_records)

# 118 Display the pipeline execution time with exactly two decimal places.
    
pipeline_name = "Sales_ETL"
execution_time = 12.45678
print(f"{pipeline_name} execution time: {execution_time:.2f}")
print("Pipeline: ", pipeline_name)
print("Execution Time: ", round(execution_time, 2))

# 119 Display the sales amount with two decimal places.

sales_amount = 45678.5678

print("Sales Amount: ", round(sales_amount, 2))

#  120 Extract the first character of the employee name.

employee_name = "VENKAT"
first_character = employee_name[0]
print("First Character: ", first_character)

#  121 Extract the last character of the employee name using negative indexing.

employee_name = "VENKAT"
last_character = employee_name[-1]
print("Last Character: ", last_character)
print("Last Character: ", employee_name[len(employee_name)-1])


# 122 Extract the first character from the employee identifier.

employee_id = "EMP101"
first_character = employee_id[0]
print("First Character: ", first_character)

# 123 Extract the last character of the file extension.

file_name = "employees.csv"

last_character = file_name[-1]
print("Last Character: ", last_character)
print("Last Character: ", file_name[len(file_name)-1])

#  124 tract the third character from the transaction identifier.

transaction_id = "TXN202611"
third_character = transaction_id[2]
print("Third Character: ", third_character)

#  125 Extract the last four characters from a customer reference number using negative indexing.

customer_reference = "CUST987654"
last_four_characters = customer_reference[-4:]
print("Last Four Characters: ", last_four_characters)

#  126 Extract the first four characters from the source system identifier.

source_name = "DATAENGINEER"
first_four_characters = source_name[0:4]
print("First Four Characters: ", first_four_characters)

#  127 Extract the year from the transaction date.

transaction_date = "2026-11-02"

year = transaction_date[0:4]
print("Year: ", year)   

#  128 Extract the month from the transaction date.

transaction_date = "2026-11-02"

month = transaction_date[5:7]
print("Month: ", month)   

Day = transaction_date[8:10]
print("Day: ", Day)

#  129 Extract the filename without its CSV extension.

file_name = "employees.csv"
filename_without_extension = file_name[:-4]
print("Filename without extension: ", filename_without_extension)
print("Filename without extension: ", file_name[0:len(file_name)-4])

#  130 Reverse the transaction identifier using string slicing.

transaction_id = "TXN12345"
reversed_transaction_id = transaction_id[::-1]
print("Reversed Transaction ID: ", reversed_transaction_id)

# 131 Extract alternate characters from the source system identifier, starting from index zero.

source_id = "ABCDEFGHIJ"
print("Alternate Characters: ", source_id[::2])

#  132 Extract the date portion from a fixed-format pipeline error message.

log_message = "ERROR|20261102|CUSTOMER_ETL"
date_portion = log_message.split("|")[1]
print("Date Portion: ", date_portion)



# Extract the transaction prefix, year and sequence number from a fixed-format transaction identifier.

transaction_id = "TXN-2026-1001"
transaction_parts = transaction_id.split("-")
transaction_prefix = transaction_parts[0]
transaction_year = transaction_parts[1]
transaction_sequence = transaction_parts[2]

print("Transaction Prefix: ", transaction_prefix)
print("Transaction Year: ", transaction_year)
print("Transaction Sequence: ", transaction_sequence)


