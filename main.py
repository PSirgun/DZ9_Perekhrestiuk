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
        except TypeError:
                return "Too much arguments"
    return inner

def decor_change(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough arguments"
        except TypeError:
            return "No one argument"
        except KeyError:
            return "Name not in phone book"
    return inner

# sub block -------------------------------------------------------------------------------------------------------
@decor_func
def sub_add(*args):
    ful_name = ""
    args = list(args)
    for i in args:
        if not re.search(r'(\d|\+)',i):
            ful_name += i + ' '       
        else:
            args = args[args.index(i):]
            args.insert(0, ful_name.strip().title())
            break

    if args[0] not in phone_book:
        good_phone = sanit_phone(args[1])
        if good_phone:
            phone_book[args[0]] = good_phone
            return f" Added {args[0]} - {good_phone} to phone book "
        else:
            return "Phone is incorrect"  
    else:
        return "Name already in phone book"

@decor_func   
def sub_show():
    pr_contacts = "All contacts \n"
    for name, phone in phone_book.items():
        pr_contacts += f"{name} - {phone} \n"
    return pr_contacts

@decor_change
def sub_change(*args):
    good_phone = sanit_phone(args[1])
    if good_phone:
        del phone_book[args[0]]
        phone_book[args[0]] = good_phone
        return f" Changed {args[0]} - {good_phone} to phone book "
    else:
        return "Phone is incorrect"  

@decor_func 
def sub_phone(*args):
    return (f'{args[0]} - {phone_book[args[0]]}')

@decor_func
def sub_hello():
    return "How can I help you?"

@decor_func
def sub_exit():
    return "Good bye!"

OPERATIONS = {
    sub_hello : ("hello",), 
    sub_add : ("add",),
    sub_change : ("change",),
    sub_phone : ("phone",),
    sub_show : ("show all",),
    sub_exit: ("good bye", "close", "exit", ".")
}
# end sub block ---------------------------------------------------------------------------------------------------

def sanit_phone(bad_phone):
        phone1 = re.findall('\d+', bad_phone)
        phone2 = ''.join(phone1)
        if len(phone2) >= 10:
            return phone2

def main():
    while True:
        user_input = input(">>> ")
        command_found = False        
        for sub_f, command  in OPERATIONS.items():
            if command_found:
                break 
            for com in command:
                if user_input.casefold().startswith(com):
                    print(sub_f(*user_input[len(com):].strip().split()))
                    if sub_f == sub_exit:
                        return
                    command_found = True
                    break
        if not command_found:       
            print("Command not found")

if __name__ == '__main__':
    main() 