import random
import string
length = int(input("Enter the length of the password"))
password = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, length))
print("your password is", password)



 