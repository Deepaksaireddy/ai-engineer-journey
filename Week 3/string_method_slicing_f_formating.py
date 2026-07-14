"""Strings are immutable. Used methods ARE upper(), lower(), strip(), replace(), split(), join(), find(),
index(), count(), startswith(), endswith(), isdigit(), isalpha(), isnumeric(), isalnum(), isspace(). Slicing
uses s[start:end:step], including negative indexes and s[::-1]. f-strings support variables,
expressions, formatting, alignment, padding, commas and percentages."""

employees=\
[" emp001 , deepak l , developer , 85000 , deepak@company.com , +91-9876543210 ",
 " emp002 , rahul , tester , 72000 , jane@company.com , +91-9988776655 "]
clean=[]
for row in employees:
    row=row.strip()                             # strip spaces
    cols=[c.strip() for c in row.split(",")]    # split + strip
    emp_id=cols[0].upper()                      # uppercase
    name=cols[1].title()                        # title case
    role=cols[2].capitalize()                   # capitalize
    salary=int(cols[3]) if cols[3].isdigit() else 0
    email=cols[4].lower()                       # lowercase
    if email.find("@")==-1:
        print("Invalid email")
    if not email.endswith("@company.com"):
        print("External email")
    phone=cols[5].replace("-","").replace("+","")
    masked="*"*(len(phone)-4)+phone[-4:] # slicing
    clean.append(",".join([emp_id,name,role,str(salary),email,masked]))
print(f'{"ID":<10}{"NAME":<20}{"ROLE":<15}{"SALARY":>10}')
for r in clean:
 i,n,ro,s,e,p=r.split(",")
 print(f"{i:<10}{n:<20}{ro:<15}{int(s):>10,}")