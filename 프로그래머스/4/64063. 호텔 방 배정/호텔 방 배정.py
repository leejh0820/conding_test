from collections import deque

def solution(k, room_number):
    answer = []
    rooms = {}
    
    for num in room_number:
        visit_path = deque()
        curr = num
        
        while curr in rooms:
            visit_path.append(curr)
            curr = rooms[curr]
            
        answer.append(curr)
        rooms[curr] = curr + 1
        
        while visit_path:
            rooms[visit_path.popleft()] = curr + 1
            
    return answer