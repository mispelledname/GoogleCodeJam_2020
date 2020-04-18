def check(acts, start, end):
    for [s, e] in acts:
        activity = set(range(s,e))
        new = set(range(start,end))
        if activity.intersection(new):
            return False
    return True
    

def solve(schedule, x):
    with_index = schedule
    with_index = [with_index[i] + [i] for i in range(len(with_index))]
    sorted_index = sorted(with_index)

    cact = []
    jact = []
    ans = [" "] * len(schedule)

    for [start, end, index] in sorted_index:
        cfree = jfree = True
        if cact and not check(cact, start, end):
            cfree = False
        if jact and not check(jact, start, end):
            jfree = False

        if cfree:
            ans[index] = "C"
            cact.append([start, end])
        elif jfree:
            ans[index] = "J"
            jact.append([start, end])
        else:
            ans = "IMPOSSIBLE"
            break
    
    if ans != "IMPOSSIBLE":
        ans = "".join(ans)

    output = "Case #{}: {}".format(x+1, ans)
    return(output)

T = int(input()) # test cases
for x in range(T):
    N = int(input()) # number of activities
    schedule = []
    for y in range(N):
        schedule.append([int(x) for x in input().split()])
    print(solve(schedule, x))