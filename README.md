# JWT-Generator-Bruteforce
JW Token generator and brute force.

*The program uses the **jwt** library*

tokenvalidator.py takes the credential informations of user and creates jw token with these credentials, with the secret key specified by the user, with the algorithm type determined by the user.

The jwt_bruteforce.py file takes the jw token as input. It first checks if the token structure is valid or not. Then, it takes a user-specified keylist (must be in the same file as jwt_bruteforce.py) as input and tries to crack the jw token with brute force over the keys in this list.

## Technologies Used : Python
