class InvalidFlavour(Exception): pass

def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 40, "lemon": 30}
    try:
        if flavour not in menu:
            raise InvalidFlavour("Selected flavour we are not serving...")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be in integer...")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai: {total}Rs/-")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank You for Visiting Chaiwala...")

bill("masala", 20)
bill("ginger", "two")
bill("lemoon", 10)