#Dashiell Wendt 2033998
class ItemToPurchase:
    
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, str(self.item_quantity), 
            str(self.item_price), str( self.item_price * self.item_quantity)))

if __name__ == "__main__":
    # Type main section of code here
    print("Item 1")
    product1 = ItemToPurchase()
    product2 = ItemToPurchase()
    product1.item_name = input('Enter the item name:\n')
    product1.item_price = int(input('Enter the item price:\n'))
    product1.item_quantity = int(input('Enter the item quantity:\n'))
    
    print("\nItem 2")
    product2.item_name = input('Enter the item name:\n')
    product2.item_price = int(input('Enter the item price:\n'))
    product2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")
    product1.print_item_cost()
    product2.print_item_cost()
    total = (product1.item_price*product1.item_quantity)+(product2.item_price * product2.item_quantity)

    print("\nTotal: $" + str(total))