# Design Browser History

'''
인터넷에 브라우저에서 방문기록과 동일한 작동을 하는 BrowserHistory class를 구현할 것이다.
구현할 브라우저는 homepage에서 시작하고, 이후에는 다른 url에 방문할 수 있다.
또, "뒤로가기"와 "앞으로가기"가 작동하도록 구현하라.

- BrowserHistory(string homepage)를 호출하면 브라우저는 homepage에서 시작이 된다.
- void visit(string url)을 호출하면 현재 page의 앞에 있는 페이지 기록은 다 삭제가 되고 url로 방문을 한다.
- string back(int steps)을 호출하면 steps 수 만큼 "뒤로가기"를 한다. "뒤로가기"를 할 수 있는 page 개수가 x이고
  step > x 라면 x번만큼만 "뒤로가기" 한다. "뒤로가기"가 완료되면 현재 url을 return 한다.
- string forward(int steps)을 호출하면 steps 수 만큼 "앞으로가기"를 한다. "앞으로가기"를 할 수 있는 page 개수가 x이고
  step > x 라면 x번만큼만 "앞으로가기" 한다. "앞으로가기"가 완료되면 현재 url을 return 한다.

ex)
    Input :                                             Output :
    browserHistory = BrowserHistory("leetcode.com")     
    browserHistory.visit("google.com")                  None
    browserHistory.visit("facebook.com")                None
    browserHistory.visit("youtube.com")                 None
    browserHistory.back(1)                              "facebook.com"
    browserHistory.back(1)                              "google.com"
    browserHistory.forward(1)                           "facebook.com"
    browserHistory.visit("linkedin.com")                None
    rowserHistory.forward(2)                            "linkedin.com"
    browserHistory.back(2)                              "google.com"
    browserHistory.back(7)                              "leetcode.com"

제약조건
    1 <= homepage.length <= 20
    1 <= url.length <= 20
    1 <= steps <= 100
    homepage와 url은 '.'를 포함한 lower case 영어 문자로 구성되어 있다.
    visit, back 그리고 forward는 최대 5000번의 호출이 있을 수 있다.
'''

# ------------------------------------------------------------

'''
(2) 접근 방법
    순서가 있는 선형 자료구조 선택

    중간에 추가하기(visit)가 많이 발생한다면 linked list가 유리
    visit   - O(1)
    back    - O(n)
    forward - O(n)

    뒤로가기(back), 앞으로가기(forward)가 많이 발생한다면 array list가 유리
    visit   - O(n)
    back    - O(1)
    forward - O(1)
'''

# ------------------------------------------------------------

class ListNode(object):
    def __init__(self, data = 0, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.curr = ListNode(homepage)

    def visit(self, url):
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next
        return None

    def back(self, steps):
        while steps > 0 and self.curr.prev != None:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.data

    def forward(self, steps):
        while steps > 0 and self.curr.next != None:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.data
    
browserHistory = BrowserHistory("leetcode.com")
print(browserHistory.visit("google.com"))
print(browserHistory.visit("facebook.com"))
print(browserHistory.visit("youtube.com"))
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
print(browserHistory.visit("linkedin.com"))
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))
