def calcular_cashback(valor_compra, desconto, is_vip):
    # 1. Aplicar desconto
    valor_final = valor_compra * (1 - desconto)

    # 2. Cashback base (5%)
    cashback = valor_final * 0.05

    # 3. Promoção: dobra cashback se valor > 500
    if is_vip:
        cashback += cashback * 0.10

    # 4. Bônus VIP (10% sobre o cashback)
    if valor_final >= 500:
        cashback *= 2

    return round(cashback, 2)