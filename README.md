# Password Strength Estimation Tool

## Overview
This tool estimates the strength of a password based on various factors including length, complexity, commonality, and presence of personal information like first name, last name, and dates. It provides a score indicating the strength level of the password: Bad, Easy, Moderate, or Hard.

## Features
- Estimates password strength based on length, complexity, and presence of common patterns.
- Considers personal information such as first name, last name, and dates to enhance accuracy.
- Provides a score indicating the strength level of the password.
- Supports both alphanumeric and special characters in passwords.
- Alerts users if the password is too common or easily guessable.

## Usage

1. **Setting up `commonpass.txt`:**
   
   - The `commonpass.txt` file contains a list of common passwords that the system uses to check against. Ensure this file is present in the project directory and populated with common passwords.

2. **Running the code:**
   
   - Execute the `main.py` file with Python to run the password strength estimation process.
     
     ```bash
     python main.py
     ```
   
3. **Input required details:**
   
   - Provide your first name, last name, and the password you want to check when prompted.

4. **View the result:**
   
   - The system will display the estimated strength of the password based on the provided criteria.


## Strength Estimation Algorithm
The strength estimation algorithm follows these steps:
1. **Length Check:** Checks if the password length is at least 8 characters.
2. **Alphanumeric Check:** Penalizes passwords that contain only alphabetic or numeric characters.
3. **Common Password Check:** Checks if the password matches any commonly used passwords.
4. **Credential Check:** Penalizes passwords containing the user's first name, last name, or dates.
5. **Entropy Calculation:** Calculates the entropy of the password based on the unique character set.
6. **Scoring:** Assigns a score based on the above checks and entropy calculation.

## Examples
- A password scoring less than 0 indicates a weak password.
- Scores between 0 and 7 suggest an easy-to-guess password.
- Scores between 8 and 14 indicate a moderately strong password.
- Scores above 14 indicate a strong password.

## Requirements
- Python 3.x
- dateutil
- re

## File Structure

- `main.py`: Main script implementing the password strength estimation functionality.
- `commonpass.txt`: Text file containing a list of common passwords.
- `README.md`: Documentation providing an overview of the project, installation instructions, and usage details.
- `requirements.txt`: File listing the required Python dependencies.


## Author
[Naman Deol](https://www.linkedin.com/in/naman-deol-b1a581232/)

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests for any enhancements or bug fixes.

## Contact
For any inquiries or further assistance, feel free to contact the author via LinkedIn.


