n = int(input("Введите количество школьников, которые будут делить яблоки (n): "))
k = int(input("Введите количество яблок, которые будут делить школьники (k): "))
apples = k // n
rem = k - (apples * n)
print(f"Каждому школьнику достанется {apples} яблок. При этом в корзине останется {rem} яблок.")