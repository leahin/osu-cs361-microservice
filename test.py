
if __name__ == '__main__':

    while True:
        action = input("Enter action: ")

        with open("temp.txt", "w") as temp:
            temp.truncate(0)
            temp.write(action)
