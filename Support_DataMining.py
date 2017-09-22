num=int(raw_input("Enter no of transactions"))
transactions=[]
print 'Enter transac strings'
for i in xrange(0,num):
    tstring=raw_input()
    transactions.append(tstring)
print 'Enter Support String'
supcheck=raw_input()
suplen=len(supcheck)
supcount=0
for j in xrange(0,num):
    templen=suplen
    for i in supcheck:
        for k in transactions[j]:
            if i==k:
                templen -= 1
                if templen == 0:
                    supcount += 1
                break
support=float(supcount)/float(num)
print support
