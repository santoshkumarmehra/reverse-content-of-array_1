arr=[1,2,3,4,5]
print("array is = ",arr)

new_arr=[]
for i in arr:
	new_arr.append(i)
print("new array is = ",new_arr)

x=0
for j in range(len(arr)-1,-1,-1):
	arr[x]=new_arr[j]
	x=x+1
print("reverse array = ",arr)
