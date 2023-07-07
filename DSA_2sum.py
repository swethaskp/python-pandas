def add_2sum(nums,target):
    num_list=[]
    for i,num in enumerate(nums):
        diff = target-num
        
        if diff in nums:
           if diff in num_list:
               
               return(num_list)
           else:
                num_list.append(num)
                
                num_list.append(diff)
           return(num_list)
           
    return(num_list)

li=[5,6,2,4,5,1]
target=10
print(add_2sum(li,target))
