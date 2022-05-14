# Name: Word List Class
# Description: Provide adding/deleting/sending World words.
#


def get_request():
    """
    Read "temp.txt" and get a request from user.
    :return:
    """
    try:
        with open("temp.txt", "r") as temp:
            req = temp.readline()
    except FileNotFoundError:
        print(f"File {temp} does not exist.")
    except OSError:
        print(f"OSError opening {temp}.")

    return req


def reply(msg: str):
    """
    Write message to temp.txt
    :param msg: str message to be sent to user
    :return:
    """
    try:
        with open("temp.txt", "w") as temp:
            temp.truncate(0)
            temp.write(msg)
    except FileNotFoundError:
        print(f"File {temp} does not exist.")
    except OSError:
        print(f"OSError opening {temp}.")


class WordList:

    def __init__(self, wordFile: str):
        """
        Initialize WordList Class
        :param wordFile: str. file path to a text file contains words.
        """
        self.file = wordFile
        self.words = []
        self.load_file()

    def load_file(self):
        """
        Read wordFile and store words to self.words
        :return:
        """
        with open(self.file, 'r') as file:
            for line in file:
                self.words.append(line)

    def get_word(self):
        """
        return self.words
        :return: self.words  list of words
        """
        words = ""
        for item in self.words:
            words += item
        reply("200\n")
        with open("temp.txt", "a") as temp:
            temp.write(words)

    def add_word(self, a_word: str):
        """
        add a word to wordFile. append it to the eof.
        :param a_word: a 5-letter word.
        :return:
        """
        if a_word + '\n' not in self.words:
            self.words.append(a_word + '\n')

            with open(self.file, 'a') as file:
                file.write(a_word + '\n')
            reply("200")
        else:
            reply("-1")  # a_word is already in self.words

    def delete_word(self, a_word: str):
        """
        delete a word in wordFile.
        :param a_word: a 5-letter word
        :return:
        """
        if a_word + '\n' in self.words:
            self.words.remove(a_word + '\n')

            with open(self.file, 'r+') as file:
                file.truncate(0)
                for item in self.words:
                    file.write(item)
            reply("200")


if __name__ == '__main__':

    storage = WordList("archive.txt")

    while True:
        # read temp file
        request = get_request()

        action = ""
        for i in range(len(request)):
            if request[i] == "(":
                action = request[:i]
                break

        # action = add
        if action == "add":
            word = request[4:-1]
            try:
                storage.add_word(word)
            except FileNotFoundError:
                reply("-1")
            except OSError:
                reply("-1")

        # action = delete
        elif action == "delete":
            word = request[7:-1]
            try:
                storage.delete_word(word)
            except FileNotFoundError:
                reply("-1")
            except OSError:
                reply("-1")

        # action = get
        elif action == "get":
            try:
                storage.get_word()
            except FileNotFoundError:
                reply("-1")
            except OSError:
                reply("-1")
