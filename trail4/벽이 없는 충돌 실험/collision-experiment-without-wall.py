T = int(input())
V = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def meet(a, b):
    xa, ya, _, da, _ = a
    xb, yb, _, db, _ = b
    vxa, vya = V[da]
    vxb, vyb = V[db]
    t = None
    for dp, dv in ((xb - xa, vxa - vxb), (yb - ya, vya - vyb)):
        if dv == 0:
            if dp != 0:
                return None
        else:
            if dp % dv != 0:
                return None
            tt = dp // dv
            if tt <= 0:
                return None
            if t is not None and t != tt:
                return None
            t = tt
    return t

for _ in range(T):
    n = int(input())
    beads = []
    for idx in range(1, n + 1):
        x, y, w, d = input().split()
        # 좌표를 2배로 늘리면 1초에 1칸 이동
        beads.append((int(x) * 2, int(y) * 2, int(w), d, idx))

    events = {}
    for i in range(n):
        for j in range(i + 1, n):
            t = meet(beads[i], beads[j])
            if t is not None:
                events.setdefault(t, []).append((i, j))

    INF = float('inf')
    death = [INF] * n
    last = -1

    for t in sorted(events):
        groups = {}
        for i, j in events[t]:
            if death[i] >= t and death[j] >= t:
                for k in (i, j):
                    x, y, w, d, idx = beads[k]
                    vx, vy = V[d]
                    groups.setdefault((x + vx * t, y + vy * t), set()).add(k)
        for members in groups.values():
            if len(members) > 1:
                last = t
                winner = max(members, key=lambda k: (beads[k][2], beads[k][4]))
                for k in members:
                    if k != winner:
                        death[k] = t
    print(last)