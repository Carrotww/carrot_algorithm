# https://school.programmers.co.kr/learn/courses/30/lessons/133500
from collections import defaultdict, deque

def solution(n, lighthouse):
    path_dict = defaultdict(list)
    
    for a, b in lighthouse:
        path_dict[a].append(b)
        path_dict[b].append(a)
    
    # path_dict를 모두 돌면서 key의 value가 하나 있는 곳을 먼저 체크 한다.
    # 체크 한 후 path_dict에 존재하는지도 체크한다 - 없으면 물려있는 상대 노드에 관련있는
    # 모든 노드를 제거 한다.
    # result += 1을 한다
    
    result = 0
    while path_dict:
        for end_node, center_node in path_dict.items():
            if len(center_node) == 1: # val 이 중심, key 가 끝 노드
                del_val = [x for x in path_dict[center_node[0]]]
                print(del_val)
                break
        break
    return result

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))