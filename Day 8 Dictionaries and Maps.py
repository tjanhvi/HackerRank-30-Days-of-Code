n = int(input())
d = {}
for i in range(n):
    s = input().split()
    d[s[0]] = s[1]


while True:
    try:
        s = input()
        if s in d:
            print(f"{s}={d[s]}")
        else:
            print("Not found")
    
    except:
        break