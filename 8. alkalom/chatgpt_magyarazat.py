global_variable = 10  # Globális változó a globális névtérben

def example_function():
    local_variable = 5  # Lokális változó a függvény hatókörében

    print(global_variable)  # Hozzáférünk a globális változóhoz a lokális hatókörben
    print(local_variable)   # Hozzáférünk a lokális változóhoz a lokális hatókörben

example_function()

print(global_variable)  # Hozzáférünk a globális változóhoz a globális hatókörben
# print(local_variable)  # Hiba! Nem tudunk hozzáférni a lokális változóhoz a globális hatókörben
