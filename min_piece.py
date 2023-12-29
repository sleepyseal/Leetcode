def contain(list1,list2):
    flag = False
    for i in range(len(list2) - len(list1) + 1):
        if list2[i: i+len(list1)] == list1:
            flag = True
            break
    return flag 

def min_pieces(original, desired):
    i=0
    cut=0
    while i <len(original):
        min_len=2
        sub_o=original[i:i+min_len]
        while contain(sub_o, desired):
            if i+min_len>=len(original):
                break
            min_len+=1
            sub_o=original[i:i+min_len]
        if i+min_len<len(original):
            cut+=1
        i=i+min_len-1
    return cut+1
original = [1, 4, 3, 2]
desired = [1,2,3,4]
print(min_pieces(original, desired))