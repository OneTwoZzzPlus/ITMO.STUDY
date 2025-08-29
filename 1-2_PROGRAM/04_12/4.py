def control_sum(s: str) -> str:
    """
    Считает контрольную сумму СНИЛС
    :param s: Первые 9 цифр СНИЛС
    :return: контрольная сумма
    """
    su = sum(int(s[i]) * (9 - i) for i in range(9))
    if su < 100:
        return str(su)
    elif su == 100 or su == 101:
        return "00"
    elif (su % 101) < 100:
        return str(su % 101)
    else:
        return "00"


def validate(s: str) -> bool:
    """
    Проверяет СНИЛС на корректность
    :param s: СНИЛС
    :return: корректно или нет
    """
    if len(s) != 11 or not s.isdigit():  # СНИЛС неправильной длины или не из цифр
        return False
    for i in range(0, 7):
        if s[i] == s[i + 1] == s[i + 2]:  # Есть 3 одинаковые цифры подряд
            return False
    if control_sum(s[:10]) != s[9:]:  # Контрольная сумма не совпадает
        return False
    return True


print("СНИЛС правильный!" if validate(input('СНИЛС > ')) else "СНИЛС неправильный!")
