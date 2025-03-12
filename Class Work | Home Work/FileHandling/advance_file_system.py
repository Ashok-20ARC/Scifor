import os

def main_menu():
    print("\n-----Advanced File System-----")
    print("1.Create a new file")
    print("2.Write to a file")
    print("3.Read a file")
    print("4.Append to a file")
    print("5.Delete a file")
    print("6.Exit")
    
def create():
    file_name=input("Enter the name of the file to create :")
    
    if os.path.exists(file_name):
        print("File already exists...")
    else:
        with open(file_name,"w") as file:
            print("File",file_name,"created successfully")
            
def write():
    file_name=input("Enter the name of the file to write : ")
    
    if os.path.exists(file_name):
        content=input("Enter what should write in a file : ")
        with open(file_name,'w') as file:    
            file.write(content)
            print("\ncontent written successfully")
        
    else:
        print("file does not exist.")
        
def read():
    file_name=input("Enter the name of the file to read : ")

    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            content=file.read()
            
            print("\nContent of the file",file_name,":",content)
            
    else:
        print("File does not exist")
        
def append():
    file_name=input("Enter the name of the file to append the content : ")
    
    content=input("Enter content to append to the file : ")
    
    if os.path.exists(file_name):
        with open(file_name,'a') as file:
            file.write(content)
            print("Content appending successfully")
        
    else:
        print("file does not exists")
        
def delete():
    file_name=input("Enter the name of the file to delete : ")
    
    if os.path.exists(file_name):
        os.remove(file_name)
        print("file deletion successful")
    
    else:
        print("file does not exist")

def advance_file_system():
    while True:
        main_menu()
        choice=input("Enter your choice : ")
        
        if choice=="1":
            create()
        elif choice=="2":
            write()
        elif choice=="3":
            read()
        elif choice=="4":
            append()
        elif choice=="5":
            delete()
        elif choice=="6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
            
advance_file_system()