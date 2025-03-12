f=open("file.txt",'r')

content=f.read()

sentences=content.split('.')



        
sentence_strip=[sentence.strip() for sentence in sentences if sentence.strip()]

tot_sentences=len(sentence_strip)

starts_with_a_sentence=0

for sentence in sentence_strip:
    if sentence.lower().startswith('a'):
        starts_with_a_sentence+=1
        
print("Sentences split by (.) :",sentence_strip)
print("\nNumber of sentences in this file : ",tot_sentences)
print("\nNumber of sentences starts with 'a' letter :",starts_with_a_sentence)
        

