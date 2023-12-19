
numbers = input('Введите коэффиценты через проблем: ')
a, b, c = map(float, numbers.split())
D = b ** 2 - 4 * a * c

if D < 0:
    print('Нет корней')
    exit()

x1 = (-b + D ** 0.5) / (2 * a)
print(f'x₁ = {x1}')

if D > 0:
    x2 = (-b - D ** 0.5) / (2 * a)
    print(f'x₂ = {x2}')
