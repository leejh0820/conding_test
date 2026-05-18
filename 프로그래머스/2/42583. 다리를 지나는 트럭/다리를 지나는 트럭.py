from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    current_weight = 0
    
    while bridge:
        answer += 1
        current_weight -= bridge.popleft()
        
        if trucks:
            if current_weight + trucks[0] <= weight:
                next_truck = trucks.popleft()
                bridge.append(next_truck)
                current_weight += next_truck
            else:
                bridge.append(0)
    
    return answer