arr =[1,4,20,3,10]
target = 33
left=0
current_sum=0
for right in range (len(arr)):
  current_sum = current_sum+arr[right]
  while current_sum > target:
    current_sum = current_sum-arr[left]
    left = left+1
    if current_sum == target:
     print(arr[left:right+1])
     break     