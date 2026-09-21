def ingreso_total(precio_libro, cantidad_vendida):
    return precio_libro * cantidad_vendida


def cumple_meta(ingreso_total):
    if ingreso_total >= 10_000_000:
        return "Cumple"
    else:
        return "No cumple"


def comparar_ventas(ingreso_novelas, ingreso_comics):
    if ingreso_novelas > ingreso_comics:
        return "Novelas tuvo mayores ingresos"
    elif ingreso_comics > ingreso_novelas:
        return "Comics tuvo mayores ingresos"
    else:
        return "Novelas y Comics tuvieron los mismos ingresos"


if __name__ == "__main__":
    casos = [
        (150_000, 80),
        (57_000, 200),
        (60_000, 150),
    ]

    print("Precio del libro | Cantidad vendida | Ingreso total | Meta")
    ingresos = []
    for precio, cantidad in casos:
        total = ingreso_total(precio, cantidad)
        ingresos.append(total)
        print(f"{precio} | {cantidad} | {total} | {cumple_meta(total)}")

    print()
    print("Comparación novelas vs comics:")
    print(comparar_ventas(ingresos[0], ingresos[1]))
