# Chapter02-1

# sep option
print("p", "y", "t", "h", "o", "n", sep="|")

# end option
print("Welcome to", end=" ")
print("IT News", end=" ")
print("Web Site", end=" ")

# file option
import sys

print("Learn Pyton", file=sys.stdout)
print()


# format 사용(d, s, f)
# d = 정수, s = 문자열, f = float

print("%s %s" % ("one", "two"))
print("{} {}".format("one", 2))

# index
print("{1} {0}".format("one", "two"))

# f
ONE = "one"
TWO = "two"
print(f"{ONE} {TWO}")
print()

# %s - 남는 공간은 첫번째 부터 공백
print("%10s" % "nice")
print("{:>10}".format("nice"))

print(f"{'nice':>10}")
print()

# 음수인 경우 오른쪽 부터 공백
print("%-10s" % "nice")
print("{:10}".format("nice"))

print(f"{'nice':<10}")
print(f"{'nice':10}")
print()

print("{:_>10s}".format("nice"))
print(f"{'nice':_>10s}")

# 중앙 정렬 ^
print("{:_^10s}".format("nice"))
print(f"{'nice':_^10s}")
print()

# 절삭
print("%.5s" % ("pythonStudy"))
print(f"{'pythonStudy'[:5]}")
print()

print("{:10.5}".format("pythonStudy"))
print(f"{'pythonStudy':10.5}")
print()

# %d
print("%d %d" % (1, 2))
print(f"{1} {2}")

print("%4d" % (42))
print("{:4d}".format(42))

# %f
print("%1.18f" % 3.141412421421)
print("{:f}".format(3.1314214214215))
print()

print("%06.2f" % (3.1415926535243243241))
print(f"{3.1415923424:06.2f}")
