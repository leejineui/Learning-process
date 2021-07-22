'''프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2] '''


def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: # 1.progresses 와 speeds* time 의 값이 100 되지 않는 시 time만 + 시킨다. 
            progresses.pop(0)                       # 2.time 이 증가하여 100%를 채우면 해당하는 progresses 와 speeds 값을 제외 시키고 count를 +1 한다.
            speeds.pop(0)                           # 3.다음항이 설정된 progresses(다음항) + speeds* time(전의 time) 의 값이 100 되면 count +1을 한 번 더하고 아닐 경우   
            count += 1
            
        else:                                      
            if count > 0:                           # 4. 현재 쌓인 count의 갯수를 answer 에 올리고 count 는 다시 0 으로 지정한다. 
                answer.append(count)                # 5. 다시 1~4 를 반복하여 일정 time 에 같이 끝낼 수 있는 일을 count로 묶어 올린다. 
                count = 0                           # 6. 모든 progresses의 항을 다 정리 하면 return 값이 나옴. 
            time += 1
    answer.append(count)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))