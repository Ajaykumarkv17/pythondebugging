from collections import Counter

if __name__ == '__main__':
    a=input()

    l=sorted(list(a))

    c=Counter(l)
    mc=c.most_common(4)

    for a,b in mc:
        print(f'{a} {b}')