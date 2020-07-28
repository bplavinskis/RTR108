# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
rez = float('0')
skaits = int('0')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    atpos = line.find('0')
    host = line[atpos:]
    rez = rez + float(host)
    skaits=skaits+1
print("Average spam confidence:",rez/skaits)	
