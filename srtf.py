def select(n,time,key,process={},array=[]):
	i=0
	if key==-1:
		while i<n:
			if(time>=process.get(array[i])[0]):
				key=array[i]

				break
			i=i+1
	i=0
	if key!=-1:
		while i<n:
			if(time>=process.get(array[i])[0]):
				if(process.get(array[i])[2]<process.get(key)[2]):
					key=array[i]		
			i=i+1
	return key

process={1:[1,15,15],2:[2,10,10],3:[4,6,6],4:[5,9,9],5:[6,2,2]}
#n=input('Enter no of processor')
n=5
key=[1,2,3,4,5]
RQ=[]
#i=0
#while i<n:
#	key.append(input('Enter proces no'))
#	process[key[i]]=[input('Enter Arrival time'),input('Enter brust time')]	
#	i=i+1
time=0
while True: 
	temp=-1
	temp=select(n,time,temp,process,key)
	RQ.append(temp)
	time=time+1
	if temp!=-1:
		process.get(temp)[2]=process.get(temp)[2]-1
		if process.get(temp)[2]==0:
			n=n-1
			print temp ,'turning time is=',time-process.get(temp)[0]
			key.remove(temp)
			if n==0:
				break
	
	
