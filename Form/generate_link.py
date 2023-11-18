import streamlit as st
import requests
from email.message import EmailMessage
import smtplib



api_endpoint = 'http://20.20.16.145:5050/add_client'
hardcoded_link = 'https://sirdargroup.com/'
def generate_questionnaire_link(email, company_name):
   
    headers = {'Content-Type': 'application/json'}
    data = {'email': email, 'company_name': company_name}
    response = requests.post(api_endpoint, json=data, headers=headers)


    if response.status_code == 200:
        return hardcoded_link
    else:
        return None


def send_email(email, questionnaire_link):
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'mukendigloria5@gmail.com'
    smtp_password = 'stbd tkxl remh hxrf'
    msg = EmailMessage()
    msg.set_content(f"Click the following link to access our app and login with your company details: {questionnaire_link}")
    msg['Subject'] = 'Questionnaire Link'
    msg['From'] = 'lehlogonolomaw@gmail.com'
    msg['To'] = email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)


def main():
    st.title("SIRDAR GROUP")
    st.header("Questionnaire Link Generator")

    company_name = st.text_input("Comapany Name")
    st.session_state.company_name = company_name


    emails = st.session_state.get("emails", [""])

    for i, email in enumerate(emails):
        emails[i] = st.text_input(f"Email {i + 1}", email)
    

    if st.button("Add New Email"):
        emails.append("")
   




    # Save updated emails list to session state
    st.session_state.emails = emails
    st.session_state.company_name = company_name

    if st.button("Generate Link and Copy"):
        # Use the hardcoded link instead of making an API call
        access_link = hardcoded_link
        st.success(f"Access Link: {access_link}")



    if st.button("Generate Link and Send Emails"):
        for email in emails:
            if email.strip() != "":
                questionnaire_link = generate_questionnaire_link(email, company_name)
                
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
                st.error(f"Email field is Empty! Please enter Email")

if __name__ == "__main__":
    main()
