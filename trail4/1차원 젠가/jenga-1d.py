n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

new_blocks = []

# 첫번째 작업
new_blocks = blocks[:s1 - 1] + blocks[e1:]
    
# 두번째 작업 
new_blocks = new_blocks[:s2 - 1] + new_blocks[e2:]

print(len(new_blocks))
for block in new_blocks:
    print(block)