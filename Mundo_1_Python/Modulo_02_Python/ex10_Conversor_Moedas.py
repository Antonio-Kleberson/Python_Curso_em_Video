#Crie um programa que receba um valor em reais e convertar para dolar, euro e libra.

from forex_python.converter import CurrencyRates

def converter_moeda(valor_brl):
    c = CurrencyRates()

    valor_usd = c.convert('BRL', 'USD', valor_brl)
    valor_eur = c.convert('BRL', 'EUR', valor_brl)
    valor_gbp = c.convert('BRL', 'GBP', valor_brl)

    return valor_usd, valor_eur, valor_gbp

def main():
    valor_brl = float(input('Quantos reais você tem? R$'))
    
    valor_usd, valor_eur, valor_gbp = converter_moeda(valor_brl)
    
    print('DOLAR: ${:.2f}'.format(valor_usd))
    print('EURO: €{:.2f}'.format(valor_eur))
    print('LIBRA: £{:.2f}'.format(valor_gbp))

if __name__ == "__main__":
    main()