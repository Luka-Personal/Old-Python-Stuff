import random
# გავაგოროთ ორი კამათელი და დავაგენერიროთ ორი list
first_roll_list = [random.randint(1, 6) for _ in range(0, 6)]
second_roll_list = [random.randint(1, 6) for _ in range(0, 6)]

# გავაერთიანოთ ეს ორი list და შევქმნათ tuples
tuple_dices = list(zip(first_roll_list, second_roll_list))
# დავპრინტოთ საწყისი სია
print("თქვენი საწყისი სია არის: ")
print(tuple_dices, "\n")
# დავპრინტოთ დასორტირებული სია
print("თქვენი დასორტირებული სია არის: ")
print(sorted(tuple_dices, key=lambda x: x[0] + x[1]))
