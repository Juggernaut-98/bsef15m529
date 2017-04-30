def smallest(n,dictonary={},array=[]):
	i=0
	key=array[0]
	smallest=9999
	smallest_time=0
	while i<n:	
		if dictonary.get(array[i])[0]<smallest:
			smallest=dictonary.get(array[i])[0]
			smallest_time=dictonary.get(array[i])[1]
			key=array[i]
		if dictonary.get(array[i])[0]==smallest:
			if dictonary.get(array[i])[1]<smallest_time:
				key=array[i]
				smallest_time=dictonary.get(array[i])[1]
		i=i+1
	return key

process={1:[0,9],2:[0,2],3:[0,8],4:[0,6],5:[0,7]}
#n=input('Enter no of processor')
n=5
key=[1,2,3,4,5]
#i=0
#while i<n:
#	key.append(input('Enter proces no'))
#	process[key[i]]=[input('Enter Arrival time'),input('Enter brust time')]
#	i=i+1
time=0
while n>0:
	temp=smallest(n,process,key)
	if process.get(temp)[0]>time:
		time=process.get(temp)[0]
	time=time+process.get(temp)[1]
	process.get(temp).append(time-process.get(temp)[0])
	print temp,'is running Brust time=',process.get(temp)[2]
	key.remove(temp)
	n=n-1



