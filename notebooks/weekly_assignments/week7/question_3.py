"""This program manages a list of countries and their capital cities.
If the capital city for the entered country already exists in the list the function prints it
but if it doesn't it asks the user to enter it and this keeps repeating until the user enters quit.
"""


def capital_dic():
    capitals = {
        "nepal": "Kathmandu",
        "india": "New Delhi",
        "wales": "Cardiff",
        "france": "Paris",
    }
    print("Country and It's Capital")
    print("========================")
    while True:
        country = input("Enter a country: ").strip().lower()
        if country == "quit":
            print("Bye Bye!!!")
            break
        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country]}.")
        else:
            print("Data Not Found!")
            capital = input(f"Please enter the capital of {country.title()}: ").strip()
            capitals[country] = capital
            print("Data updated!!!")
            print(f"{country.title()}:{capital}")


capital_dic()
