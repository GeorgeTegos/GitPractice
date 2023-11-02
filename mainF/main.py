def add(a, b):
    try:
        result = a+b
        return result
    except Exception as e:
        print(f"Error {e}")
        return None

def subtract(a,b):
    return a-b

result = add(3,"2")

print("test")

