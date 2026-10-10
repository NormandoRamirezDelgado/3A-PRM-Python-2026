'''
Hacer un programa que basado en la venta realizada al cliente le podamos aplicar una promoción que actualmente se tiene y es la siguiente:
- Si la venta es mayor a $500.00 se le aplica el 10% de descuento
- De lo contrario solo obtiene el 5% de descuento.
Imprimir como resultado la cantidad obtenida de descuento o promoción y la cantidad final a pagar por el cliente.
'''
venta = float(input('Monto de la Venta: $'))

if venta > 500:
    descuento = venta * 0.10
else:
    descuento = venta * 0.05
    
totalPagar = venta - descuento

print(f'El Descuento es de: ${descuento:.2f}')
print(f'Cantidad A Pagar: ${totalPagar:.2f}')





