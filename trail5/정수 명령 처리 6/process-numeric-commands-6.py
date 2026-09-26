import heapq

n = int(input())
max_heap = []

for _ in range(n):
    command = input().split()
    cmd = command[0]

    if cmd == 'push':
        val = int(command[1])
        # 파이썬 heapq는 Min-Heap이므로 음수로 변환하여 저장
        heapq.heappush(max_heap, -val)
    elif cmd == 'pop':
        # 가장 작은 음수를 꺼낸 뒤 다시 양수로 반환하면 최댓값이 됨
        print(-heapq.heappop(max_heap))
    elif cmd == 'size':
        print(len(max_heap))
    elif cmd == 'empty':
        print(1 if not max_heap else 0)
    elif cmd == 'top':
        # 힙의 루트 원소(-최댓값)를 확인
        print(-max_heap[0])



