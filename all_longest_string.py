def all_long(arr):
    longest=[len(x) for x in arr]
    longest=[arr[x] for x,v in enumerate(longest) if v==max(longest)]
    return longest

all_long(["aba", "aa", "ad", "vcd", "aba"])