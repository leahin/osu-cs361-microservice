# Word List Microservice
##### CS361 micrservice for teammates

# Description
A simple microservice communicate via a text file. It provides the following services:
1. add(word): add the given word to archive.txt only if when the word is NOT in archieve.txt
2. delete(word): delete the given word to archive.txt
3. get(): get all words from archive.txt and send them to the user

# How to Use
0. Get all files except test.py
1. Run microservice locally.
2. From your program, clear and then write a command (ex. add(word), delete(word), get()) to temp.txt
3. Upon a succssful request, the microservice will clear temp.txt and write "200". (with get() request, it will add all words from archive.txt followed by the "200")
4. If there's an error or failed requests, the microserivce will clear temp.txt and write "-1" instead.

# how to test the microservice
1. text.py is a dummy client file and can be used to test the microservice.
2. Simply run $python3 test.py then enter either add(word), delete(word), or get() to test if temp.txt and archive.txt are actually affected by your requests.
