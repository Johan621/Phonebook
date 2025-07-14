def add_contacts(contacts):
    
    ''' 
        Used to Add contacts with name and phone numbers 
        as the input from the users.
    '''
    
    name = input("Enter contact name : ")
    if not name:
        print("Name cannot be empty.")
        return
    ph_num = input("Enter 10-digit number : +91 ")
    if not (ph_num.isdigit() and len(ph_num) == 10):
        print("Enter a valid 10-digit number.")
        return
    if name in contacts:
        print(f"Contact '{name}' already exists!!")
    else:
        contacts[name] = ph_num
        print(f"Contact '{name}' added successfully!")
        
def search_contacts(contacts):
    
    '''
        Used to search the contact number by providing the input as the contact name
        if it does exists then it will show you the phone number.
    '''
    name = input("Enter contact name to search : ")
    if not name:
        print("Invalid input - Provide a name")
        return
    if name in contacts:
        print(f"Contact '{name}' has phone number : +91 {contacts[name]}")
    else:
        print("Contact not found!")
    
def delete_contacts(contacts):
    
    '''
        Delete's the contact from phonebook contact list 
        using the name provided by the user. 
    '''
    name = input("Enter contact name you want to delete : ")
    if not name:
        print("Invalid input.")
        return
    if name in contacts:
        del contacts[name]
        print("Contact deleted Successfully.")
    else:
        print("Contact does not exists.")
        
def view_contacts(contacts):
    
    '''
        View contacts is used to display the dictionary items 
        containing {key:value} pairs.   
    '''
    if not contacts:
        print("No contacts exists use option 1 to 'Add contact'")
        return
    print("----- Contacts Lists -----\n")
    print("Names\t\tPhone number")
    print("----\t\t------------")
    for name,ph_num in contacts.items():
        print(f"{name}\t\t+91 {ph_num}\n")

def main():
    contacts = {}
    while True:
        print("\nWelcome to phonebook!!")
        print("Choose any one option provided below:\n")
        print("1. Add Contacts\n2. Search Contacts\n3. Delete Contacts\n4. Display Contacts\n5. Exit")
        option = input("Enter the option number : ")
        if option == '1':
            add_contacts(contacts)
        elif option == '2':
            search_contacts(contacts)
        elif option == '3':
            delete_contacts(contacts)
        elif option == '4':
            view_contacts(contacts)
        elif option == '5':
            print("Thank you for using the app")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()