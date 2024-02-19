# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius

def celsius_para_fahrenheit(temperatura_celsius):
    fahrenheit = (temperatura_celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input('Enter with temperature in Celsius: '))

temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

print(f'Temperature {temperatura_celsius} C in Fahrenheit is {temperatura_fahrenheit} F')