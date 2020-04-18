def getChunk(pattern, i):
    ''' gets the next chunk of the pattern, from index i to 
    either * or the end of the pattern'''
    if pattern[i] == '*':
        return '*'
    j = i
    while pattern[j] != '*':
        j += 1
        if j == len(pattern):
            break
    return pattern[i:j]

def matchChunk(chunk, pattern, i):
    if chunk == '*':
        return True 
    for j in range(len(chunk)):
        if pattern[i + j] != chunk[j]:
            return False
    return True

def combine(p1, p2):
    if p2[-1] == '*' and len(p1) > len(p2):
        new = [' '] * len(p1)
        new[:len(p2)] = p2
        new[len(p2): ] = '*' * (len(p1) - len(p2))
        p2 = ''.join(new)
    if len(p1) > len(p2):
        temp = p1
        p1 = p2
        p2 = temp 
    combined = ""
    if set(p2) == {'*'}:
        return '*'
    for i in range(len(p1)):
        if p1[i] == p2[i]:
            combined += p1[i]
        elif p1[i] == '*':
            combined += p2[i]
        elif p2[i] == '*':
            combined += p1[i]
        else:
            return "Something wrong"
    return combined

def findName(patterns, t):
    ans = ""
    patterns = sorted(patterns, key=len, reverse=True)
    print(patterns)
    while patterns: 
        curr = patterns[0]
        if not ans:
            ans = curr
        else:
            i = 0 # index for ans
            j = 0 # index for curr
            k = 0 # index for new_ans
            new_ans = [' '] * (len(ans) + len(curr))
            if ans[0] == '*' and curr[0] != '*':
                i += 1
            elif ans[0] != '*' and curr[0] == '*':
                j += 1
            while True:
                chunk = getChunk(curr, j)
                if matchChunk(chunk, ans, i):
                    new_ans[k:len(chunk)] = chunk
                    i += len(chunk)
                    j += len(chunk)
                    k += len(chunk)
                else:
                    i += 1
                    if k != 0 and new_ans[k-1] == '*':
                        new_ans[k] = '*'
                    k += 1
                if i == len(ans) or j == len(curr):
                    break
            new_ans = new_ans[:k]
            new_ans = ''.join(new_ans)
            ans = combine(ans, new_ans)
        patterns = patterns[1:]
    if ans != '*':
        ans = ans.replace('*', '')
    output = "Case #{}: {}".format(t+1, ans)
    return output

T = int(input())
for t in range(T):
    N = int(input())
    patterns = []
    for n in range(N):
        patterns.append(input())
    print(findName(patterns, t))
    #print(getChunk(patterns[0], 1))