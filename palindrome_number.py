def len_num(n):
    len_count = 0
    while n > 0:
        len_count+=1
        n = n // 10
    return len_count