def len_num(n):
    len_count = 0
    while n > 0:
        len_count+=1
        n = n // 10
    return len_count

def is_palindrome(number):
    original_num = number
    reverse_num = 0
    while number > 0:
        mod = number % 10
        reverse_num = reverse_num * 10 + mod
        number = number // 10
        
    return reverse_num == original_num

def pl_of_none_pl(number):
    original_num = temp_num = number
    n = len_original_num = len_num(number)
    first_half_part = 0
    
    if n%2==0:
        n=n/2
    else:
        n=(n//2)+1
    l=0    
    while number > 0:
        
        mod = number % 10
        if l >= n:
            first_half_part = first_half_part * 10 + mod
        if len_original_num % 2 != 0:
            if l < n-1:
                temp_num = temp_num // 10
        else:
            if l < n:
                temp_num = temp_num //10
                
        number = number // 10
        l += 1 

    temp_num = temp_num * ( 10 ** ( len_original_num // 2 ) )
    return temp_num + first_half_part