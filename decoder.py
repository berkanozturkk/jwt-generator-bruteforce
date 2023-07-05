import base64
import jwt
import time
import json
import sys
import binascii

counter=0

token = input("Enter JWT token:")

try:
    elements = token.split('.')
    encodedheader = elements[0]
    header = base64.b64decode(encodedheader);
    algo = json.loads(header)

except binascii.Error as e :
    print("Token structure is invalid")
    sys.exit()

print(algo['alg'])


files = input("Enter wordlist name : ")

start=time.time()

with open(files) as wordlist:
    for key in wordlist:
            try:
                counter+=1
                payload = jwt.decode(token, key.rstrip(), algorithms=algo['alg'])
                print("Success. Token decoded with the following key:" + key)
                print(payload)
                break
            except jwt.InvalidTokenError:
                counter+=1

timepassed=((time.time() - start))

print("Number of attempts : ")
print(counter)
print("Time passed in seconds : ")
print(round(timepassed,2))