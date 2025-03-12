def replace_word_file(filename,incorrectword,correctword):


    f=open(filename,"r")

    content=f.read()

    print(content)

    f.close()

    updated_content=content.replace(incorrectword,correctword)

    f=open(filename,"w")

    f.write(updated_content)

    f.close()

    print("Incorrected Words are corrected successfully")
    
replace_word_file("lang.txt", "langage", "language")