class Solution:
    def int2array(self, num):
        ans=[]
        while num>=10:
            res=num%10
            num=num//10
            ans.append(str(res))
        ans.append(str(num))

        return ans 

    def intToRoman(self, num):
        num=self.int2array(num)
        s=''
        d={'1':'I', '5':'V', '4':'IV'}
        count=0
        for i in num:
            if int(i) <4:
                temp='I'*int(i)
            elif i =='4' or i =='5':
                temp=d[i]
            elif int(i)>5 and int(i)<9:
                temp='V'+'I'*(int(i)-5)
            else:
                temp='IX'

            if count==0:
                s=temp+s
            elif count==1:
                temp_10=''
                for i in temp:
                    if i=='I':
                        temp_10+='X'
                    elif i=='V':
                        temp_10+='L'
                    else: 
                        temp_10+='C'
                s=temp_10+s
            elif count==2:
                temp_100=''
                for i in temp:
                    if i=='I':
                        temp_100+='C'
                    elif i=='V':
                        temp_100+='D'
                    else:
                        temp_100+='M'
                s=temp_100+s 
            elif count==3:
                temp_1000=''
                for i in temp:
                    if i=='I':
                        temp_1000+='M'  
                s=temp_1000+s   
            count+=1
        return s
num = 10
print(Solution().intToRoman(num))