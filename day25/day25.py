snafus = open("input.txt").read().split("\n")


def snafu_to_dec(snafu):
    snafu = [*snafu]
    dec = 0
    i = 1
    while snafu:
        n = snafu.pop()
        if n == '2':
            dec += 2 * i
        elif n == '1':
            dec += i
        elif n == '0':
            dec += 0
        elif n == '-':
            dec -= i
        elif n == '=':
            dec -= 2 * i
        i *= 5
    return dec


fuel = sum(snafu_to_dec(snafu) for snafu in snafus)


def dec_to_snafu(dec):
    if dec == 0:
        return ""
    if dec % 5 == 0:
        return dec_to_snafu(dec // 5) + "0"
    if dec % 5 == 1:
        return dec_to_snafu(dec // 5) + "1"
    if dec % 5 == 2:
        return dec_to_snafu(dec // 5) + "2"
    if dec % 5 == 3:
        return dec_to_snafu((2 + dec) // 5) + "="
    if dec % 5 == 4:
        return dec_to_snafu((1 + dec) // 5) + "-"


print(dec_to_snafu(fuel))
