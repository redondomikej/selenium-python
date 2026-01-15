import pandas as pd
import os

# Define the test cases data
data = [
    ["LOGIN_01", "Login", "Verify login with valid credentials", "User is on login page", "1. Enter valid username and password\n2. Click Login", "User should be redirected to the dashboard", "High"],
    ["LOGIN_02", "Login", "Verify login with invalid credentials", "User is on login page", "1. Enter invalid username or password\n2. Click Login", "Error message 'Invalid credentials' is displayed", "High"],
    ["LOGIN_03", "Login", "Verify login with empty fields", "User is on login page", "1. Leave username and password empty\n2. Click Login", "Error message 'Required' displayed for empty fields", "Medium"],
    ["LOGIN_04", "Login", "Verify logout functionality", "User is logged in", "1. Click on profile dropdown\n2. Click Logout", "User should be redirected to login page", "High"],
    ["ADMIN_01", "Admin", "Verify Admin page access", "User is logged in as Admin", "1. Navigate to Admin module", "Admin page opens with search and add user options", "High"],
    ["ADMIN_02", "Admin", "Add a new user", "Admin page is open", "1. Click Add User\n2. Fill in required fields\n3. Click Save", "New user should be created and listed", "High"],
    ["ADMIN_03", "Admin", "Search for a user", "Admin page is open", "1. Enter username or employee name in search\n2. Click Search", "User matching criteria should appear in results", "Medium"],
    ["ADMIN_04", "Admin", "Edit a user", "Admin page is open", "1. Search for a user\n2. Click Edit\n3. Update fields\n4. Click Save", "User details should be updated successfully", "Medium"],
    ["ADMIN_05", "Admin", "Delete a user", "Admin page is open", "1. Search for a user\n2. Click Delete\n3. Confirm deletion", "User should be removed from the list", "High"],
    ["PIM_01", "PIM", "Verify PIM page access", "User is logged in", "1. Navigate to PIM module", "PIM page opens with employee list", "High"],
    ["PIM_02", "PIM", "Add a new employee", "PIM page is open", "1. Click Add Employee\n2. Fill required details\n3. Click Save", "New employee is added successfully", "High"],
    ["PIM_03", "PIM", "Search for an employee", "PIM page is open", "1. Enter employee name or ID\n2. Click Search", "Employee details matching criteria are displayed", "Medium"],
    ["PIM_04", "PIM", "Edit employee details", "Employee exists in list", "1. Search employee\n2. Click Edit\n3. Update details\n4. Click Save", "Employee information updated successfully", "Medium"],
    ["PIM_05", "PIM", "Delete an employee", "Employee exists in list", "1. Search employee\n2. Click Delete\n3. Confirm deletion", "Employee should be removed from list", "High"],
    ["LEAVE_01", "Leave", "Verify Leave page access", "User is logged in", "1. Navigate to Leave module", "Leave page opens with leave list", "High"],
    ["LEAVE_02", "Leave", "Apply for leave", "Leave page is open", "1. Click Apply\n2. Select leave type, dates, reason\n3. Click Submit", "Leave request is submitted successfully", "High"],
    ["LEAVE_03", "Leave", "Approve leave", "Leave request exists", "1. Login as Manager\n2. Navigate to Leave module\n3. Approve leave request", "Leave status changes to Approved", "High"],
    ["LEAVE_04", "Leave", "Reject leave", "Leave request exists", "1. Login as Manager\n2. Navigate to Leave module\n3. Reject leave request", "Leave status changes to Rejected", "High"]
]

# Create a DataFrame
columns = ["Test Case ID", "Module", "Description", "Precondition", "Steps", "Expected Result", "Priority"]
df = pd.DataFrame(data, columns=columns)

# Create output folder if it doesn't exist
folder = "output"
if not os.path.exists(folder):
    os.makedirs(folder)

# Save to Excel inside the folder
file_path = os.path.join(folder, "OrangeHRM_TestCases.xlsx")
df.to_excel(file_path, index=False)

print(f"Excel file saved at: {file_path}")
