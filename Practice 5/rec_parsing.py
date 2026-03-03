import re
import json

with open("Practice 5/raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

parsed_data = {
    "products": [],
    "prices": [],
    "total": None,
    "date_time": None,
    "payment_method": None
}

# Prices
price_pattern = r'\d[\d\s]*,\d{2}'
parsed_data["prices"] = re.findall(price_pattern, text)

# Products
product_pattern = r'\d+\.\n(.+)'
parsed_data["products"] = re.findall(product_pattern, text)

# Total
total_pattern = r'ИТОГО:\n([\d\s]+,\d{2})'
total_match = re.search(total_pattern, text)
if total_match:
    parsed_data["total"] = total_match.group(1)

# Date
date_pattern = r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}'
date_match = re.search(date_pattern, text)
if date_match:
    parsed_data["date_time"] = date_match.group()

# Payment
payment_pattern = r'Банковская карта|Наличные'
payment_match = re.search(payment_pattern, text)
if payment_match:
    parsed_data["payment_method"] = payment_match.group()

print(json.dumps(parsed_data, indent=4, ensure_ascii=False))