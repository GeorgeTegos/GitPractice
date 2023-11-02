def can_pay(price, cash_given):
    try:
        if cash_given >= price:
            return True
        else:
            return False
    except TypeError as e:
        print(f"Wrong type input : {e}")
        return None

print(can_pay(5,'2'))