def calcular_cashback(valor_compra, desconto, is_vip):
    # 1. Aplicar desconto
    valor_final = valor_compra * (1 - desconto)

    # 2. Cashback base (5%)
    cashback = valor_final * 0.05

       # 3. Bônus VIP: aumento de 10% no cashback base
    if is_vip:
        cashback += cashback * 0.10

    # 4. Promoção: cashback é dobrado para compras acima de R$ 500
    if valor_final >= 500:
        cashback *= 2

    #5. Arredonda resultado final para 2 casas decimais
    return round(cashback, 2)