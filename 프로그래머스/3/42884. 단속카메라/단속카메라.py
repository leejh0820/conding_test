def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30000
    
    for route in routes:
        start, end = route
        if start > camera:
            answer += 1
            camera = end
        
    return answer