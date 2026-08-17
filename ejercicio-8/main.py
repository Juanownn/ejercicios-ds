def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    precio_final = precio_base * (1 - porcentaje_descuento/100)
    if es_vip:
        precio_final = precio_final * 0.95
    return precio_final

if __name__ == "__main__":
    precio_ini = int(input("Ingresa el valor del producto: "))
    es_vip = input("Es usuario vip?: ('SI' si es): ") == "SI"
    tiene_desc = input("Tiene descuento especifico?: ('SI' si es): ") == "SI"
    if tiene_desc:
        desc = int(input("Ingrese el descuento: "))
        print(f"El precio final es: {calcular_precio_final(precio_ini,desc,es_vip)}")
    else:
        print(f"El precio final es: {calcular_precio_final(precio_ini,es_vip=es_vip)}")