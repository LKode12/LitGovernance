import streamlit as st
import requests
import json

def main():
    st.title("Governace Questionnaire")
    st.write("Welcome to the SIDAR Governace Questionnaire, it has 55 questions.")
    # Add questions and choices
    email = st.text_input("Enter email")
    company_name = st.text_input("What comapany do yo work for?")
    purpose_1 = st.radio("1.There is an up-to-date board charter in place approprate to the life-stage of the organisation and its current structure.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_2 = st.radio("2.There is an up-to-date delegation of authority policy in place, which is effectively monitored.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_3 = st.radio("3.The managing director's report effectively communicates status, identifies issues, and clearly indicates a linkage to the business plan.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_4 = st.radio("4.Board packs are structured and used effectively to guide the board to make decisions and hold those authorised to make decisions accountable.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_5 = st.radio("5.The board calendar is up-to-date and relevant for the timing requirements of the enterprise and its strategic focus.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_6 = st.radio("6.All board meeting dates (and committee dates if applicable) for the year are scheduled in directors' diaries and align with the board calendar.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_7 = st.radio("7.The organisation has an up-to-date strategy (identifying the companies purpose and medium-term vision) and a business plan (identifying the necessary next steps) that guides its focus and direction.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_8 = st.radio("8.The board ensures a strategic focus in every board meeting to ensure that board papers relevant to the theme agreed upon for that meeting are prepared and that necessary key strategic issues are addressed proactively.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_9 = st.radio("9.There is clarity regarding the organisation's culture, values, and beliefs.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_10 = st.radio("10.The culture and values of the organisation are demonstrated by the board, setting the appropriate tone for the rest of the organisation to follow.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_11= st.radio("11.The board's conduct is characterised by trust, respect, candour, professionalism, accountability, diligence and commitment.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    purpose_12= st.radio("12.The organisation has developed a culture of accountability for performance.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    #There are going to be hidden
    comittee_structure = st.radio("13.The board has committee structures in place",["Yes","No"])
    if comittee_structure =="Yes":
        purpose_13= st.radio("a.The board committees have approved terms of reference.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
        purpose_14= st.radio("b.The board committees have an agreed work plan for the year and are making good progress against that plan.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_1= st.radio("14.The chairman and managing director meet before every board meeting, and this engagement delivers value to the board's focus and preparation, as well as enhancing the relationship between the board and management.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_2= st.radio("15.Independent directors meet before every board meeting and utilise this engagement to focus on value creation and enhance effective governance implementation.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_3= st.radio("16.The board is effective at passing resolutions based on thorough discussions and the information presented in board papers.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_4= st.radio("17.Shareholder-managers demonstrate their acceptance of the authority of the board.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_5= st.radio("18.There is a succession plan in place for the chief executive and this plan is proceeding as designed.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_6= st.radio("19.The chief executive/managing director has KPIs (Key Performance Indicators) in place and is held accountable for their performance against these indicators.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_7= st.radio("20.Board papers are distributed to the board at least seven working days prior to each board meeting.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_8= st.radio("21.An updated performance or measurement dashboard is provided in every set of board papers.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_9= st.radio("22.The measurement dashboard is used effectively and enables to board to predict the likely future performance of the organisation.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_10= st.radio("23.The chief executive/managing director's report is well-designed to be substantially comprehensive and provide an accurate reflection of the performance of the organisation. ", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_11= st.radio("24.Every board meeting takes place.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_12= st.radio("25.Directors attend every scheduled board meeting.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_13= st.radio("26.All directors of the board are prompt at reviewing circulated minutes and providing feedback, ideally within two working days. ", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    accountability_14= st.radio("27.Directors are rotated every three years or as per the board charter.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_1= st.radio("28.All relevant and strategic (material) internal and external stakeholders have been identified", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_2= st.radio("29.Stakeholder requirements (needs, interests, and expectations) are regularly assessed and understood to ensure the delivery of long-term, sustainable benefits.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_3= st.radio("30.There is a strategic approach to stakeholder engagement that ensures that the board and the rest of the organisation engage with stakeholders appropriately.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_4= st.radio("31.The organisation holds an annual general meeting every year.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_5= st.radio("32.The annual general meeting is effective at formally engaging shareholders.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_6= st.radio("33.The expectations of shareholders are understood, including both financial and non-financial outcomes, and the board manages these expectations so that they are more realistic where necessary.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_7= st.radio("34.The value that the organisation seeks is sustainable over time and meets the needs and expectations of shareholders, stakeholders and interested parties alike.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_8= st.radio("35.The audited annual financial statements are available for the previous year-end.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_9= st.radio("36.The board has determined the organisation's risk appetite and tolerance levels across all dimensions of the organisation's operations and performance.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_10= st.radio("37.A risk framework has been defined and implemented in line with this risk appetite and tolerance.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_11= st.radio("38.This risk framework facilitates the regular examination of both the internal operations of the organisation and the external environment to identify risks and implement mitigation strategies", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_12= st.radio("39.All risks are managed appropriately in line with the risk management framework.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_13= st.radio("40.The organisation acts in a socially responsible manner and delivers on its CSR (Community Social Responsibility) plan.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    sustainability_14= st.radio("41.The organisation operates in an environmentally sustainable manner and reports on its environmental impact.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_1= st.radio("42.Directors understand the contents of the organisation’s incorporation and founding documents (organisation constitution or memorandum of incorporation or other such documents).", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_2= st.radio("43.The appointed directors have been duly registered as directors of the organisation with the relevant companies' commission.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_3= st.radio("44.Each board director maintains an up-to-date conflict of interest register.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_4= st.radio("45.The organisation’s directors’ and officers’ liability insurance is current and sufficient.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_5= st.radio("46.There is a regular policy review process that enables the board to recieves, review and approves both new and updated organisation policies on a regular basis.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_6= st.radio("47.The board, and each individual director, understand the financial model, activities and performance of the organisation.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_7= st.radio("48.The monthly financial measures that are tracked are up-to-date and actively monitored.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_8= st.radio("49.The financial report includes an income statement, balance sheet, cash flow forecast and financial ratios.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_9= st.radio("50.The monthly financial reports indicate that profitability, business value and solvency are improving.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_10= st.radio("51.The organisation has met solvency requirements.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_11= st.radio("52.The executive team has the necessary financial understanding and competence, supported by a finance manager, chief financial officer or outsourced provide who leads this element of the organisation's management.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_12= st.radio("52.An objective and regular operational assessment is actively used to monitor and evaluate organisation performance and focus ongoing improvement activity within the organisation.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_13= st.radio("54.An objective and regular governance assessment or evaluation is actively used by the board to monitor its own performance and cultivate a culture of continuous improvement of the board.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    comformance_14= st.radio("55.Directors regularly attend director training and continuous professional development, and demonstrate their commitment to continuous learning.", ["Fully in place","Largely in Place", "Some Elements", "Minimal", "Non-Existent"])
    t_n_c = st.checkbox("Do you agree to the T&Cs")

    # add purpose to reponse dict
    
    responses = {
        "purpose_1":purpose_1,
        "purpose_2":purpose_2,
        "purpose_3":purpose_3,
        "purpose_4":purpose_4,
        "purpose_5":purpose_5,
        "purpose_6":purpose_6,
        "purpose_7":purpose_7,
        "purpose_8":purpose_8,
        "purpose_9":purpose_9,
        "purpose_10":purpose_10,
        "purpose_11":purpose_11,
        "purpose_12":purpose_12
    }
    if comittee_structure =="Yes":
        responses["purpose_13"] = purpose_13
        responses["purpose_14"] = purpose_14
    else:
        responses["purpose_13"] = "null"
        responses["purpose_14"] = "null"
        
    #add accountability to response dict
    
    responses["accountability_1"] = accountability_1
    responses["accountability_2"] = accountability_2
    responses["accountability_3"] = accountability_3
    responses["accountability_4"] = accountability_4
    responses["accountability_5"] = accountability_5
    responses["accountability_6"] = accountability_6
    responses["accountability_7"] = accountability_7
    responses["accountability_8"] = accountability_8
    responses["accountability_9"] = accountability_9
    responses["accountability_10"] = accountability_10
    responses["accountability_11"] = accountability_11
    responses["accountability_12"] = accountability_12
    responses["accountability_13"] = accountability_13
    responses["accountability_14"] = accountability_14
    
    #add sustainability to response dict
    
    responses["sustainability_1"] = sustainability_1
    responses["sustainability_2"] = sustainability_2
    responses["sustainability_3"] = sustainability_3
    responses["sustainability_4"] = sustainability_4
    responses["sustainability_5"] = sustainability_5
    responses["sustainability_6"] = sustainability_6
    responses["sustainability_7"] = sustainability_7
    responses["sustainability_8"] = sustainability_8
    responses["sustainability_9"] = sustainability_9
    responses["sustainability_10"] = sustainability_10
    responses["sustainability_11"] = sustainability_11
    responses["sustainability_12"] = sustainability_12
    responses["sustainability_13"] = sustainability_13
    responses["sustainability_14"] = sustainability_14
    
    #add comformance ro response dict
    responses["comformance_1"] = comformance_1
    responses["comformance_2"] = comformance_2
    responses["comformance_3"] = comformance_3
    responses["comformance_4"] = comformance_4
    responses["comformance_5"] = comformance_5
    responses["comformance_6"] = comformance_6
    responses["comformance_7"] = comformance_7
    responses["comformance_8"] = comformance_8
    responses["comformance_9"] = comformance_9
    responses["comformance_10"] = comformance_10
    responses["comformance_11"] = comformance_11
    responses["comformance_12"] = comformance_12
    responses["comformance_13"] = comformance_13
    responses["comformance_14"] = comformance_14
    
    if t_n_c:
        responses["T_&_Cs"] = True
    else:
        responses["T_&_Cs"] = False
    response_json={
        "company":company_name,
        "email":email,
        "reponse":responses
    }
    
    # st.write(response_json)
    
    # Add a submit button
    if st.button("Submit"):
        # Store the responses in a JSON file
        with open("responses.json", "w") as json_file:
            json.dump(response_json, json_file)

        url = "http://20.20.16.145:5050/responses" 
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(response_json), headers=headers)

        # Display a success message
        if response.status_code == 200:
            st.success("Data submitted successfully!")
        else:
            st.error("Error submitting data. Please try again.")

if __name__ == "__main__":
    main()
