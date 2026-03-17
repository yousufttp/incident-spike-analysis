Create a Python module that reads an Excel file of incidents. Expected columns may include:
Incident ID, Created Date, Category, Area, Short Description, Detailed Description.
Standardize column names to snake_case, parse created date into datetime, fill missing text fields with empty string, and create a combined_text column using short description + detailed description.
Return a cleaned pandas DataFrame.