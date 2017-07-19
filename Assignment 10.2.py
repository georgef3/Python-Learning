#10.2 Write a program to read through the mbox-short.txt 
#and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by 
#finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname,'r')

counts = dict()

for line in handle: #creates a loop that reads each line
    line = line.rstrip()
    if not line.startswith('From'):continue #only ingest those lines that start with From:
    words = line.split()#split the line into parts
    if words[0] !='From':continue
    time = words[5].split(':') #creates a variable time at the fifth character
    counts[time[0]]=counts.get(time[0],0)+1

lst=list()
for key, val in counts.items():
    lst.append( (key,val) )
        
lst.sort()


for hour, count in lst:
	print hour, count
