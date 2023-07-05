import jwt

secret = "xQt"

username=input("Enter your username : ")
email=input("Enter your email : ")
password=input("Enter your password : ")

credentials= {"username": username, "email": email, "password": password}

validjwt = jwt.encode(credentials, secret , algorithm="HS256",headers={"typ": "JWT"})

print(validjwt)

