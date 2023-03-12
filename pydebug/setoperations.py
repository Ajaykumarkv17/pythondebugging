n = int(input())
s = set(map(int, input().split()))
number = int(input())

for _ in range(number):
    c = list(input().split())
    if 'pop' in c[0]:
        s.pop()
    elif 'remove' in c[0]:
        s.remove(int(c[-1]))
    elif 'discard' in c[0]:
        s.discard(int(c[-1]))

print(sum(s))