def PrintUserInformation(Name, Surname, YearOfBirth, City, Email, Phone):
    print(f"{Name} {Surname} ({YearOfBirth}), {City}, Phone: '{Phone}', Email: '{Email}'")
    return

print("Please enter information about yourself...")
inName = input("Name: ")
inSurname = input("Surname: ")
inYearOfBirth = input("Year of birth: ")
inCity = input("City: ")
inEmail = input("Email: ")
inPhone = input("Phone: ")

PrintUserInformation(Name=inName, Surname=inSurname, YearOfBirth=inYearOfBirth, City=inCity, Email=inEmail, Phone=inPhone)
