# makine llogaritese

# ky funksion shton 2 numra
def add(x, y):
    return x + y

# ky funksion zbret 2 numra
def subtract(x, y):
    return x - y

# ky funksion shumezon 2 numra
def multiply(x, y):
    return x * y

# ky funksion pjeston 2 numra
def divide(x, y):
    return x / y


print("Zgjidh operatorin.")
print("1.Mblidh")
print("2.Zbrit")
print("3.Shumezo")
print("4.Pjesto")

while True:
    # Merr input nga useri
    choice = input("Vendos zgjidhjen(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Vendos numrin e pare: "))
        num2 = float(input("Vendos numrin e dyte: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
