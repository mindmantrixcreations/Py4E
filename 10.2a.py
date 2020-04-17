#Py4E 10.2 Write a program to read through 'mbox-short.txt' and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sar Jan  5 09:14:16 2008
#Once you have accumulated the count for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

y=list()
counts = dict()
for line in handle:
   words = line.split()
   if len(words) > 1 and words[0] =='From':
        x=words[5].split(':')
        counts[x[0]]=counts.get(x[0],0)+1

for key, val in counts.items():
    newtup=(key,val)
    y.append(newtup)

y=sorted(y)

for key, val in y:
    print(key,val)
