T=int(input())

for _ in range(T):

    n=int(input())

    
    
    input1=list(map(int,input().split()))
    input2=list(map(int,input().split()))
    data=[input1,input2]

    dp=[0]*(n+1)

    action_dp=[0]*(n+1)
    #3번쨰 전 최대값 + (n-2)+(n-1)+n의 최대값 = dp
    dp[0]=max(data[0][0],data[1][0])
    dp[1]=max(data[0][0]+data[1][1],data[1][0]+data[0][1])
    
    for i in range(2,n):

        #case1
        case1=data[1][i-2]+data[0][i-1]+data[1][i]
        #case2
        case2=data[0][i-2]+data[1][i-1]+data[0][i]
        #case2
        case3= max(data[0][i-2],data[1][i-2]) + max(data[0][i],data[1][i])
        # print(action_dp[i-2])
        if action_dp[i-2]=="up":
            case3 = data[0][i-2] + max(data[0][i],data[1][i])
            big= max(case2,case3)
        elif action_dp[i-2]=="down":
            case3 = data[1][i-2] + max(data[0][i],data[1][i])
            big = max(case1,case3)
        else:
            big = max(case1,case2)
            big= max(big,case3)

        if big==case1:
            action_dp[i-1]="up"
        if big==case2:
            action_dp[i-1]="down"
        if big==case3:
            action_dp[i-1]="no"

        if i==2:
            dp[i]=big
        else:
            dp[i]=dp[i-3]+big

    print(dp[n-1])
    