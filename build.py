def solution(l):
    e=len(list(filter(lambda x:x%2==0,l)))
    o=len(l)-e
    return {'ODD':o,'EVEN':e}

print(solution([1, 2, 3, 5, 8, 9]))
l=[1, 2, 3, 5, 8, 9]
h=list(filter(lambda x:x%2==0,l))
print(h)
