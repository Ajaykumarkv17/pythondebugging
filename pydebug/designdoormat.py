n, m = map(int, input().split())
N, M = map(int, input().split())
txt = "WELCOME"
# top
for i in range(1, n, 2):
    print((i*".|.").center(m, "-"))
# center
print(txt.center(m, '-'))
# bottom
for i in range(n-2, 0, -2):
    print((i*".|.").center(m, "-"))

for i in range(1, N, 2):
    print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')
print(((M-7)//2)*'-'+'WELCOME'+((M-7)//2)*'-')
for i in range(N-2, -1, -2):
    print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')
