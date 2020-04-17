#Py4E 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greater number of mail messages
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python Dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
   words = line.split()
   if len(words) > 1 and words[0] =='From':
        counts[words[1]]=counts.get(words[1],0)+1


MaxWord = None
MaxNum = None
for word, count in counts.items():
    if MaxNum is None or count>MaxNum:
        MaxNum=count
        MaxWord=word

print(MaxWord, MaxNum)
