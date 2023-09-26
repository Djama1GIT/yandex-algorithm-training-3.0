inf = float('inf')


def cafe(count_of_days: int, price_list: list[int]) -> tuple[int, int, int, list[int]]:
    price_list: list[int] = [0] + price_list
    table: list[list[int | float]] = [[-1] * (count_of_days + 2) for _ in range(count_of_days + 1)]

    def calculate(day: int, coupon: int) -> int | float:
        if table[day][coupon] != -1:
            return table[day][coupon]
        if coupon > day:
            return inf
        else:
            if coupon == 0:
                if day == 0:
                    result = 0
                else:
                    if price_list[day] <= 100:
                        result = min(calculate(day - 1, coupon + 1), calculate(day - 1, coupon) + price_list[day])
                    else:
                        result = calculate(day - 1, coupon + 1)
            else:
                if price_list[day] <= 100:
                    result = min(calculate(day - 1, coupon + 1), calculate(day - 1, coupon) + price_list[day])
                else:
                    result = min(calculate(day - 1, coupon + 1), calculate(day - 1, coupon - 1) + price_list[day])

        table[day][coupon] = result
        return result

    for i in range(count_of_days + 1):
        calculate(count_of_days, i)

    minimum: int | float = inf
    count_of_unused_coupons: int | float = inf
    for unused_coupons in range(count_of_days + 1):
        if table[-1][unused_coupons] <= minimum:
            minimum = table[-1][unused_coupons]
            count_of_unused_coupons = unused_coupons

    recovery: list[int] = []

    def _recovery(day: int, coupon: int) -> None:
        if day > coupon:
            if coupon == 0:
                if table[day][coupon] == table[day - 1][coupon + 1]:
                    recovery.append(day)
                    _recovery(day - 1, coupon + 1)
                else:
                    _recovery(day - 1, coupon)
            else:
                if table[day][coupon] == table[day - 1][coupon + 1]:
                    recovery.append(day)
                    _recovery(day - 1, coupon + 1)
                else:
                    if price_list[day] <= 100:
                        _recovery(day - 1, coupon)
                    else:
                        _recovery(day - 1, coupon - 1)

    _recovery(count_of_days, count_of_unused_coupons)

    return minimum, count_of_unused_coupons, len(recovery), list(reversed(recovery))


minim, k1, k2, K2 = cafe(cnt_of_days := int(input()), [int(input()) for _ in range(cnt_of_days)])

print(minim)
print(k1, k2)
[print(day_of_coupon_usage) for day_of_coupon_usage in K2]
