def add(a, b):
    try:
        result = a + b
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def subtract(a, b):
    try:
        result = a - b
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def multiply(a, b):
    try:
        if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
            result = a * b
            return result
        else:
            return TypeError
    except Exception as e:
        print(f"Error:{e}")
        return None

def divide(a, b):
    try:
        result = a / b
        return result
    except Exception as e:
        print(f"Error:{e}")
        return None
