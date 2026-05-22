# ============================================
# MENÚ DE RESTAURANTE - PROBLEMA 2
# ============================================
# MATRIZ DEL MENÚ
menu = [
    ["Sopa de miso", "Comida", 12000],
    ["Domburi", "Comida", 18000],
    ["Sushi", "Comida", 20000],
    ["Rasume", "Bebida", 14000],
    ["Sake", "Bebida", 18000],
    ["Dorayaki", "Postre", 12000],
    ["Helado de té verde (Matcha)", "Postre", 10000]
]
# REGLAS DE DESCUENTO
categoria_objetivo = ["Comida", "Postre"]
umbral_precio = 25000
# PEDIDO DEL CLIENTE
pedido = []
# ============================================
# FUNCIÓN DE DESCUENTO
# ============================================

def calcular_precio_final(categoria, precio):
    if categoria in categoria_objetivo and precio > umbral_precio:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        descuento = 0
        precio_final = precio
    return descuento, precio_final
# CONTROL DEL CICLO
continuar = "si"
# ============================================
# PROCESO DE COMPRA
# ============================================
while continuar == "si":
    print("\n===================================")
    print("      MENÚ DEL RESTAURANTE")
    print("===================================")
    contador = 1

    for producto in menu:
        print(
            contador,
            "-",
            producto[0],
            "-",
            producto[1],
            "-",
            producto[2],
            "COP"
        )

        contador += 1
    # SELECCIÓN DEL PRODUCTO
    opcion = int(input("\nIngrese el número del producto que desea ordenar: "))
    if opcion >= 1 and opcion <= len(menu):
        producto_seleccionado = menu[opcion - 1]
        # VALIDACIÓN DE CANTIDAD
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad que desea ordenar: "))
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser mayor a 0.")
            except ValueError:
                print("Error: debe ingresar solo números positivos.")
        # GUARDAR EN EL PEDIDO
        pedido.append([producto_seleccionado, cantidad])
        print("Producto agregado correctamente.")

    else:
        print("Opción inválida.")
    # CONTINUAR COMPRA
    continuar = input("\n¿Desea ordenar otro producto? (si/no): ").lower()
    while continuar != "si" and continuar != "no":
        print("Ingrese solo 'si' o 'no'")
        continuar = input("¿Desea ordenar otro producto? (si/no): ").lower()
# ============================================
# FACTURA FINAL
# ============================================
print("\n===================================")
print("         FACTURA FINAL")
print("===================================")

total_general = 0
for item in pedido:

    producto = item[0]
    cantidad = item[1]

    nombre = producto[0]
    categoria = producto[1]
    precio = producto[2]

    descuento, precio_final = calcular_precio_final(categoria, precio)

    subtotal = precio_final * cantidad
    total_general += subtotal

    print("\n-----------------------------------")
    print("Producto:", nombre)
    print("Tipo:", categoria)
    print("Cantidad:", cantidad)
    print("Precio por unidad:", precio, "COP")
    print("Descuento por unidad:", descuento, "COP")
    print("Precio final por unidad:", precio_final, "COP")
    print("Subtotal (producto x cantidad):", subtotal, "COP")

print("\n===================================")
print("TOTAL A PAGAR:", total_general, "COP")
print("===================================")