
import re

username = input("Masukan Username anda: ")
if re.match("^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?![\d@#$=])(?<![\d@#$=]){5,9}$", username):
    print ("Sesuai")
else:
    print ("Tidak Sesuai")
    
password = input("Masukan Passwordnya: ")
if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$=])[\w\d@#$=]{8,}$", password):
    print ("Sesuai")
else:
    print ("Tidak Sesuai")