# შევქმნათ ფუნქცია
def check_palindrome_list(my_input):
    # შევამოწმონთ შეყვანილი უდრის თუ არა შეყვანილის შეტრიალებულს
    if my_input == my_input[::-1]:
        print("\n", "სტრიქონი არის პალინდრომი" + "\n")

    else:
        print("\n", "სტრიქონი არ არის პალინდრომი" + "\n")

# input-ის ფუნქციაში ჩასმა
my_input = [input("\n" + "შეიყვანეთ სასურველი სთრიქონი: ")]
my_input = ' '.join([str(elem) for elem in my_input])
check_palindrome_list(my_input)
