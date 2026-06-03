class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    TAX_RATE = 0.18  # 18% GST

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0
        for product in self.products:
            subtotal += product.get_total()
        return subtotal

    def calculate_tax(self):
        return self.calculate_subtotal() * self.TAX_RATE

    def calculate_final_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n" + "=" * 60)
        print("                BILLING SYSTEM")
        print("=" * 60)

        print(f"{'Product':15}{'Price':10}{'Qty':10}{'Amount':10}")
        print("-" * 60)

        for product in self.products:
            print(
                f"{product.name:15}"
                f"{product.price:<10}"
                f"{product.quantity:<10}"
                f"{product.get_total():<10}"
            )

        print("-" * 60)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_final_total()

        print(f"{'Subtotal:':40} ₹{subtotal:.2f}")
        print(f"{'GST (18%):':40} ₹{tax:.2f}")
        print(f"{'Final Total:':40} ₹{total:.2f}")
        print("=" * 60)


# Main Program
bill = Bill()

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details of Product {i+1}")

    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = Product(name, price, quantity)
    bill.add_product(product)

bill.display_bill()