print("Lista zakupów:")
shopping_dict = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

value_count = 0

for key, value in shopping_dict.items():
    print(f"Idę do {key}, kupuję tu następujące rzeczy: {value}")
    value_count += len(value)
    
print(f"W sumie kupuję {value_count} produktów.")
