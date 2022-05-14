# Word List Microservice
##### CS361 micrservice for teammates

# Description
This microservice provides the following services:
1. add(word): add the given word to archive.txt only if when the word is NOT in archieve.txt
2. delete(word): delete the given word to archive.txt
3. get(): get all words from archive.txt and send them to the user

# How to Use
1. Run microservice locally.
2. From your program, clear and then write a command (ex. add(word), delete(word), get()) to temp.txt
3. Upon a succssful request, the microservice will clear temp.txt and write "200". (with get() request, it will add all words from archive.txt followed by the "200")
4. If there's an error or failed requests, the microserivce will clear temp.txt and write "-1" instead.
