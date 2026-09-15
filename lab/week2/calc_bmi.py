def calc_bmi(cm, kg):
    return f"{kg / (cm / 100) ** 2:.2f}"

def test():
    cm, kg = map(int, input().split())
    print(calc_bmi(cm, kg))

test()