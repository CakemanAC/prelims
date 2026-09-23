#had to hardcode, sorry Dr.

USD_TO_EUR_RATE = 0.93
 
product_names = ["Product A", "Product B", "Product C", "Product D", "Product E", "Product F"]
product_prices_usd = [19.99, 45.50, 12.75, 89.00, 5.25, 150.00]
 
print("PRODUCT PRICE CONVERTER (USD to EUR)")
print("=" * 45)
print(f"{'Product':<12}{'Price (USD)':<15}{'Price (EUR)':<15}")
print("-" * 45)
 
for index in range(len(product_names)):
    price_in_usd = product_prices_usd[index]
    price_in_eur = price_in_usd * USD_TO_EUR_RATE
    print(f"{product_names[index]:<12}${price_in_usd:<14.2f}€{price_in_eur:<14.2f}")