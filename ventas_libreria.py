def ingreso_total(precio_libro, cantidad_vendida):
    return precio_libro * cantidad_vendida


def cumple_meta(ingreso_total):
    if ingreso_total >= 10000000:
        return "Cumple"
    else:
        return "No cumple"


precio_comic = 57000
precio_novela = 150000

total_comic = ingreso_total(precio_comic, 200)
print(total_comic, cumple_meta(total_comic))

total_novela = ingreso_total(precio_novela, 80)
print(total_novela, cumple_meta(total_novela))
