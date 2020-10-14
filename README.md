# AlphaLab-Hackerearth-Test

## 1. Number of drawdown for stock market
```
def calc_drawdowns(prcs, N):
    peak = float('-inf')
    trough = float('inf')
    drawdowns = []
    for i in range(len(prcs)):
        if prcs[i] > peak:
            if trough != float('inf'):
                drawdowns.append(peak - trough)
                trough = float('inf')
            peak = prcs[i]
        else: # drawdown
            trough = min(trough, prcs[i])
    drawdowns.sort(reverse = True)
    if len(drawdowns) == 0:
        print('None')
    if N >= len(drawdowns):    
        print(*drawdowns)
    else:
        drawdowns = drawdowns[:N]
        print(*drawdowns)
    

x = int(input()) # number of input followed
array1 = []
array2 = []

for i in range(x):
    P = input()
    P = P.split(' ')
    P =[int(p) for p in P]
    array1.append(P)
    N = int(input())
    array2.append(N)

for i, prcs in enumerate(array1):
    N = array2[i]
    calc_drawdowns(prcs, N)
    
# 1
# 1 2 3 4 5 7
# 3
# None
```

## 2. Sum of each digit is sum, number of digit is n
```
def findNDigitNumsUtil(n, sum, out, index, result):  
    if index > n or sum < 0: 
        return
    
    if index == n: 
        if sum == 0: 
            f = "" 
            for i in out: 
                f = f + str(i) 
            result.append(f) 
        return
  
    for i in range(10):  
        out[index] = i
        findNDigitNumsUtil(n, sum - i, out, index + 1, result) 

def findNDigitNums(sum, n): 
    out = [0] * (n) 
    result = []
    for i in range(1, 10): 
        out[0] = i
        findNDigitNumsUtil(n, sum - i, out, 1, result) 
    print(*result)
      
sum, n = list(map(int,input().rstrip().split()))
findNDigitNums(sum, n) 

# 7 3
# 106 115 124 133 142 151 160 205 214 223 232 241 250 304 313 322 331 340 403 412 421 430 502 511 520 601 610 700
```

## 3. Simple matching machine
#### SUB juhb B foo 10 450
#### SUB bpjl B foo 7 500
#### SUB lpqn B foo 10 1000
#### SUB jyfu S foo 10 1200
#### SUB zqcu S foo 15 400
#### CXL zqcu
#### END
<br>

### after order lpqn, the OB is 
### B: ['450@10#juhb', '1000@l0#pqn', '500@7#bpjl']
### S: []
### after order jyfu. the OB is 
### B: ['250@l0#pqn', '500@7#bpjl']
### S: []
<br>

## Result of my code:
```
SUB juhb B foo 10 450
B: ['450@10#juhb']
S: []
SUB bpjl B foo 7 500
B: ['450@10#juhb', '500@7#bpjl']
S: []
SUB lpqn B foo 10 1000
B: ['450@10#juhb', '1000@10#lpqn', '500@7#bpjl']
S: []
SUB jyfu S foo 10 1200
B: ['250@10#lpqn', '500@7#bpjl']
S: []
SUB zqcu S foo 15 400
B: ['250@10#lpqn', '500@7#bpjl']
S: ['400@15#zqcu']
CXL zqcu
B: ['250@10#lpqn', '500@7#bpjl']
S: []
END
```
