# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
raio = float(input("insira o valor do raio: "))
def calcular_area_base():
    area = (3.14*raio**2)
    return area 
ver_area = calcular_area_base()
print(ver_area)

altura = float(input("digite o a altura do cilindro: "))
def calcular_volume_cilindro():
    volume = 3.14*raio*2*altura
    return volume
ver_volume = calcular_volume_cilindro()
print(ver_volume)

