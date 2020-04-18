def nesting(S, num):
    snum = [int(char) for char in S]
    sout = ""
    brackets = 0
    for i in range(len(snum)):
        sout += (snum[i] - brackets) * "(" + S[i]
        brackets += (snum[i] - brackets)
        if i < len(snum)-1:
            if snum[i+1] < snum[i]:
                sout += ")" * (snum[i] - snum[i+1])
                brackets -= (snum[i] - snum[i+1])
    sout += brackets * ")"
        
    output = "Case #{}: {}".format(num+1, sout)
    return output

t = int(input()) # test cases
for num in range(t):
    S = input()
    print(nesting(S, num))