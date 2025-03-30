# paranoia 

A Python script for organizing and managing a "Paranoia" style game among students. This program reads a student directory, assigns targets randomly, and sends automated email notifications to participants.

## Installation
1. Clone this repository or download the script
2. Install required packages

`pip install -r requirements.txt`

3. Create a `.env` file in the same directory with your email credentials. If you have 2FA enabled on your Gmail account, you may need to create an "App Password." To do so, open your Google account and navigate to the following: Security --> 2-Step Verification --> App Passwords.

```
EMAIL_ADDRRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password (app password if 2FA is enabled)
```

## Email Functionality
The email sending functionality is disabled by default for safety. To enable it, uncommted the email sending code block in the `send_email()` function.