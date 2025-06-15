class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total spent per category
    spent = []
    for cat in categories:
        total_withdraw = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(total_withdraw)
    total_spent = sum(spent)
    # Calculate percentages rounded down to nearest 10
    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    # Build chart
    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        line = str(level).rjust(3) + "|"
        for perc in percentages:
            line += " o " if perc >= level else "   "
        chart += line + " \n"

    # Dashes line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            chart += line + "\n"
        else:
            chart += line
    return chart


# Example usage and demonstration
if __name__ == "__main__":
    # Create categories
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    # Perform transactions
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    food.transfer(50, clothing)

    clothing.withdraw(25.55, "shirt")
    clothing.deposit(100, "gift")

    auto.deposit(500, "car maintenance")
    auto.withdraw(150, "engine repair")

    # Print ledgers and balances
    print(food)
    print()
    print(clothing)
    print()
    print(auto)
    print()
    # Print spend chart
    print(create_spend_chart([food, clothing, auto]))