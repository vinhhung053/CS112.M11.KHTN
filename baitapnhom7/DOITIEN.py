n,k = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a,reverse = True)

def sol1(k):
    cnt = 0
    i = 0
    while k > 0 and i < n:
        if (k >= a[i]):
            tmp = k//a[i]
            cnt += tmp
            k -= tmp*a[i]
        i+=1
    if k > 0: 
        cnt += 1
    return cnt
def sol2(k):
    cnt = 0
    if (k >= a[0]):
        tmp = k//a[0] - 1
        cnt += tmp
        k -= tmp*a[0]
    for i in range (0,n-1):
        for j in range(0,n-1):
            if a[i] + a[j] == k:
              return cnt + 2
    for i in range (0,n-1):
        for j in range(0,n-1):
            for h in range(0,n-1):
                if a[i] + a[j] + a[h] == k:
                    return cnt + 3
    return cnt + 4
def sol3(k):
    a.append(0)
    cuoi = min(n+1,5)
    a[cuoi - 1] = 0;
    mn = 10000000000
    for i1 in range(0,cuoi):
        for i2 in range(0,cuoi):
            for i3 in range(0,cuoi):
                for i4 in range(0,cuoi):
                    for i5 in range(0,cuoi):
                        for i6 in range(0,cuoi):
                            tong = a[i1] + a[i2] + a[i3] + a[i4] + a[i5] + a[i6]
                            d = (a[i1] != 0) + (a[i2] != 0) + (a[i3] != 0) + (a[i4] != 0) + (a[i5] != 0) + (a[i6] != 0)
                            if (k - tong) % a[0] == 0:
                                mn = min(mn, d + (k - tong)//a[0])
    return mn

print(min(sol1(k),sol2(k),sol3(k)))