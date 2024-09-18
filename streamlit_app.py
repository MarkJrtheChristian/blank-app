import streamlit as st
from datetime import datetime
import requests


st.set_page_config(page_title="Comm Creator", page_icon=":bug:")

st.markdown("## Communication Creator")

# Drop down for type of issue
comm_type = st.selectbox(
    "Type of Communication", ("Executive Summary", "Status Page Communication", "Impact Statement")
)

# Date and time picker for Start time
#start_time = st.date_input("Start time -", datetime.now())

# Date and time picker for Notified time
#notified_time = st.date_input("Notified Time -", datetime.now())

# Input field for Ticket ID with a 10 character limit
ticket_id = st.text_input("Ticket ID", max_chars=10)

# Dropdown for Severity
severity = st.selectbox("Severity", ("Low", "Medium", "High"))

# Switch for "External to the company"
external_to_company = st.checkbox("External to the company")

# Text area for Description of the issue with a 3000 character limit
description = st.text_area("Description of the issue", max_chars=3000)


# Submit button
if st.button("Submit"):
   

            
    # Prepare the data to send to the Google Cloud function
    data = {
    "query": description + " " + ticket_id + " " + severity,
    #"start_time": "start time is " + start_time.isoformat(),
    #"notified_time": "notified time is " + notified_time.isoformat(),
    #"ticket_id": "Ticket ID is " + ticket_id,
    #"severity": "The severity is " + severity,
    #"external_to_company": "This issue is external to the company. ",
    #"description": description,
    }
    
    # Replace with your actual Google Cloud function endpoint URL
    cloud_function_url = "https://us-central1-testa-53w5j7.cloudfunctions.net/CommsCreatorCall"

    try:
    # Send the data to the Google Cloud function
        response = requests.post(cloud_function_url, json=data)
        print("this is doing something")
    # Handle the response from the Google Cloud function
        if response.status_code == 200:
    # Display the response from the Google Cloud function in a Markdown field

            #st.markdown("## Response from Google Cloud Function:")
            some_text = response.text.encode('ascii').decode('unicode-escape')
            new1_text = some_text.replace("\"", "")
            st.markdown(str(new1_text))
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")