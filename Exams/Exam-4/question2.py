f=open("quest2.txt","r")

lines=f.readlines()
found=False

lineNumber=1

for line in lines:
    has_num=False
    for char in line:
        if char.isdigit():
            has_num=True
            break
    
    if has_num:
        print(f"Line {lineNumber} {line.strip()}")
        found=True
    
    lineNumber+=1
    
    
if not found:
    print("No numerical values are found in this file")