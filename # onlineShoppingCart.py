# onlineShoppingCart
# Module 6

# Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

# Define the ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item):
        item_found = False
        for existing_item in self.cart_items:
            if existing_item.item_name == item.item_name:
                existing_item.item_price = item.item_price if item.item_price != 0 else existing_item.item_price
                existing_item.item_quantity = item.item_quantity if item.item_quantity != 0 else existing_item.item_quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            total_cost = 0
            for item in self.cart_items:
                item.print_item_cost()
                total_cost += item.item_price * item.item_quantity
            print(f"Total: ${total_cost}")
    
    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Item Descriptions:")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_name} description here.")

# Main section to interact with the user
def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    
if __name__ == "__main__":
    # Initialize shopping cart
    customer_name = input("Enter customer name: ")
    current_date = input("Enter today's date: ")
    shopping_cart = ShoppingCart(customer_name, current_date)
    
    while True:
        print_menu()
        choice = input("Choose an option: ").lower()
        
        if choice == 'a':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity)
            shopping_cart.add_item(item)
        
        elif choice == 'r':
            item_name = input("Enter item name to remove: ")
            shopping_cart.remove_item(item_name)
        
        elif choice == 'c':
            item_name = input("Enter item name to modify: ")
            item_price = float(input("Enter new item price (enter 0 to keep the same): "))
            item_quantity = int(input("Enter new item quantity (enter 0 to keep the same): "))
            item = ItemToPurchase(item_name, item_price, item_quantity)
            shopping_cart.modify_item(item)
        
        elif choice == 'i':
            shopping_cart.print_descriptions()
        
        elif choice == 'o':
            shopping_cart.print_total()
        
        elif choice == 'q':
            break
        else:
            print("Invalid option. Please choose again.")
