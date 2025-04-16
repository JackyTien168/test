result1,result2='',''
for i in range(0,10,3): #(1) 1,2,3,4,5,6,7,8,9
    # result1=''
    for j in range(1,10): #(1) 1,2,3,4,5,6,7,8,9
        result1=''
        for k in (1,2,3):
            result1=str(k+i) + '*' + str(j) + '=' + str((k+i)*j)+'\t' #(1) result1='1*1=1'+'1*2=2' (2) result1='1*1=1'+'1*2=2'
            result2=result2+result1
        result2=result2+'\n'
                 #(1回合)1*1=1   1*2=2    1*3=3  
                   #      2*1=2    2*2=4  
       
      
    result2=result2+'\n'

#     result2=result2+result1+'\n'
print(result2)