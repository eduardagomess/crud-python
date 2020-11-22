import json

print("Option 1: Insert a contact")
print("Option 2: Remove a contact")
print("Option 3: Search a contact")
print("Option 4: List all the contacts")
print("Option 5: Search all the contacts that begin with a certain letter")
print("Option 6: Search for contacts emails")
print("Option 7: Change contact information")
print("Option 8: Generate a json file with all contacts")
print("Option 9: Finish the program")


def insert_contact(contacts, contact_information):
    register = "yes"
    while register == "yes":
        name = input("Enter the contact name: ")
        telephone = input("Enter the contact telephone: ")
        email = input("Enter the contact email: ")
        contact_information["name"] = name
        contact_information["telephone"] = telephone
        contact_information["email"] = email
        contacts[name] = contact_information
        contact_information = {}
        register = input("Do you want to add more contacts? ")
    return contacts, contact_information


def remove_contact(contacts):
    remove = "yes"
    while remove == "yes":
        name = input("Enter the contact name: ")
        contacts.pop(name)
        remove = input("Do you want to remove someone else from the list: ")
    return contacts


def search_contact(contacts):
    search_contact = "yes"
    while search_contact == "yes":
        name = input("Enter the contact name: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact does not exist, if you want add, enter no twice, and after that insert option 1")
        search_contact = input("Do you want to search another name?")
    return contacts


def list_all_contacts(contacts):
    for contact in contacts:
        print(contact)
    return contacts


def search_contact_by_initial_letter(contacts):
    search_letter = "yes"
    while search_letter == "yes":
        letter = input("Search for contact using the first letter of the name: ")
        for contact in contacts:
            if (contacts[contact]["name"][0]) == letter:
                print(contacts[contact])
        search_letter = input("Do want to search another contact using the first letter of the name: ")
    return contacts


def contacts_email(contacts):
    json_file_email = open("email-file.json", "w")
    for contact in contacts:
        email_information = {"name": contacts[contact]["name"], "email": contacts[contact]["email"]}
        json.dump(email_information, json_file_email, indent=2)
    return contacts


def change_contact_information(contacts):
    add_new_information = "yes"
    while add_new_information == "yes":
        change_information = input("Do you want to change name, telephone or email?")
        contact_change = input("Enter the name of the contact that you want to update: ")
        new_information = input("What is the change?")
        contacts[contact_change][change_information] = new_information
        add_new_information = input("Do you want to do another change in contacts?")
    return contacts


def json_contacts(contacts):
    json_file_information = open("contact-information.json", "w")
    for contact in contacts:
        information = {"name": contacts[contact]["name"], "telephone": contacts[contact]["telephone"],
                       "email": contacts[contact]["email"]}
        json.dump(information, json_file_information, indent=2)
    return contacts


def finish_the_program():
    finish = "yes"
    return finish


options = {1: insert_contact, 2: remove_contact, 3: search_contact, 4: list_all_contacts,
           5: search_contact_by_initial_letter, 6: contacts_email, 7: change_contact_information,
           8: json_contacts,9: finish_the_program}

contacts = {}
contact_information = {}
finish = "no"

while finish != "yes":
    option = int(input("Enter an option: "))
    function = options[option]
    if option == 1:
        contacts, contact_information = function(contacts, contact_information)
    elif option == 9:
        finish = function(contacts)
    else:
        contacts = function(contacts)


