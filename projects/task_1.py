"""
This is a project for Beckett Pizza Plaza that is running a 4-for-3 offer.
This is an interactive program that runs on CLI.
The functions in this project are modular and reusable with different offers and systems.
"""


def price(pz_num):
    """
    Prompts the user to enter a valid pizza price.
    Ensures the input provided(price) is a positive number.
    Repeats the prompt until valid input is provided.
    """
    while True:
        try:
            print("-------------------------------------")
            price = float(input(f"Enter the price for Pizza number#{pz_num}:"))
            print("-------------------------------------")
            if price <= 0:
                print("*****************************")
                print("PLEASE ENTER A VALID PRICE!!!")
                print("*****************************")
            else:
                return price
        except ValueError:
            print("*****************************")
            print("PLEASE ENTER A VALID INPUT!!!")
            print("*****************************")


def offer():
    """
    Calculates the total price for the four pizzas using 4-for-3 discount offer.
    Displays the final total with the discount percentage.
    """
    print("===============================")
    print("Welcome to Beckett Pizza Plaza!")
    print("===============================")
    print("Beckett Pizza Plaza 4-for-3 Offer")
    prices = []
    for i in range(1, 5):
        prices.append(price(i))
    original_total = sum(prices)
    cheapest_pz = min(prices)
    offer_total = original_total - cheapest_pz
    discount = original_total - offer_total
    discount_percent = (discount / original_total) * 100
    print("======================================================")
    print(
        f"Your total today is \u00a3{offer_total:.2f} after a discount of {discount_percent:.0f}%!!!"
    )
    print("======================================================")


if __name__ == "__main__":
    offer()
