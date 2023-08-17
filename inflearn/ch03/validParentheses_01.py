# Valid Parentheses

'''
'() {} []'를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오.

ex)
    Input: s = ")("
    Output: false

    Input: s = "([]}"
    Output: false

    Input: s = "{()[]}"
    Output: true

제약조건
    1 <= s.length <= 10^4
    문자열 s는 '()[]{}'의 괄호들로만 구성되어 있다.

'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    1 <= s.length <= 10^4 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    스택 자료구조 사용

(3) 코드 설계
    stack = []

    for p in s
        if  p == '({['
            stack.append(')}]')
        if p == ')}]'
            # 스택이 비어있다면 닫는 괄호가 더 많은 것이므로 False 리턴
            # pop한 괄호가 p와 다르다면 짝이 다른 것이므로 False 리턴
            if stack.isEmpty || stack.pop() != p
                return F

    # 반복문이 다 끝났는데 스택에 괄호가 남아있다면 여는 괄호가 더 많은 것이므로 False 리턴
    # 스택이 비어있다면 짝도 맞고 개수도 맞는 것이므로 True 리턴
    if stack.isEmpty
        T
    else
        F
    
(4) 코드 구현
'''

# ------------------------------------------------------------

def isValid(s):
    stack = []

    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    
    return not stack

print(isValid(")("))
print(isValid("([]}"))
print(isValid("{()[]}"))
