def bday_message():
    name = input("name: ")
    birthMonth = input("Birth Month: ")
    birthDay = input("Birth Day of the Month: ")
    birthYear = input("Birth Year: ")
    print(name, ", your birthday is on ", sep="", end="")
    print(birthMonth, " ", birthDay, ", ", birthYear, "!", sep="")

bday_message()
bday_message()
bday_message()