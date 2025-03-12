import re

def modify_file(filename):
    
    f=open(filename,'r')
    
    content=f.read()
    
    f.close()
    
    modified_content=re.sub(r"(\d\.)",r"\1\n",content)
    
    f=open(filename,"w")
    
    f.write(modified_content)
    
    print("file modified successfully")
    
modify_file("modify.txt")