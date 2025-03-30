import pandas as pd
import numpy as np
import requests
import json
import os

with open("student_directory.json", "r") as f:
    student_directory = json.load(f)

grade_input = str(input("Please enter the grade you want to filter by (e.g., '12'): "))
senior_data = []

for student in student_directory:
    if student["GradeDisplay"] == grade_input:
        senior_data.append({
            "Name": f"{student['FirstName']} {student['LastName']}",
            "Email": student["Email"]
        })

df = pd.DataFrame(senior_data)
print("Data successfully collected from student directory.")
print(f"First 5 entries: \n{df.head()} \n")

# Create third column for Paranoia targets
df['Paranoia Target'] = np.random.permutation(df['Name'].values)
print(f"First 5 entries with Paranoia Target: \n{df.head()} \n")

# Send automated emails to each player with their Paranoia target
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

sender_email = os.getenv("EMAIL_ADDRESS")
sender_password = os.getenv("EMAIL_PASSWORD")

def send_email():
    if input(f"Are you sure you want to send emails to {len(df)} players? (yes/no): ").strip().lower() != 'yes':
        print("Email sending aborted.")
        return
    else: 
        for index, row in df.iterrows():
            recipient_email = row['Email']
            target_name = row['Paranoia Target']
            
            subject = "Your Paranoia Target"
            body = f"""
            Hello {row['Name']},
            
            Your Paranoia target is: {target_name}.
            
            Best regards,
            Paranoia Game Coordinator
            """
            
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            
            message.attach(MIMEText(body, "plain"))
            
            print(f"To: {recipient_email} \n From: {sender_email} \n Subject: {subject} \n Body: {body}")

            # Uncomment the following lines to enable sending emails
            # try:
            #     server = smtplib.SMTP("smtp.gmail.com", 587)
            #     server.starttls()
            #     server.login(sender_email, sender_password)
            #     text = message.as_string()
            #     server.sendmail(sender_email, recipient_email, text)
            #     server.quit()
            #     print(f"Email successfully sent to {recipient_email}")
                
            # except Exception as e:
            #     print(f"Error sending email to {recipient_email}: {e}")

if __name__ == "__main__":
    send_email()