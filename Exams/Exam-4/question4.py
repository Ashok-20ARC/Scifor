def adding_serial_num(filename):
    f=open(filename,"r")
    
    lines=f.readlines()
    
    f.close()
    
    f=open(filename,"w")
    
    serial_num=1
    
    for line in lines:
        f.write(f"{serial_num}.{line}")
        serial_num+=1
    print("Serial numbers added successfully")
    
f_name=input("Enter file name with extenstion :")

adding_serial_num(f_name)
    