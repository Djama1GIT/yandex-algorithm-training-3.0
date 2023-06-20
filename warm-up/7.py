from datetime import timedelta

A = list(map(int, input().split(':')))
B = list(map(int, input().split(':')))
C = list(map(int, input().split(':')))
result = ((timedelta(days=1 if C[0] < A[0] else 0)) +
          timedelta(hours=C[0], minutes=C[1], seconds=C[2]) -
          timedelta(hours=A[0], minutes=A[1], seconds=A[2])) / 2 + \
         timedelta(hours=B[0], minutes=B[1], seconds=B[2])
ms = result.microseconds
if ms != 0:
    if ms >= 500000:
        result += timedelta(microseconds=(1000000 - ms))
    else:
        result -= timedelta(microseconds=ms)
print(f"{result.seconds // 60 // 60:02}:{result.seconds // 60 % 60:02}:{result.seconds % 60:02}")
