#Example 1 for both Exception handling and file I/O :
try :
    with open("Inventory.txt", "w") as file:            #Creates where my current python file is present
        file.write("Item : laptop\n")
        file.write("Quantity : 25\n")
    print(f"Inventory Exported successfully.")

except PermissionError:
    print("You didn't have permission to read this file.")

except OSError :
    print("A file system error occurred")

finally :
    print("Export process finished")

#Example 2 :

try:
    with open("attendance.txt", "a") as file:
        file.write("Deepak - Present\n")

except PermissionError:
    print("You don't have permission to update attendance.")

except FileNotFoundError:
    print("Attendance file not found.")

else:
    print("Attendance marked successfully.")

finally:
    print("Attendance process finished.")

"""
here :
What do I want to do?
        v
Open the attendance file.
        v
Read or write data.
        v
What can go wrong?
    - File missing
    - No permission
    - Disk full
        v
Handle each problem gracefully.
        v
Make sure the file is always closed.

try   - Attempt an operation that might fail  
except  - Handle a specific failure  
else   - Run only if nothing failed 
finally -  Run no matter what 
open()  -  Open a file    
read()  - Read file contents
write() - Replace the file's contents 
append() -  Add new data to the end     
with open() - Open a file and automatically close it

"""