import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title = "Add New"
)

st.title("Add New 📝")

# Name input
name = st.text_input("Enter your name please: ")

# Identification options
identity_options = ["Student", "Professional", "University", "Firm"]
identification = st.selectbox("How would you like to register yourself as : ", options = identity_options)

# Skills options
skills_options = ['C', 'Chemistry', 'Mathematics', 'Relationship Development', 'Client Relations', 'Key Metrics', 'AnSys', 'SOLIDWORKS', 'Physics', 
                  'MATLAB', 'Manufacturing', 'Deposits', 'Data Warehousing', 'Patient Care', 'MySQL', 'CPR', 'Data Visualization', 
                  'Waste Disposal', 'Physical Therapy', 'SQL', 'Product Strategy', 'Rehabilitation', 'Cash Handling', 
                  'Data Analysis', 'Machine Design', 'Materials Science', 'Process Simulation', 'ETL', 'Manual Therapy', 
                  'Sports Medicine', 'Automation', 'Project Management', 'Engineering Management', 'Java', 
                  'Manufacturing Process', 'Databases', 'Latex', 'NLP', 'Fabrication', 'Python', 'C++', 'Dashboards', 
                  'Process Safety', 'CAD', 'JavaScript', 'Fitness', 'AutoCAD', 'Market Analysis', 'Customer Service', 
                  'System Design', 'Microsoft Office']

# Student Identification and Parameters
if identification == "Student":
    student_current_status_options = ["Junior", "Sophomore", "Senior", "Graduate Student", "Phd Candidate"]
    student_current_status = st.selectbox("What is the current level of study : ", options = student_current_status_options)

    # Education
    student_education_major = st.text_input("What is your current major of study")

    # University
    student_university_name = st.text_input("Which university you are studying in right now : ")

    # Clubs or Associations
    clubs_or_association = st.text_input("Are you part of any club or association, please specify one : ")

    # Job or Internship
    job_internship = "No"
    if student_current_status in ["Sophomore", "Senior", "Graduate Student", "Phd Candidate"]:
        Job_options = ["Yes", "No"]
        job_internship = st.selectbox("Are you looking for Job or Internship", options = Job_options)

    # students skills
    student_skills = st.multiselect("Can you please select 3 skills which you are good at : ", options = skills_options, max_selections = 3)

firm_skills = ['Engineering', 'Law', 'Natural Sciences', 'Management', 'Physical Sciences', 'Others', 'Software Development', 
               'Analytics', 'Cloud Services', 'Simulation', 'Research and Development', 'Data Analysis', 'Hardware', 'Banking']

firm_options = ["Engineering", "Research and Development", "Consultancy", "Law", "Bank", "Real Estate","Non Profit Organization"]

if identification == "Firm":
    firm_status = st.selectbox("What kind of firm are you : ", options = firm_options)

    firm_specializations = st.multiselect("Can you please select 3 areas in which you provide services", options = firm_skills, max_selections = 3)

university_skills = ['Engineering', 'Law', 'Natural Sciences', 'Management', 'Physical Sciences', 'Others']

if identification == "University":
    university_specialization = st.multiselect("Can you please select 3 areas in which you provide education", options = university_skills, max_selections=3)

if identification == "Professional":
    professional_firm_type = st.selectbox("What kind of firm you work at : ", options = firm_options)
    professional_firm_name = st.text_input("Can you please provide the name of your firm : ")

    professional_university_name = st.text_input("Which university you studied at?")

    professional_education_major = st.text_input("What was your major of study?")

    professional_clubs_assoc = st.text_input("Were you part of any clubs or association, please specify one : ")

    professional_skills = st.multiselect("Can you please select 3 skills which you are good at : ", options = skills_options, max_selections = 3)

contact_email = st.text_input("Please provide your contact email address : ")

def submit_all():
    if identification == "Student":
        element_vector = {
            "Name" : name,
            "Identification" : identification,
            "Current Status" : student_current_status,
            "Looking for Job or Internship" : job_internship,
            "Major" : student_education_major,
            "Tech Firm Name" : "",
            "Tech Firm Type" : "",
            "University Name" : student_university_name,
            "Club/Association" : clubs_or_association,
            "Contact" : contact_email,
            "Attribute1" : student_skills[0],
            "Attribute2" : student_skills[1],
            "Attribute3" : student_skills[2],
            "Record Timestamp" : datetime.now(),
            "Record Status" : "New"
        }
    
    if identification == "Professional":
        element_vector = {
            "Name" : name,
            "Identification" : identification,
            "Current Status" : "",
            "Looking for Job or Internship" : "",
            "Major" : professional_education_major,
            "Tech Firm Name" : professional_firm_name,
            "Tech Firm Type" : professional_firm_type,
            "University Name" : professional_university_name,
            "Club/Association" : professional_clubs_assoc,
            "Contact" : contact_email,
            "Attribute1" : professional_skills[0],
            "Attribute2" : professional_skills[1],
            "Attribute3" : professional_skills[2],
            "Record Timestamp" : datetime.now(),
            "Record Status" : "New"
        }

    if identification == "University":
        element_vector = {
            "Name" : name,
            "Identification" : identification,
            "Current Status" : "",
            "Looking for Job or Internship" : "",
            "Major" : "",
            "Tech Firm Name" : "",
            "Tech Firm Type" : "",
            "University Name" : "",
            "Club/Association" : "",
            "Contact" : contact_email,
            "Attribute1" : university_specialization[0],
            "Attribute2" : university_specialization[1],
            "Attribute3" : university_specialization[2],
            "Record Timestamp" : datetime.now(),
            "Record Status" : "New"
        }

    if identification == "Firm":
        element_vector = {
            "Name" : name,
            "Identification" : identification,
            "Current Status" : "",
            "Looking for Job or Internship" : "",
            "Major" : "",
            "Tech Firm Name" : "",
            "Tech Firm Type" : "",
            "University Name" : "",
            "Club/Association" : "",
            "Contact" : contact_email,
            "Attribute1" : firm_specializations[0],
            "Attribute2" : firm_specializations[1],
            "Attribute3" : firm_specializations[2],
            "Record Timestamp" : datetime.now(),
            "Record Status" : "New"
        }

    element_df = pd.DataFrame(data = element_vector, index = [0])

    # node color
    match identification:
        case "Student":
            node_color  = "#F29F05"
            node_shape = "dot"
            node_size = 15
        
        case "Professional":
            node_color = "#D96704"
            node_shape = "hexagon"
            node_size = 15
        
        case "University":
            node_color = "#F28D77"
            node_shape = "dot"
            node_size = 30
        
        case "Firm":
            node_color = "#F2B05E",
            node_shape = "dot",
            node_size = 30

    Node_vector = {
        "Name" : name,
        "Identification" : identification,
        "title" : name,
        "label" : name,
        "color" : node_color,
        "shape" : node_shape,
        "size" : node_size
    }

    Node_df = pd.DataFrame(data = Node_vector, index = [0])

    output_path = "Dataset.csv"
    element_df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index = False)

    Node_file_output_path = "Nodes.csv"
    Node_df.to_csv(Node_file_output_path, mode = 'a', header = not os.path.exists(Node_file_output_path), index = False)

    st.success('Your record has been added!', icon="✅")
    

st.button("Submit", on_click = submit_all)
