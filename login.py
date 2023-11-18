import streamlit as st
import json
import streamlit as st
import requests

# Streamlit pages
def login_page():
    st.subheader("Login")

    # For clients, automate the login assuming the user is a client
    company_name = st.text_input("Company Name", key="client_company_name")
    email = st.text_input("Email", key="client_email", value="client@example.com")

    if st.button("Login as Client"):
        # Call the client authentication endpoint
        payload = {"company_name": company_name, "email": email}
        with open("worker.json", "w") as json_file:
            json.dump(payload, json_file)
        headers = {"Content-Type": "application/json"}
        response = requests.post("http://20.20.16.145:5050/authenticate_director",data=json.dumps(payload),headers=headers)
        if response.status_code == 200:
            # Assuming the API returns a success status code
            st.success("Logged in as client")
        else:
            st.error("Client authentication failed. Please check your credentials.")

    # For company personnel, provide a small button at the bottom
    st.markdown("---")  # Add a separator line
    personel = st.radio("Are you a company personnel?",["No","Yes"])
    if personel == "Yes":
        email = st.text_input("Email (@sidar.com)", key="company_email")
        password = st.text_input("Password", type="password", key="company_password")
        if st.button("Login as Company Personnel"):
            # Call the sidar personnel authentication endpoint
            payload = {"email": email}
            with open("personnel.json", "w") as json_file:
                json.dump(payload, json_file)

            headers = {"Content-Type": "application/json"}
            response = requests.post("http://20.20.16.145:5050/authenticate_director",data=json.dumps(payload),headers=headers)
            if response.status_code == 200:
                # Assuming the API returns a success status code
                st.success("Logged in as company personnel")
            else:
                st.error("Company personnel authentication failed. Please check your credentials.")




def questionnaire_page():
    st.subheader("Questionnaire")
    # Implement your questionnaire form here

def add_client_page():
    st.subheader("Add Client")
    # Implement your add client form here

def client_dashboard():
    st.subheader("Client Dashboard")
    # Display client-specific data and deadlines

def company_dashboard():
    st.subheader("Company Dashboard")
    # Display all current clients and their data, including deadlines

# # Example usage
if __name__ == '__main__':
    login_page()
#     if current_user.is_authenticated:
#         if current_user.role == "Company Personnel":
#             company_dashboard()
#             add_client_page()
#         elif current_user.role == "Client":
#             client_dashboard()
#             questionnaire_page()
