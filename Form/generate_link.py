import streamlit as st
import requests
from email.message import EmailMessage
import smtplib


api_endpoint = 'http://localhost:8501/questionnaire'

def generate_questionnaire_link(email):
    response = requests.post(api_endpoint, json={'email': email})
    if response.status_code == 200:
        return response.json().get('questionnaire_link')
    else:
        return None

def send_email(email, questionnaire_link):
    # Replace with your SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'lehlogonolomaw@gmail.com'
    smtp_password = 'Hlogi12!'
    msg = EmailMessage()
    msg.set_content(f"Click the following link to access the questionnaire: {questionnaire_link}")
    msg['Subject'] = 'Questionnaire Link'
    msg['From'] = 'lehlogonolomaw@gmail.com'
    msg['To'] = email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

def main():
    st.title("SIRDAR")
    st.header("Questionnaire Link Generator")

    emails = st.session_state.get("emails", [""])

    for i, email in enumerate(emails):
        emails[i] = st.text_input(f"Email {i + 1}", email)

    if st.button("Add New Email"):
        emails.append("")

    # Save updated emails list to session state
    st.session_state.emails = emails

    if st.button("Generate Link and Copy"):
       
        try:
            response = requests.get(api_endpoint)
            print(response)

            if response.status_code == 200:
                access_link = response.json().get("questionnaire_link")
                if questionnaire_link:
                    st.success(f"Access Link: {questionnaire_link}")
                else:
                    st.error("Failed to generate access link. Please try again.")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")

    if st.button("Generate Link and Send Emails"):
        for email in emails:
            if email.strip() != "":
                questionnaire_link = generate_questionnaire_link(email)
                if questionnaire_link:
                    send_email(email, questionnaire_link)
                    st.success(f"Email sent successfully to {email}!")

                    # Copy and display link option
                    st.write(f"Generated Link: {questionnaire_link}")
                    st.button(
                        "Copy Link to Clipboard",
                        key=f"copy_{email}",
                        on_click=lambda email=email: st.text_area(
                            label="", value=questionnaire_link, height=1, key=f"textarea_{email}"
                        ),
                    )
                else:
                    st.error(f"Failed to generate questionnaire link for {email}.")

if __name__ == "__main__":
    main()
