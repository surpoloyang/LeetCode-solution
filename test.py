def mySqrt(x: int) -> int:
    left = 0
    right = x//2
    while left < right:
        mid = (right-left)//2 + left
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            right = mid-1
        else:
            left = mid+1
    return -1
mySqrt(int(input()))