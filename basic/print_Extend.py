# Chapter02-1 extend1


"""
    Escape 코드
    
    \n : 개행
    \t : 텝
    \\, \", \' : 문자
    \000: null 문자
"""

### 3가지 format practices

x = 50
y = 100
text = 3082
n = "Choi"

# 출력 1
ex1 = "n = %s, s = %s, sum = %d" % (n, text, (x + y))
print(ex1)

# 출력 2
ex2 = "n = {n}, s = {s}, sum = {sum}".format(n=n, s=text, sum=x + y)
print(ex2)

# 출력 3
ex3 = f"n = {n}, s = {text}, sum = {x + y}"
print(ex3)
print()

# 구분 기호
m = 100000000

print(f"m: {m:,}")
print()

# 정렬
# ^: 가운데, <: 왼쪽, >: 오른쪽

t = 20

print(f"t: {t:10}")
print(f"t^: {t:^10}")
print(f"t<: {t:<10}")
print(f"t>: {t:>10}")
print()

print(f"t^: {t:-^4}")
