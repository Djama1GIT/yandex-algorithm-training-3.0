n = int(input())
k = int(input())
row = int(input())
left_or_right = int(input())

seat = row * 2 - (2 if left_or_right == 1 else 1)

rear_seat = seat + k
front_seat = seat - k

if rear_seat >= n and front_seat < 0:
    print(-1)
else:
    rear_row = (rear_seat + 2) // 2
    front_row = (front_seat + 2) // 2
    rear_left_or_right = 2 if rear_seat % 2 == 1 else 1
    front_left_or_right = 2 if front_seat % 2 == 1 else 1

    if rear_seat >= n:
        print(front_row, front_left_or_right)
    elif front_seat < 0:
        print(rear_row, rear_left_or_right)
    elif rear_row - row > row - front_row:
        print(front_row, front_left_or_right)
    else:
        print(rear_row, rear_left_or_right)