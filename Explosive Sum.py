def exp_sum(n): 
    table =[0] * (n + 1)
    table[0] = 1
    for i in range(1, n): 
        for j in range(i , n + 1): 
            table[j] +=  table[j - i]  
    return table[n]+1
print(exp_sum(10))