def solution(enroll, referral, seller, amount):
    parent = {}
    profit = {}
    
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        profit[enroll[i]] = 0
        
    for i in range(len(seller)):
        current_seller = seller[i]
        money = amount[i] * 100
        
        while current_seller != "-" and money > 0:
            send = money // 10
            mine = money - send
            
            profit[current_seller] += mine
            
            current_seller = parent[current_seller]
            money = send
            
    answer = [profit[name] for name in enroll]
    return answer