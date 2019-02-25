def division(a,b):
    try:
        return a/b
    except ZeroDivisionError :
        return "Zero division"

print(division(1,0))
