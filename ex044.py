pr = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
o = int(input('Qual é a opção? '))
if o == 1:
    d = pr * 10 / 100
    print('Sua compra terá 10% de desconto!\nSua compra de R${:.2f} irá custar R${:.2f} no final!'.format(pr, pr - d))
elif o == 2:
    d = pr * 5 / 100
    print('Sua compra terá 5% de desconto!\nSua compra de R${:.2f} irá custar R${:.2f} no final!'.format(pr, pr - d))
elif o == 3:
    total = pr
    pa = pr/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS\nSua compra de R${:.2f} irá custar R${:.2f} no final!'.format(pa, pr, total))
elif o == 4:
    totpar = int(input('Quantas parcelas? '))
    total = pr + (pr * 20 /100)
    pa = pr / totpar
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS\nSua compra de {:.2f} vai custar {:.2f} no final'.format(totpar, pa, pr, total))
else:
    print('Opção inválida')

