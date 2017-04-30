def smallest(n,dictonary={},array=[]):
	i=0
	key=array[0]
	smallest=9999
	while i<n:	
		if dictonary.get(array[i])[0]<smallest:
			smallest=dictonary.get(array[i])[0]
			key=array[i]
		i=i+1
	return key

process={1:[0,2],2:[5,2],3:[3,3],4:[1,6],5:[2,7]}
#n=input('Enter no of processor')
n=5
key=[1,2,3,4,5]
#i=0
#while i<n:
#	key.append(input('Enter proces no'))
#	process[key[i]]=[input('Enter Arrival time'),input('Enter brust time')]
#	i=i+1
time=0
i=0
while n>0:
	temp=smallest(n,process,key)
	if i==0:
		time=process.get(temp)[0]
		i=i+1
	if process.get(temp)[0]>time:
		time=process.get(temp)[0]
	time=time+process.get(temp)[1]
	process.get(temp).append(time-process.get(temp)[0])
	print temp,'is running Turn around time=',process.get(temp)[2]
	key.remove(temp)
	n=n-1



