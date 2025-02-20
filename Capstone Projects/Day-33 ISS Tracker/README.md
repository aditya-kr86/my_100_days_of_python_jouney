# 🚀 ISS Tracker

A Python script to track the International Space Station (ISS) and send an email notification when it is overhead.

## 📜 Description

This project is a beginner-friendly Python script that allows you to track the position of the International Space Station (ISS) and send an email notification when it is overhead and it is dark outside.

### Example:
```
The script checks the current position of the ISS and your location's sunrise and sunset times. If the ISS is overhead and it is dark, it sends an email notification.
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
   git sparse-checkout set "Capstone Projects/Day-33 ISS Tracker"
   ```
2. Navigate to the Capstone Projects directory:
   ```bash
   cd Capstone\ Projects/
   ```
3. Navigate to the Day-33 ISS Tracker directory:
   ```bash
   cd Day-33\ ISS\ Tracker/
   ```
4. Install the required dependencies:
   ```bash
   pip install requests
   ```
5. Update the `MY_LAT`, `MY_LONG`, `MY_EMAIL`, `MY_PASSWORD`, and `recipient_email` variables in the `iss-tracker.py` file with your credentials and location details.
6. Run the script:
   ```bash
   python3 iss-tracker.py
   ```

#### On Windows:

1. Clone this repository:
   ```bash
   git clone --depth 1 --filter=blob:none --sparse https://github.com/aditya-kr86/my_100_days_of_python_jouney.git
   cd my_100_days_of_python_jouney
   git sparse-checkout set "Capstone Projects/Day-33 ISS Tracker"
   ```
2. Navigate to the Capstone Projects directory:
   ```bash
   cd "Capstone Projects"
   ```
3. Navigate to the Day-33 ISS Tracker directory:
   ```bash
   cd "Day-33 ISS Tracker"
   ```
4. Install the required dependencies:
   ```bash
   pip install requests
   ```
5. Update the `MY_LAT`, `MY_LONG`, `MY_EMAIL`, `MY_PASSWORD`, and `recipient_email` variables in the `iss-tracker.py` file with your credentials and location details.
6. Run the script:
   ```bash
   python iss-tracker.py
   ```

## 📦 Features

- Tracks the position of the ISS
- Checks your location's sunrise and sunset times
- Sends an email notification when the ISS is overhead and it is dark

## 🛠️ Technologies Used

- **Python** - for implementing the logic
- **requests** - for making HTTP requests
- **smtplib** - for sending emails

## 💡 Ideas for Improvement

- Add a graphical user interface (GUI) for better user experience.
- Implement input validation to handle incorrect inputs.
- Add more customization options for the email notifications.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📬 Contact

ADITYA KUMAR  
Linkedin: [linkedin.com/in/aditya-kr86](http://linkedin.com/in/aditya-kr86)  
Email: [aditya_kumar_gupta@yahoo.com](mailto:aditya_kumar_gupta@yahoo.com)

---

Enjoy tracking the ISS! 😊🚀
