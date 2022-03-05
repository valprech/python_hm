def user_info(name, lastname, dob, hometown, email, mobnumber):
    return f" User information: \n 1. Name: {name} \n 2. Last name: {lastname} \n 3. DOD: {dob} \n 4. Hometown: {hometown} \n 5. E-mail: {email} \n 6. Mobile number: {mobnumber} "


arg1 = input("Enter your name: ")
arg2 = input("Enter your last name: ")
arg3 = input("Enter your DOB: ")
arg4 = input("Enter your hometown: ")
arg5 = input("Enter your email: ")
arg6 = input("Enter your mobile number: ")

print(user_info(name=arg1, lastname=arg2, dob=arg3, hometown=arg4, email=arg5, mobnumber=arg6))
