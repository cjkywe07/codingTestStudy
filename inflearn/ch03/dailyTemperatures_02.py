# Daily Temperatures

'''
매일의 온도를 나타내는 int형 배열 temperatures가 주어진다.
answer 배열의 원소 answer[i]에는 i번째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야 하는지 나타낸다.
만약 더 따뜻해지는 날이 없다면 answer[i] == 0 이다. answer 배열을 반환하는 함수를 구현하시오.

ex)
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

    Input: temperatures = [30,60,90]
    Output: [1,1,0]

제약조건
    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100

'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    1 <= temperatures.length <= 10^5 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    스택 자료구조 사용

(3) 코드 설계
    answer = [0] * len
    stack = []

    for t in temperatures
        while stack.isNotEmpty && stack[-1] < t
            stack.pop()
            answer[pop한 값 idx] = t와 pop한 값 idx 차이
        stack.append(t)

    return answer

(4) 코드 구현
'''

# ------------------------------------------------------------

def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day = stack.pop()[0]
            answer[prev_day] = cur_day - prev_day
            
        stack.append((cur_day, cur_temp))

    return answer

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
# print(dailyTemperatures([73,71,69,67,72]))
