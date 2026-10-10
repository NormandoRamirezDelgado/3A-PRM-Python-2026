'''Hacer un programa que resuelva lo siguiente.
En un negocio de abarrotes se esta ofreciendo la siguiente promoción debido a que le negocio esta en liquidación y cerra sus puertas, por ello cada producto tiene un decuento y son los siguientes:
- Frijol $20    - 20% descuento
- Arroz $18     - 10% descuento
- Leche $35     - 8.5% descuento
- Refresco $32  - 3% descuento
- Hariana $27   - 45% descuento
Para saber cuanto pagará el cliente pide los siguientes datos de cada producto de los mencionados deberás pedir la cantidad que se pidió, en base a la cantidad de productos deberas calcular el costo del producto.
Por cada venta deberas aplicar el descuento correspondiente y obtener lo que pagará por ese producto.
Calcular la suma total a liquidar de la venta.
Como resultado se desea saber cuanto pagará el cliente.
'''

frijol      = int(input('Cantidad comprada de Frijol: '))
arroz       = int(input('Cantidad comprada de Arroz: '))
leche       = int(input('Cantidad comprada de Leche: '))
refresco    = int(input('Cantidad comprada de Refresco: '))
harina      = int(input('Cantidad comprada de Harina: '))

totalFrijol = frijol * 20
totalArroz = frijol * 18
totalLeche = frijol * 35
totalRefresco = frijol * 32
totalHarina = frijol * 27

descuentoFrijol = totalFrijol * 0.20
descuentoArroz = totalArroz * 0.10
descuentoLeche = totalLeche * 0.085
descuentoRefresco = totalRefresco * 0.03
descuentoHarina = totalHarina * 0.45

ventaTotal = (totalFrijol - descuentoFrijol) + (totalArroz - descuentoArroz) + (totalLeche - descuentoLeche) + (totalHarina - descuentoHarina) + (totalRefresco - descuentoRefresco)

print(f'La Venta Total ya con Descuento es: ${ventaTotal:.2f}')
