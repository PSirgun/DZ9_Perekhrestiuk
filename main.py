import re


phone_book = {}

def decor_func(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough arguments"
        except KeyError:
            return "Name not in phone book"
        # except TypeError:
        #     return "Too much arguments"
    return inner

def decor_change(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough arguments"
        except TypeError:
            return "No one argument"
    return inner

# sub block -------------------------------------------------------------------------------------------------------
@decor_func
def sub_add(*user_input_list):
    if user_input_list[1] not in phone_book:
        good_phone = sanit_phone(user_input_list)
        if good_phone:
            phone_book[user_input_list[1]] = good_phone
            return f" Added {user_input_list[1]} - {good_phone} to phone book "
        else:
            return "Phone is incorrect"  
    else:
        return "Name already in phone book"

@decor_func   
def sub_show(*arg):
    pr_contacts = "All contacts \n"
    for name, phone in phone_book.items():
        pr_contacts += f"{name} - {phone} \n"
    return pr_contacts

@decor_change
def sub_change(*user_input_list):
    if user_input_list[1] in phone_book:
        good_phone = sanit_phone(user_input_list)
        if good_phone:
            phone_book[user_input_list[1]] = good_phone
            return f" Changed {user_input_list[1]} - {good_phone} to phone book "
        else:
            return "Phone is incorrect"  
    else:
        return "Name not in phone book"

@decor_func 
def sub_phone(*user_input_list):
    return (f'{user_input_list[1]} - {phone_book[user_input_list[1]]}')

OPERATIONS = {
    "add" : sub_add,
    "change" : sub_change,
    "phone": sub_phone,
    "show all" : sub_show
}
# end sub block ---------------------------------------------------------------------------------------------------

def sanit_phone(user_input_list):
        phone1 = re.findall('\d+', user_input_list[2])
        phone2 = ''.join(phone1)
        if len(phone2) >= 10:
            return phone2
        else:
            return 


def main():
    while True:
        user_input = input(">>> ")
        
        if user_input.casefold() == "hello":
            print ("How can I help you?")
        
        elif user_input.casefold() in ("good bye", "close", "exit", '.'):
            print ("Good bye!")
            break
        else:
            user_input_list = user_input.split(" ")
            
            if user_input_list[0] == "show":
                user_input_list[:2] = [user_input_list[0]+' '+user_input_list[1]]
            
            if user_input_list[0] in OPERATIONS:
                sub_input = OPERATIONS[user_input_list[0]]
                print(sub_input(*user_input_list))
            else:
                print('command not found')

if __name__ == '__main__':

    main()