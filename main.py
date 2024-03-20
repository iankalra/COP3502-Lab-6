def encode(password):
    encodedPass = ""
    encodedPass += ''.join(([str((int(char) + 3)) for char in password]))
    return encodedPass


def main():
    while (1):
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            passwd = input("Please enter your password to encode: ")
            encodedPasswd = encode(passwd)
            print("Your password has been encoded and stored!")
#        elif choice == "2":
#            print("The encoded password is" + str(encodedPasswd) + "and the original password is" \
#                 + str(decode(encodedPasswd)) + ".")
        else:
            break


if __name__ == '__main__':
    main()
