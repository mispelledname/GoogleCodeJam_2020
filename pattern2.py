def check(ans, curr):
    for i in range(1, len(curr)+1):
        if curr[-i] != ans[-i]:
            return False
    return True
    
def findName(patterns, t):
    patterns = sorted(patterns, key=len, reverse=True)
    patterns = [x[1:] for x in patterns]
    ans = patterns[0]
    patterns = patterns[1:]
    while patterns:
        curr = patterns[0]
        if not check(ans, curr):
            ans = '*'
            break
        patterns = patterns[1:]
    output = "Case #{}: {}".format(t+1, ans)
    return output

T = int(input())
for t in range(T):
    N = int(input())
    patterns = []
    for n in range(N):
        patterns.append(input())
    print(findName(patterns, t))