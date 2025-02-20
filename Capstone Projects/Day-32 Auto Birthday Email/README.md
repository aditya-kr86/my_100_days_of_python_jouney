# 🎉 Auto Birthday Email

A Python script to automatically send birthday wishes via email!

## 📜 Description

This project is a beginner-friendly Python script that allows you to automatically send birthday wishes via email. It reads the birthday dates and email addresses from a CSV file and sends a random birthday wish from a list of predefined messages.

### Example:
```
The script checks the current date, and if it matches any birthday in the CSV file, it sends an email with a random birthday wish.
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- An email account to send the messages (e.g., Gmail)

### How to Run

#### On Linux:

1. Clone this repository:
   ```bash
   git clone --depth 1 --filter=blob:none --sparse https://github.com/aditya-kr86/my_100_days_of_python_jouney.git
   cd my_100_days_of_python_jouney
   git sparse-checkout set "Capstone Projects/Day-32 Auto Birthday Email"
   ```
2. Navigate to the Capstone Projects directory:
   ```bash
   cd Capstone\ Projects/
   ```
3. Navigate to the Day-32 Auto Birthday Email directory:
   ```bash
   cd Day-32\ Auto\ Birthday\ Email/
   ```
4. Install the required dependencies:
   ```bash
   pip install pandas
   ```
5. Update the `MY_EMAIL` and `MY_PASSWORD` variables in the `birthday_wisher.py` file with your email credentials.
6. Run the script:
   ```bash
   python3 birthday_wisher.py
   ```

#### On Windows:

1. Clone this repository:
   ```bash
   git clone --depth 1 --filter=blob:none --sparse https://github.com/aditya-kr86/my_100_days_of_python_jouney.git
   cd my_100_days_of_python_jouney
   git sparse-checkout set "Capstone Projects/Day-32 Auto Birthday Email"
   ```
2. Navigate to the Capstone Projects directory:
   ```bash
   cd "Capstone Projects"
   ```
3. Navigate to the Day-32 Auto Birthday Email directory:
   ```bash
   cd "Day-32 Auto Birthday Email"
   ```
4. Install the required dependencies:
   ```bash
   pip install pandas
   ```
5. Update the `MY_EMAIL` and `MY_PASSWORD` variables in the `birthday_wisher.py` file with your email credentials.
6. Run the script:
   ```bash
   python birthday_wisher.py
   ```

## 📦 Features

- Automatically sends birthday wishes via email
- Reads birthday data from a CSV file
- Chooses a random birthday wish from a list of predefined messages

## 🛠️ Technologies Used

- **Python** - for implementing the logic
- **pandas** - for reading the CSV file
- **smtplib** - for sending emails

## 💡 Ideas for Improvement

- Add more birthday wish templates.
- Implement input validation to handle incorrect inputs.
- Add a graphical user interface (GUI) for better user experience.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📬 Contact

ADITYA KUMAR  
Linkedin: [linkedin.com/in/aditya-kr86](http://linkedin.com/in/aditya-kr86)  
Email: [aditya_kumar_gupta@yahoo.com](mailto:aditya_kumar_gupta@yahoo.com)

---

Enjoy sending birthday wishes automatically! 😊🎉
