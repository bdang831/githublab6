# Bethany Dang


def encode(to_encode):
    encoded = ""
    for i in range(len(to_encode)):
        # shifts each digit by 3
        current_digit = int(to_encode[i]) + 3
        # decreases by 10 if greater than ten
        # ex: 9 + 3 = 12, shifted down 10 to 2
        if current_digit >= 10:
            current_digit -= 10
        encoded += str(current_digit)
    return encoded

def decode(to_decode):
	decoded = ""
	for i in range(len(to_decode)):

        current_digit = int(to_decode[i]) - 3

        if current_digit < 0:
            current_digit += 10
        decoded += str(current_digit)
    return decoded


if __name__ == "__main__":
    password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_choice = int(input("Please enter an option: "))
        if user_choice == 1:
            string_to_encode = input("Please enter your password to encode: ")
            # password is saved as encoded password
            password = encode(string_to_encode)
            print("Your password has been encoded and stored!")

        if user_choice == 2:
		decoded_password = decode(password)
		print(f"The encoded password is {password}, and the original password is {decode(password)}")

        if user_choice == 3:
            break
