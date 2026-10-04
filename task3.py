# Дан словарь. Поменяйте местами ключи и значения.

# Дано:

# countries = {
#     "BY": "Belarus",
#     "PL": "Poland",
#     "DE": "Germany",
#     "FR": "France",
#     "ES": "Spain"
# }
# Результат:

# {
#     "Belarus": "BY",
#     "Poland": "PL",
#     "Germany": "DE",
#     "France": "FR",
#     "Spain": "ES"
# }

countries = {
    "BY": "Belarus",
    "PL": "Poland",
    "DE": "Germany",
    "FR": "France",
    "ES": "Spain"
}

keys = countries.keys()
values = countries.values()

result = dict(values, keys)

print(result)