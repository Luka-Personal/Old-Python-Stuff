# შევქმნათ loop
# სანამ სწორ რიცხვს არ შეიყვანს მომხმარებელი არ გამოვიდეთ loop-იდან
while True:
    try:
        user_number = int(input("\n" + "შეიყვანეთ რიცხვი: "))
    except BaseException:
        print("\n", "გთხოვთ შეიყვანოთ მხოლოდ მთელი რიცხვები")
        continue
    else:
        break
# თუ მომხმარებლის მიერ შეყვანილი რიცხვი მეტია ნულზე ის უბრალოდ გავყოთ 10 ზე სანამ არ დაგვრჩება ბოლო ციფრი
if user_number > 0:
    last_digit = user_number % 10
# თუ მომხმარებლის მიერ შეყვანილი რიცხვი ნაკლებია ნულზე ჯერ გავამრავლოთ 0-ზე და გავყოთ 10 ზე სანამ არ დაგვრჩება ბოლო ციფრი
else:
    last_digit = -user_number % 10
# დავპრინტოთ შედეგი
print("\n" + "რიცხვის ბოლო ციფრია: {}".format(last_digit) + "\n")
