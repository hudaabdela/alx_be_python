shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1.Add Item")
    print("2.Remove Item")
    print("3.View List")
    print("4.Exit")
def main() :
    shopping_list = []
    while True :
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1" : 
            a = input("Enter the item to add: ")
            shopping_list.append(a)
        elif choice == "2" :
            y = input("Remove item : ")
            shopping_list.remove(y)
        elif choice == "3" :
            for v in shopping_list:
                print(f"-{v}")
        elif choice == "4" :
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

