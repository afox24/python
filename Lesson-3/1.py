def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не может быть нулем"
    except ValueError:
        return "введите число"
print(my_func(int(input("Введите x = ")), int(input("Введите y = "))))
