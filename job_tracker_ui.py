import pandas as pd
import streamlit as st
import os

FILENAME = "job_applications.csv"

# Load existing data or create new
if os.path.exists(FILENAME):
    df = pd.read_csv(FILENAME)
else:
    df = pd.DataFrame(columns=[
        "Date Applied",
        "Company",
        "Job Title",
        "Location",
        "Job URL",
        "Contact Person",
        "Contact Email",
        "Application Status",
        "Resume Version Used",
        "Cover Letter Used",
        "Follow-Up Date",
        "Notes"
    ])

st.title("📋 Job Application Tracker")

# Form to add a new application
with st.form("new_application"):
    st.subheader("➕ Add New Entry")
    date_applied = st.date_input("Date Applied")
    company = st.text_input("Company")
    job_title = st.text_input("Job Title")
    location = st.text_input("Location")
    job_url = st.text_input("Job URL")
    contact_person = st.text_input("Contact Person")
    contact_email = st.text_input("Contact Email")
    status = st.selectbox("Application Status", ["Applied", "Interviewing", "Offer", "Rejected"])
    resume = st.text_input("Resume Version Used")
    cover_letter = st.text_input("Cover Letter Used")
    follow_up_date = st.date_input("Follow-Up Date")
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Submit")
    if submitted:
        df.loc[len(df)] = [
            date_applied, company, job_title, location, job_url,
            contact_person, contact_email, status,
            resume, cover_letter, follow_up_date, notes
        ]
        df.to_csv(FILENAME, index=False)
        st.success("✅ Entry added!")

# Display the full table
st.subheader("📄 Tracked Applications")
st.dataframe(df)
