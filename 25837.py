def issquare(num):
    if num < 0:
        return False
    left = 0
    right = num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

T = int(input())
for _ in range(T):
    S, P = map(int, input().split())
    D = S**2 - P*4
    if issquare(D) is not False:
        if (S % 2) == (issquare(D) % 2):
            print('Yes')
        else:
            print('No')
    else:
        print('No')


"""
N + M = S

N * M = P

S - M = P / M

M^2 - SM + P = 0

-b +- sqrt(b^2 -4ac)/2a

S^2 -4P => 자연수

S +- sqrt(S^2 -4P) => 짝수

"""