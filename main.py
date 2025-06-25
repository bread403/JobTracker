import pandas as pd
from ace_tools import display_dataframe_to_user

# Create a job application tracking template
job_applications_template = pd.DataFrame(columns=[
    "Date Applied",
    "Company",
    "Job Title",
    "Location",
    "Job URL",
    "Contact Person",
    "Contact Email",
    "Application Status",  # e.g., Applied, Interviewing, Offer, Rejected
    "Resume Version Used",
    "Cover Letter Used",
    "Follow-Up Date",
    "Notes"
])

# Display to user
display_dataframe_to_user("Job Application Tracker Template", job_applications_template)
