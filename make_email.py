# შევიყვანოთ სახელი
my_name = str(input("შეიყვანეთ სახელი ინგლისური ასოებით : "))

# შემოწმების ფუქცია, არის თუარა ინგლისური ენა

def is_english(s):
    return (s.isascii())

# შემოწმების ფუნქცია, არის თუარა ინგლისური ასოები

def is_alphabet(d):
    return (d.isalpha())

# შემოწმება არის თუარა ინგლისური ენა და ინგლისური ასო
while is_english(my_name) is False or is_alphabet(my_name) is False:
    my_name = str(input("შეიყვანეთ სახელი ინგლისური ასოებით : "))
# შევოყვანოთ გვარი
my_surname = str(input("შეიყვანეთ გვარი ინგლისური ასოებით : "))
# შემოწმება არის თუარა ინგლისური ენა და ინგლისური ასო
while is_english(my_surname) is False or is_alphabet(my_surname) is False:
    my_surname = str(input("შეიყვანეთ გვარი ინგლისური ასოებით : "))
# დავპრინტოთ E-mail
else:
    print("\n"+my_name.lower() + "." + my_surname.lower() + "@btu.edu.ge"+"\n")
