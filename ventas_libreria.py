def ingreso_total(precio_libro, cantidad_vendida):
    return precio_libro * cantidad_vendida


def cumple_meta(ingreso_total):
    if ingreso_total >= 10000000:
        return "Cumple"
    else:
        return "No cumple"


total1 = ingreso_total(150000, 80)
print(total1, cumple_meta(total1))

total2 = ingreso_total(57000, 200)
print(total2, cumple_meta(total2))

total3 = ingreso_total(60000, 150)
print(total3, cumple_meta(total3))
