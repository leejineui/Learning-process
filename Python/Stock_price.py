




def solution(prices):
    n = len(prices)
    # 1. answer를 리스트의 길이와 맞춘다. (리스트의 길이의 숫자만큼 시도할 것이기 때문에)
    answer = [0] * n
    # 2. 스택 생성 ====> 주식가격이 떨어지지 않을 시간을 저장하는 것 
    st = []
    # 3. 0 ~ n-1 초까지 순회
    
    for i in range(n):
        
        # 4. 스택 비지 않고, prices[top] > prices[i] 이라면 현재의 가격이 바로전 가격보다 떨어졌을 경우 다음 반복

        while st and prices[st[-1]] > prices[i]:  
            top = st.pop()   # 스택에서 마지막에 저장된 시간 top 꺼냄  ==> 여기서 top 은 바로전에 저장된 시간 를 의미한다. 
            answer[top] = i - top 
            # answer[top]에 i - top을 저장 ===>i-top 은 현재시간(지금의 index)에서 바로전 전의시간(index 넘버 값)을 빼는 것 즉 얼마나 벼텼는지==> 버틴시간을 top index에 해당하는 것에 지정해준다.
        
        st.append(i)  # 5. prices[st[-1]] <= prices[i] 이라면 지금 가격이 전의 가격보다 떨어지지 않았으므로 현재 price[i] 의 값을 저장한다==> 후에 시간저장 개념
    
    # 6. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while st:
        
        top = st.pop() # 스택에서 마지막에 저장된 시간 top 꺼냄
        answer[top] = n - 1 - top  # n 번 차이지만 3 번째에서 한 번 빠졌으므로 -1을 해준다 즉 (전체시간) - top (저장된 시간) = 전체시간 -저장된 시간 = 버틴시간
    
    return answer

print(solution([1,2,3,2,3]))



def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            answer[i] += 1

            if prices[i] > prices[j]:
                break
        
    return answer

print(solution([1,2,3,2,3]))