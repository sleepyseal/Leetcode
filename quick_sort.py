def quick(nums, left, right):
    if left>=right:
        return
    pivot=nums[left]
    i=left
    j=right
    while i<j:
        while nums[j]>=pivot and i<j:
            j-=1
        while nums[i]<=pivot and i<j:
            i+=1
        if i<j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp 
    nums[left]=nums[i]
    nums[i]=pivot
    quick(nums, left, i-1)
    quick(nums, i+1, right)
        
arr = [3, 6, 8, 10, 1, 2, 1]
quick(arr, 0, len(arr) - 1)
print(arr)       

def quick(nums, left, right):
    if left>=right:
        return
    i, j= left, right
    pivot=nums[left]
    while i<j:
        while i<j and nums[j]>=pivot:
            j-=1
        while i<j and nums[i]<=pivot:
            i+=1
        if i<j:
            swap(nums, i, j)
        swap(nums, i, left)
        quick(nums, left, i-1)
        quick(nums, i+1, right)