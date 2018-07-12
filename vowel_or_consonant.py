letter=input("")
vowel=['a','e','i','o','u','A','E','I','O','U']
if((letter>='a' and letter<='z') or (letter>='A' and letter<='Z')):
  if letter in vowel:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
