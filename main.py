from converter import convert, currencies
import time
def get_valid_amount() -> float:
    while True:
        amount_input = input("Введите сумму: ").strip()
        cleaned = amount_input.replace(".", "", 1).lstrip("-")
        if cleaned and cleaned.isdigit():
            return float(amount_input)
        print("Введите корректное число ")

def get_valid_currency(prompt: str) -> str:
    while True:
        curr = input(prompt).strip().upper()
        if curr in currencies:
            return curr
        print(f"Неверная валюта, доступные валюты: {', '.join(currencies)}, введите корректную валюту ")

def main():
    print("Доступные валюты:", ", ".join(currencies))

    amount = get_valid_amount()
    from_curr = get_valid_currency("Из какой валюты: ")
    to_curr = get_valid_currency("В какую валюту: ")

    result = convert(amount, from_curr, to_curr)

    if result is None:
        print("Не удалось выполнить конвертацию")
    else:
        print(f"{amount} {from_curr} = {result:.2f} {to_curr}")

if __name__ == "__main__":
    main()

time.sleep(8)
