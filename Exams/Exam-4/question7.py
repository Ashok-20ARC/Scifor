def remove_duplicates(filename):
    f=open(filename,'r')
    
    lines=f.readlines()
    
    f.close()
    
    cleanedLine=[]
    
    for line in lines:
        words=line.split()
        
        unique_words=[]
        
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
            
        cleanedLine.append(" ".join(unique_words))
        
    f=open(filename,'w')
    
    f.write("\n".join(cleanedLine))
    
    f.close()
    
    print("Duplicates are removed Successfully")
    
remove_duplicates("quest7.txt")