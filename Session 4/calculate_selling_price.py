class CosmeticItem:
    def __init__(self, name, variants, prices):
        self.name = name
        self.variants = variants
        self.prices = prices

# Markup Percentage is 10% or 0.10

    def calculate_selling_price(self):
        selling_prices = []
        for price in self.prices:
            selling_price = price + (price * 0.10)
            selling_prices.append(selling_price)
        return selling_prices

def main():
    cosmetic_items = [
        CosmeticItem("Eye Shadow", ["Matte", "Powder"], [10000, 15000]),
        CosmeticItem("Lipstick", ["Matte", "Glossy"], [55000, 70000]),
        CosmeticItem("Powder", ["Compact", "Loose"], [75000, 85000]),
    ]

    for item in cosmetic_items:
        print(f"Item: {item.name}")
        print("Variants:", item.variants)
        print("Original Prices:", item.prices)
        print("Selling Prices:", item.calculate_selling_price())
        print()

if __name__ == "__main__":
    main()