
def common_character_count(s1,s2):
    all_letter=set(s1+s2)
    # count=0
    n=list()
    for letter in all_letter:
        n.append([letter,s1.count(letter),s2.count(letter)])
    
        # if 0 not in n:
        #     count+=sum(n)//2
        

    return n


print(common_character_count("bccc","aaabcd"))