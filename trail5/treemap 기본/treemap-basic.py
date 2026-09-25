from sortedcontainers import SortedDict

n = int(input())

sd = SortedDict()

for _ in range(n):
    query = input().split()
    cmd = query[0]

    if cmd == "add":
        k, v = int(query[1]), int(query[2])
        sd[k] = v
        
    elif cmd == "remove":
        k = int(query[1])
        del sd[k]
        
    elif cmd == "find":
        k = int(query[1])
        if k in sd:
            print(sd[k])
        else:
            print("None")
            
    elif cmd == "print_list":
        if not sd:
            print("None")
        else:
            # SortedDict의 values()는 키 오름차순 순서로 정렬된 값들의 뷰를 반환합니다.
            print(*(sd.values()))