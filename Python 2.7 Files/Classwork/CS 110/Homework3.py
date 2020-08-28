#Homework 3
#1
def min_value(thelist):
    min_value=thelist[0]
    for number in thelist:
		if number>min_value:
			pass
		else:
			min_value=number
    return min_value

#2
def gauss(N):
    sum=0
    for number in range(1,N+1):
		sum=sum+number
    return sum
#3
def sumOfSquares(N):
	sum=0
	for number in range(1,N+1):
		sum=sum+number*number
	return sum
