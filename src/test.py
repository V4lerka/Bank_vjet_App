from src.masks import get_mask_account, get_mask_card_number

result_card_number = get_mask_card_number(input("Введите номер карты: "))
print(result_card_number)

result_account_number = get_mask_account(input("Введите номер счета: "))
print(result_account_number)
