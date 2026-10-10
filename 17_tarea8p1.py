'''
Hacer un programa que basado en la compra realizada por un cliente y de acuerdo a dicha compra se le puede aplicar una promoción para que pague menos en su compra final.
Dichas promociones son las siguientes:
- Hasta $250.00 un descuento de 5%
- Hasta $700.00 un descuento del 8.5%
- Hasta $1,000.00 el descuento del 10%
- Superior a los $1,000 el 15% de descuento.
Imprimir como resultado el monto inicial de la venta, el descuento y el total final a pagar.
'''
compra = float(input('Total de la Compra: $'))

if compra <= 250.00:
    descuento = compra * 0.05
else: 
    if compra <= 700.00:
        descuento = compra * 0.085
    else:
        if compra <= 1000.00:
            descuento = compra * 0.10
        else:
            descuento = compra * 0.15
print(f'Monto Inicial de Compra: ${compra}')
print(f'Descuento obtenido: ${descuento}')
print(f'Moto Final a Pagar: ${compra - descuento}')