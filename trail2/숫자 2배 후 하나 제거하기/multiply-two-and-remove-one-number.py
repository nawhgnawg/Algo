n = int(input())
arr = list(map(int, input().split()))

min_sum = float('inf')

# i: 2배를 할 인덱스 
for i in range(n):
    # j: 제거를 할 인덱스
    for j in range(n):
        # 새로운 리스트 구성
        temp_list = []
        for k in range(n):
            if k == j:  # 제거할 인덱스는 건너뜀
                continue
            
            val = arr[k]
            if k == i:
                val *= 2
            temp_list.append(val)
        
        # 인접한 원소 간의 차이를 합산
        curr_sum = 0
        for l in range(len(temp_list) - 1):
            curr_sum += abs(temp_list[l + 1] - temp_list[l])
    
        # 최솟값 갱신
        min_sum = min(min_sum, curr_sum)

print(min_sum)