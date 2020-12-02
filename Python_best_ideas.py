def prime_numbers_lower_than_a_number(n):
    return(list(filter(lambda x: int(x) > 1 and (x == 2 or x == 3 or [x % i == 0 for i in range(2,int(x**0.5)+1)].count(True) == 0)
    ,[i for i in range(int(n))])))
