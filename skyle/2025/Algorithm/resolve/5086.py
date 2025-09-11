# 5086

### My Solution
```python
import sys

while True:
    a,b = map(int, sys.stdin.readline().strip().split())
    if a==0 and b==0:
        break
    elif a<b and b%a == 0:
        print("factor")
    elif a>b and a%b == 0:
        print("multiple")
    else :
        print("neither")
```
