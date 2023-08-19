print("Lista zakupów:")
shopping_dict = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

value_count = 0
shop_count = 0

for key, value in shopping_dict.items():
    print(f"Idę do {key}, kupuję tu następujące rzeczy: {value}")
    value_count += len(value)
    shop_count += 1
    
print(f"W sumie kupuję {value_count} produktów w {shop_count} sklepach.")
