from api import get_rates

currencies = ["RUB", "USD", "EUR", "JPY", "CNY"]

rates = get_rates()

def convert(amount: float, from_curr: str, to_curr: str) -> float:
    froms = from_curr.upper()
    to = to_curr.upper()

    #print(f"[proverka] Курсы, которые пришли: {list(rates.keys())}")
    print(f"[proverka] Ищем: {froms} и {to}")

    if froms not in rates:
        print(f"[proverka] Нет курса для {froms}")
        return None
    if to not in rates:
        print(f"[proverka] Нет курса для {to}")
        return None

    amount_in_usd = amount / rates[froms]
    result = amount_in_usd * rates[to]
    return result
