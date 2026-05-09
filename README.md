# 🔐 Password Generator

A simple Python program that generates a strong, random password based on the length you choose.

---

## 📋 Description

This program asks the user for a desired password length, then builds a random password using a mix of letters, numbers, and symbols. It is lightweight, beginner-friendly, and runs directly in the terminal.

---

## ⚙️ How It Works

```
Input length → Select random characters → Display password
```

| Step | Action |
|------|--------|
| 1 | Program starts |
| 2 | User enters the desired password length |
| 3 | Characters are prepared (letters + numbers + symbols) |
| 4 | Random characters are picked one by one |
| 5 | They are joined into a single string |
| 6 | The final password is displayed |

---

## 🗂️ Project Structure

```
password-generator/
│
└── password_generator.py   # Main program file
```

---

## 🧰 Requirements

- Python 3.x
- No external libraries needed — uses built-in modules only:
  - `random`
  - `string`

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Open a terminal and navigate to the project folder.
3. Run the following command:

```bash
python password_generator.py
```

4. Enter your desired password length when prompted.

---

## 💻 Code

```python
import random
import string

length = int(input("Enter the length of the password: "))
password = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, length))
print("Your password is:", password)
```

---

## 📌 Example

```
Enter the length of the password: 12
Your password is: aB3#kP9!mQzL
```

---

## ⚠️ Note

- The length you enter must not be greater than **94** (the total number of unique characters available).
- Each character in the password is **unique** — no character repeats.

---

## 👤 Author

**Abdul Muqeet**  
Computer Science Student — UMT  
Programming for AI
