INF = float('inf')


def cafe(count_of_days: int, price_list: list) -> tuple[int | float, int, int, list[int]]:
    """
    Данная функция решает задачу "Кафе":

    Около Петиного университета недавно открылось новое кафе, в котором действует следующая система скидок:
    при каждой покупке более чем на 100 рублей покупатель получает купон, дающий право на один бесплатный обед
    (при покупке на сумму 100 рублей и меньше такой купон покупатель не получает).
    Однажды Пете на глаза попался прейскурант на ближайшие N дней. Внимательно его изучив, он решил,
    что будет обедать в этом кафе все N дней, причем каждый день он будет покупать в кафе ровно один обед.
    Однако стипендия у Пети небольшая, и поэтому он хочет по максимуму использовать
    предоставляемую систему скидок так, чтобы его суммарные затраты были минимальны.
    Требуется найти минимально возможную суммарную стоимость обедов и номера дней,
    в которые Пете следует воспользоваться купонами.

    Формат ввода
    В первой строке входного файла записано целое число N (0 ≤ N ≤ 100).
    В каждой из последующих N строк записано одно целое число,
    обозначающее стоимость обеда в рублях на соответствующий день.
    Стоимость — неотрицательное целое число, не превосходящее 300.

    Формат вывода
    В первой строке выдайте минимальную возможную суммарную стоимость обедов.
    Во второй строке выдайте два числа K1 и K2 — количество купонов,
    которые останутся неиспользованными у Пети после этих N дней и количество использованных им купонов соответственно.
    В последующих K2 строках выдайте в возрастающем порядке номера дней,
    когда Пете следует воспользоваться купонами.
    Если существует несколько решений с минимальной суммарной стоимостью, то выдайте то из них,
    в котором значение K1 максимально (на случай, если Петя когда-нибудь ещё решит заглянуть в это кафе).
    Если таких решений несколько, выведите любое из них.


    :param count_of_days: Количество дней
    :param price_list: Список содержащий стоимость обеда в рублях на соответствующие дни
    minimum: Минимальная возможная суммарную стоимость обедов.
    K1: Количество неиспользованных купонов.
    K2: Количество использованных купонов.
    *K2 строк: Номера дней, когда Пете следует воспользоваться купонами.
    :return: minimum, K1, K2, *K2
    """
    # После долгого времени проведенном над этой задачей, могу сделать выводы, что нужно учитывать и т.д.
    # 1. Сначала пишем базу
    # 2. Потом краевые случаи
    # 2.1 Сначала чекаем параметр внутреннего цикла (купоны)
    # 2.2 Проверяем параметр внешнего цикла (дни)
    # 3. Обязательно должны быть учтены случаи выхода за предел возможных данных: -1 купон, max+1 день и подобное
    # 4. Действовать нужно аккуратно, не торопиться и всё обдумывать
    # 5. Для параметров разной природы лучше использовать рекурсию

    price_list = [0] + price_list
    # инициализация таблицы динамики
    table = [[-1] * (count_of_days + 2) for _ in range(count_of_days + 1)]

    def calculate(day, coupon):
        """
        Находим наименьшую сумму для комбинации день - количество оставшихся купонов
        :param day:
        :param coupon:
        :return:
        """
        if coupon > day:
            # Если количество купонов > количества дней, то возвращаем INF, т.к. такое невозможно
            return INF
        else:
            # иначе:
            if table[day][coupon] != -1:
                # если значение уже вычислено, то не делаем повторных вычислений
                return table[day][coupon]
            # делаем проверку на наличие купонов
            if coupon == 0:
                # Если купонов нет, то в алгоритме есть отличие от алгоритма, когда купоны есть: мы не проверяем
                # (day - 1, coupon - 1), т.к. отрицательного количества купонов быть у нас не может
                if day > 0:
                    # Делаем проверку, что день не нулевой, иначе возвращаем 0, т.к. в нулевой день не было трат
                    if price_list[day] <= 100:
                        # Если сегодня мы не получили купон, то проверяем вчерашний день с количеством купонов на
                        # 1 больше, что значит, что сегодня мы потратили купон, а так же с таким же количеством.
                        # (Это как если бы мы не потратили купон).
                        result = min(calculate(day - 1, coupon + 1), calculate(day - 1, coupon) + price_list[day])
                    else:
                        # Если же мы можем получить купон, то возвращаем значение вчерашнего дня с +1 купоном
                        # что значит, что мы потратили купон.
                        # Почему так? Дело в том, что мы не можем иметь 0 купонов никак иначе в таком дне.
                        # У нас два пути: потратить купон, и сумма будет как вчера с купоном + 1
                        # или купить еду без купона, и в таком случае у нас будет 1 купон, а не 0.
                        result = calculate(day - 1, coupon + 1)
                else:
                    # если день нулевой, то возвращаем 0
                    result = 0
            else:
                # Если купонов больше, чем 1, то день у нас 100% не первый, так что тут всё базово
                if price_list[day] <= 100:
                    # Минимум вычисляется по 2 числам.
                    # Мы либо потратили купон, либо нет и потратили деньги и у нас такое же количество купонов
                    # т.к. прайс <= 100
                    result = min(calculate(day - 1, coupon + 1), calculate(day - 1, coupon) + price_list[day])
                else:
                    # Мы либо потратили купон, либо нет и потратили деньги и у нас на 1 больше количество купонов
                    # чем вчера, т.к. прайс > 100
                    result = min(calculate(day - 1, coupon + 1), calculate(day - 1, coupon - 1) + price_list[day])
        table[day][coupon] = result
        return result

    # запуск динамики
    for coupons in range(count_of_days + 1):
        calculate(count_of_days, coupons)

    # отображение таблицы динамики
    # for idx, row in enumerate(table):
    #     print(f"{idx + 1:>2}) {price_list[idx]:>3} | ", end=' ')
    #     for elem in row:
    #         print(f"{elem:>5}", end='')
    #     print()

    minimum = INF
    count_of_unused_coupons = INF
    for unused_coupons, summ in enumerate(table[-1]):
        if summ not in [-1, INF]:
            if minimum >= summ:
                count_of_unused_coupons = unused_coupons
                minimum = summ

    recovery = []

    def _recovery(day, coupon):
        """
        Восстанавливаем ответ для комбинации день - количество оставшихся купонов
        :param day:
        :param coupon:
        :return:
        """
        if coupon < day:
            # Чекаем, возможность ситуации, купонов не может быть больше, чем количества дней
            if coupon == 0:
                # если купонов 0, то проверка одним образом, если больше, то другим
                if day > 0:
                    # если день нулевой, то мы уже все восстановили, иначе чекаем
                    if price_list[day] <= 100:
                        # если прайс меньше ста, то значит, если у нас 0 купонов, что мы либо потратили купон
                        # сегодня, либо нет, и проверяем мы в соответствии с этим
                        if calculate(day - 1, coupon + 1) == calculate(day, coupon):  # проверяем потратили ли мы купон
                            # вчера было на 1 больше, проверяем для этой комбинации
                            recovery.append(day)
                            _recovery(day - 1, coupon + 1)
                        else:
                            # если мы сегодня не потратили купон, то кол-во купонов не изменилось
                            # продолжаем восстановление ответа
                            _recovery(day - 1, coupon)
                    else:
                        # если прайс больше ста, то 0 купонов может быть только если мы сегодня потратили купон
                        recovery.append(day)
                        _recovery(day - 1, coupon + 1)
            else:
                # если купонов больше 0, то действуем базово
                if calculate(day - 1, coupon + 1) == calculate(day, coupon):  # если потратили купон
                    recovery.append(day)
                    _recovery(day - 1, coupon + 1)  # продолжаем восстановление
                else:  # если не потратили купон
                    _recovery(day - 1, coupon - (1 if (price_list[day] > 100) else 0))
                    # продолжаем восстановление, учитывая прайс

    _recovery(count_of_days, count_of_unused_coupons)  # запускаем восстановление

    return minimum, count_of_unused_coupons, len(recovery), list(reversed(recovery))


minim, k1, k2, K2 = cafe(cnt_of_days := int(input()), [int(input()) for _ in range(cnt_of_days)])

print(minim)
print(k1, k2)
[print(day_of_coupon_usage) for day_of_coupon_usage in K2]
# if __name__ == '__main__':
#     assert cafe(5, [35, 40, 101, 59, 63]) == (235, 0, 1, [5]) or print(cafe(5, [35, 40, 101, 59, 63]))
#     print()
#     assert cafe(1, [300]) == (300, 1, 0, [])
#     print()
#     assert cafe(
#         22,
#         [171, 177, 83, 184, 131, 47, 182, 93, 41, 35, 65, 72, 106, 161, 0, 167, 200, 49, 103, 0, 101, 58]
#     ) == (1299, 0, 6, [4, 7, 8, 16, 17, 21]) or print(cafe(
#         22,
#         [171, 177, 83, 184, 131, 47, 182, 93, 41, 35, 65, 72, 106, 161, 0, 167, 200, 49, 103, 0, 101, 58]
#     ))
