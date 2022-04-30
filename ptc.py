from collections import deque
n = int(input())
Deque = deque()
for i in range(n):
    mathod = input().split()
    if(mathod[0] == 'append'):
        Deque.append(int(mathod[1]))    
    elif(mathod[0] == 'appendleft'):
        Deque.appendleft(int(mathod[1]))
    elif(mathod[0] == 'pop'):
        Deque.pop()
    elif(mathod[0] == 'popleft'):
        Deque.popleft()
for i in Deque:
    print(i, end=' ')