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