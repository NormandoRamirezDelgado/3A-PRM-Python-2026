'''Hacer un programa que de una venta realizada le calcule el 20% de descuento e imprima como resultado el total a pagar por el cliente ya aplicándole el descuento obtenido.'''

venta = float(input('Cuál es el total de la venta? $'))

descuento = venta * 0.20

pagar = venta - descuento

print(f'Total a Pagar {pagar}')


