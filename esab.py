import sys

def query(B):
    ans = [0] * B
    nquery = 1
    pos = 1
    while pos <= B:
        print(pos)
        sys.stdout.flush()
        x = input()
        ans[pos-1] = x
        if nquery % 10 == 1: 
            pos -= 1
        pos += 1
        nquery += 1
    print(''.join(ans))
    sys.stdout.flush()
    return 

[T, B] = map(int, input().split())
for t in range(T):
    query(B)
    result = input()
sys.exit(0)
