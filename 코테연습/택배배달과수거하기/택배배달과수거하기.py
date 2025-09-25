def update(box,cap):
    while len(box):
        if cap<box[-1]:
            box[-1]-=cap
            break
        else:
            cap -= box[-1]
            box.pop()
            
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while len(deliveries) or len(pickups):
        while len(deliveries) and deliveries[-1]==0:
            deliveries.pop()
        while len(pickups) and pickups[-1]==0:
            pickups.pop()
            
        answer += max(len(deliveries),len(pickups))*2
        
        update(deliveries,cap)
        update(pickups,cap)
        
    
    return answer