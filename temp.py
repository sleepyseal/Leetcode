def compare(input, left_ele, right_ele):
    if input>left_ele and input>right_ele:
        return True
    return False

def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    # Write your code here
    origin_data=entries.copy()
    l=len(entries)
    for i in range(l):
        left=i-3
        right=i+4
        if left>=0 and right<l:
            res=compare(origin_data[i], origin_data[left], origin_data[right])
        elif left<0 and right<l:
            res=compare(origin_data[i], origin_data[i]-1, origin_data[right])
        elif left<0 and right>=l:
            res=True
        elif left>=0 and right>=l:
            res=compare(origin_data[i], origin_data[left], origin_data[i]-1)  
        if res:
            pass
        else:
            entries[i]=0 
    return entries       

records = [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]
print(simulate(records))
# Expected output
# [1, 0, 0, 5, 0, 0, 0, 3, 3, 0]