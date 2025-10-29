from math import sqrt

def triangle_info(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return "Всички страни трябва да са положителни числа."

    
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        s = perimeter / 2  
        area = sqrt(s * (s - a) * (s - b) * (s - c))  
        
        result = (
            f"Страните {a}, {b}, {c} могат да образуват триъгълник.\n"
            f"Периметърът е: {perimeter:.2f}\n"
            f"Лицето е: {area:.2f}"
        )
        return result
    else:
        return "a, b, c НЕ могат да образуват триъгълник."


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))


print(triangle_info(a, b, c))
