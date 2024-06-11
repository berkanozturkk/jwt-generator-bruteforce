### JWT Generator and Brute Force Tool

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

#### Overview
This repository contains tools for generating JSON Web Tokens (JWT) and performing brute force attacks on JWTs. It includes functionalities to create JWTs with specified credentials and to validate and brute force JWTs using a predefined keylist.

#### Features
- 🔑 **JWT Generation:** Create JWTs with user credentials, a secret key, and a specified algorithm.
- 🛠️ **Brute Force JWTs:** Validate JWT structure and attempt to crack tokens using a user-provided keylist.
  
#### Technologies
- **Language:** 
  - ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- **Libraries:**
  - `jwt`

#### Prerequisites
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 

#### Getting Started
1. **Clone the repository:**
   ```bash
   git clone https://github.com/berkanozturkk/jwt-generator-bruteforce.git
   ```
2. **Install dependencies:**
   ```bash
   pip install pyjwt
   ```

#### Running the Application
- **Generate JWT:**
  ```bash
  python tokenvalidator.py
  ```
- **Brute Force JWT:**
  ```bash
  python jwt_bruteforce.py
  ```

