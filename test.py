#给定一个非负整数，反复将它的个个位数相加，直到它为个位数，如果
def merge_interval(input_interval):
    #输入是空 第二个点排序
    input_interval.sort()
    l=len(input_interval)
    ans=[]
    ans.append(input_interval[0])
    for i in range(1, l):
        if input_interval[i][0]<=input_interval[i-1][1]:
            right=max(input_interval[i][1], input_interval[i-1][1])
            ans[-1][1]=right
        else:
            ans.append(input_interval[i])
    return ans
l=[[1,3],[4,6],[8,10],[1,4]]
print(merge_interval(l))