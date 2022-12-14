
import functools


def compare(a,b):
    if a < b:
        return -1 #pull to lower index
    elif a > b:
        return 1 #push to higher index
    else:
        return 0

arr = [1,3,5,1,5,9]
arr.sort(key=functools.cmp_to_key(compare))
print(arr)
    