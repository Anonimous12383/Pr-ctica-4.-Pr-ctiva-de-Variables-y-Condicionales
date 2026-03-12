# ----- CONSTANTES -----
TSS = 0.0591        # 5.91% Seguridad Social (TSS)
ISR = 0.0835        # ISR aproximado (ejemplo: 8.35% para simular cálculo real)
DOBLE_SUELDO = 1    # equivalente a un sueldo adicional
BONIFICACION = 0.10 # 10% del sueldo bruto (simplificado)

print("==============================================================")
print("        CALCULA TU SUELDO PA' QUE NO SE TE LIQUIDEN  (RD$)   ")
print("==============================================================")

# ----- ENTRADA DE DATOS -----
nombre = input("Ingrese el nombre del empleado: ")
antiguedad = int(input("¿Cuántos años lleva en la empresa?: "))
sueldo_bruto = float(input("Digite el sueldo bruto mensual (RD$): "))

# Validación
if sueldo_bruto <= 0:
    print("Error: el sueldo debe ser mayor que 0")
    exit()

otros_descuentos = float(input("Digite otros descuentos (RD$, si no hay escriba 0): "))

respuesta_bonificacion = input("¿Aplica bonificación? (si/no): ").lower()
respuesta_doble = input("¿Aplica doble sueldo? (si/no): ").lower()

# ----- CALCULOS -----
descuento_tss = sueldo_bruto * TSS
descuento_isr = sueldo_bruto * ISR

# Bonificación según antigüedad
if respuesta_bonificacion == "si":
    bonificacion = sueldo_bruto * BONIFICACION
else:
    bonificacion = 0

# Doble sueldo
doble_sueldo = sueldo_bruto * DOBLE_SUELDO if respuesta_doble == "si" else 0

# Sueldo neto
sueldo_neto = sueldo_bruto - descuento_tss - descuento_isr - otros_descuentos + bonificacion + doble_sueldo

# ----- RESULTADOS -----
print("====================================")
print("\n Detalle del cálculo del sueldo ")
print("====================================")
print(f"Empleado: {nombre}")
print(f"Años en la empresa: {antiguedad}")
print(f"Sueldo Bruto: RD${sueldo_bruto:,.2f}")
print(f"Descuento Seguridad Social (TSS): RD${descuento_tss:,.2f}")
print(f"Descuento ISR (DGII): RD${descuento_isr:,.2f}")
print(f"Otros Descuentos: RD${otros_descuentos:,.2f}")
print(f"Bonificación: RD${bonificacion:,.2f}")
print(f"Doble Sueldo: RD${doble_sueldo:,.2f}")
print("------------------------------")
print(f"Sueldo Neto: RD${sueldo_neto:,.2f}")
print("------------------------------")