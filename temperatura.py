escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if escala == 'f':
    f = float(input("Digite a temperatura em Fahrenheit: "))
    celcius = (f - 32) * (5 / 9)
    print(f"Temperatura equivalente em Celsius: {celcius:.2f}")
elif escala == 'c':
    c = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (c * (9 / 5)) + 32
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}")