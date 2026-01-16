# Projects Folder
This folder contains the projects assigned for this module. Below are the description for both of the tasks assigned:
---
## `Task 1: Beckett Pizza Plaza – 4-for-3 Offer System`

---

### Project Description
This project implements a **4-for-3 pizza discount** for *Beckett Pizza Plaza*. When a customer orders four pizzas, the **cheapest pizza is free**. The program collects pizza prices, validates inputs, applies the discount, and shows the final total and discount percentage.

---

### Features
- Interactive CLI-based program
- Accepts prices for **four pizzas**
- Validates user input (positive numeric values only)
- Automatically applies the **4-for-3 discount**
- Displays:
  - Final discounted price
  - Discount percentage
- Modular and reusable functions

---

### How It Works
1. The user is prompted to enter prices for four pizzas.
2. Invalid inputs (non-numeric or ≤ 0) are rejected.
3. The program:
   - Calculates the original total
   - Identifies the cheapest pizza
   - Deducts its price from the total
4. The final amount and discount percentage are displayed.

---

## `Task 2: Password Security Verification System`

---

### Project Description
This project implements a **password security verification system** designed to assess password strength and confirm user authenticity.  
The system enforces a minimum password length requirement and performs randomized character verification checks to ensure that the user has legitimate knowledge of the entered password.
The program operates through a command-line interface and terminates immediately if any security requirement is not satisfied.

---

### Features
- Interactive CLI-based program
- Enforces a minimum password length of **nine characters**
- Performs randomized character-position verification
- Executes multiple security checks for increased reliability
- Terminates immediately upon failed verification
- Modular and reusable security functions

---

### How It Works
1. The user is prompted to enter a password.
2. The system verifies that the password contains at least nine characters.
3. The program performs three security checks:
   - A random position within the password is selected.
   - The user is prompted to enter the character at that position.
4. If the user provides an incorrect character at any stage, the program terminates.
5. If all verification checks are passed successfully, the password is accepted and the security check is completed.

---


