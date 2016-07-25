import pyperclip
 5.
 6. # the string to be encrypted/decrypted
 7. message = 'This is my secret message.'
 8.
 9. # the encryption/decryption key
10. key = 13
11.
12. # tells the program to encrypt or decrypt
13. mode = 'encrypt' # set to 'encrypt' or 'decrypt'
14.
15. # every possible symbol that can be encrypted
16. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
17.
18. # stores the encrypted/decrypted form of the message
19. translated = ''
20.
21. # capitalize the string in message
22. message = message.upper()
23.
24. # run the encryption/decryption code on each symbol in the message string
25. for symbol in message:
26.     if symbol in LETTERS:
27.         # get the encrypted (or decrypted) number for this symbol
28.         num = LETTERS.find(symbol) # get the number of the symbol
29.         if mode == 'encrypt':
30.             num = num + key
31.         elif mode == 'decrypt':
32.             num = num - key
33.
34.         # handle the wrap-around if num is larger than the length of
35.         # LETTERS or less than 0
36.         if num >= len(LETTERS):
37.             num = num - len(LETTERS)
38.         elif num < 0:
39.             num = num + len(LETTERS)
40.
41.         # add encrypted/decrypted number's symbol at the end of translated
42.         translated = translated + LETTERS[num]
43.
44.     else:
45.         # just add the symbol without encrypting/decrypting
46.         translated = translated + symbol
47.
48. # print the encrypted/decrypted string to the screen
49. print(translated)
50.
51. # copy the encrypted/decrypted string to the clipboard
52. pyperclip.copy(translated)
