import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd
import numpy as np
from itertools import chain
from scipy.spatial.distance import euclidean, hamming
import os
import warnings
warnings.filterwarnings('ignore')

st.title("Buffalo Network 🗺️")

# reading the Nodes list
try:
    Node_df = pd.read_csv("Nodes.csv")
    data_df = pd.read_csv("Dataset.csv")
except Exception as e:
    st.info("No records to show.")

nodes = []
edges = []

########################## Experimental Code ##########################################

Engineering = ["AnSys", "AutoCAD", "Automation", "CAD", "Fabrication", "Latex", "MATLAB", "Machine Design", "Manufacturing", "Microsoft Office", "MySQL", "Python", "SOLIDWORKS", "System Design"]
Law = ["Microsoft Office"]
Natural_Sciences = ["Microsoft Office"]
Management = ["Client Relations", "Customer Service", "Engineering Management", "Key Metrics", "Market Analysis", "Microsoft Office", "Product Strategy", "Project Management", "Relationship Development"]
Physical_Sciences = ["CPR", "Fitness", "Manual Therapy", "Microsoft Office", "Patient Care", "Physical Therapy", "Rehabilitation", "Sports Medicine"]
Others = ["Mathematics", "Microsoft Office", "Physics", "Process Safety", "Process Simulation", "Waste Disposal"]
Software_Development = ["C", "C++", "Databases", "ETL", "Java", "JavaScript", "Latex", "MATLAB", "Microsoft Office", "MySQL", "NLP", "Python", "SQL", "System Design"]
Analytics = ["Dashboards", "Data Analysis", "Data Visualization", "Data Warehousing", "Market Analysis", "Mathematics", "Microsoft Office", "NLP", "Python", "SQL"]
Cloud_Services = ["Data Visualization", "Python", "SQL"]
Simulation = ["Data Analysis", "Data Visualization", "MATLAB", "Manufacturing Process", "Microsoft Office", "Process Simulation", "Python"]
Research_and_Development = ["Chemistry", "Data Analysis", "Data Visualization", "Market Analysis", "Materials Science", "Mathematics", "Microsoft Office", "MySQL", "Process Simulation", "Python", "SQL", "Waste Disposal"]
Data_Analysis = ["Dashboards", "Data Analysis", "Data Visualization", "Data Warehousing", "Databases", "Microsoft Office", "MySQL", "NLP", "Python", "SQL"]
Hardware = ["Machine Design", "Manufacturing", "Microsoft Office", "Process Safety", "SOLIDWORKS", "System Design"]
Banking = ["Cash Handling", "Client Relations", "Customer Service", "Deposits", "Microsoft Office"]

Skills_dict = {
    "Engineering" : Engineering,
    "Law" : Law,
    "Natural Sciences" : Natural_Sciences,
    "Management" : Management,
    "Physical Sciences" : Physical_Sciences,
    "Others" : Others,
    "Software Development" : Software_Development,
    "Analytics" : Analytics,
    "Cloud Services" : Cloud_Services,
    "Simulation" : Simulation,
    "Research and Development" : Research_and_Development,
    "Data Analysis" : Data_Analysis,
    "Hardware" : Hardware,
    "Banking" : Banking
}

Student_Professional_df = data_df[(data_df["Identification"] == "Student") | (data_df["Identification"] == "Professional")]

temp_list = ['Identification', 'Current Status', 'Looking for Job or Internship', 'Major', 'Tech Firm Name',
       'Tech Firm Type', 'University Name', 'Club/Association', 'Attribute1', 'Attribute2', 'Attribute3']

zero_vector_list = []
for column in temp_list:
    zero_vector_list.append(Student_Professional_df[column].unique())

zero_vector_list = list(chain.from_iterable(zero_vector_list))
zero_vector = {item : 0 for item in zero_vector_list}

print(zero_vector)

Student_Professional_df.fillna("No Data", inplace = True)

People_df = pd.DataFrame(zero_vector, index = Student_Professional_df["Name"])

for idx, data in Student_Professional_df.iterrows():
    #print("Student Profile : ")
    #print("Name : ", data["Name"])
    try:
        # update Identification
        People_df.loc[data["Name"]][data["Identification"]] += 1
    
    except Exception as e:
        pass
    
    try:
        # Update current Status
        People_df.loc[data["Name"]][data['Current Status']] += 1
    except Exception as e:
        pass
    
    try:
        # Update jobs or Internship Status
        if data["Looking for Job or Internship"].strip() == "Yes":
            People_df.loc[data["Name"]]["Job/Yes"] += 2
        else:
            People_df.loc[data["Name"]]["Job/No"] += 1
    except Exception as e:
        pass
        
    try:
        # Update Major
        #print("Major : ", data["Major"])
        People_df.loc[data["Name"]][data["Major"]] += 1
        
    except Exception as e:
        pass
        
    try:
        # Update Tech Firm
        People_df.loc[data["Name"]][data["Tech Firm Name"]] += 1
        
    except Exception as e:
        pass
        
    try:
        # Update University Name
        People_df.loc[data["Name"]][data["University Name"]] += 2
        
    except Exception as e:
        pass
    
    try:
        # School
        People_df.loc[data["Name"]][data["School"]] += 2
        
    except Exception as e:
        pass
        
    try:
        # Clubs or Associations
        People_df.loc[data["Name"]][data["Club/Association"]] += 1
        
    except Exception as e:
        pass
        
    
    #print("Attribute 1", data["Attribute1"])
    for k in Skills_dict.keys():
        try:
            #print(k)
            temp_index = Skills_dict[k].index(data["Attribute1"])
            #print("A1 temporary index : ", temp_index)
            if temp_index != -1:
                People_df.loc[data["Name"]][k] += 1
        except Exception as e:
            pass
    
    # Attribute 2
    #print("Attribute 2", data["Attribute2"])
    for k in Skills_dict.keys():
        try:
            #print(k)
            temp_index = Skills_dict[k].index(data["Attribute2"])
            #print("A2 temporary index", temp_index)
            if temp_index != -1:
                People_df.loc[data["Name"]][k] += 1
        except Exception as e:
            pass

    # Attribute 3
    #print("Attribute 3", data["Attribute3"])
    for k in Skills_dict.keys():
        try:
            temp_index = Skills_dict[k].index(data["Attribute3"])
            #print("A3 temporay index", temp_index)
            if  temp_index != -1:
                People_df.loc[data["Name"]][k] += 1
        except Exception as e:
            pass

def calculate_distance(vector1, vector2):
    euclids_dist, hams_dist = euclidean(vector1, vector2) * 10, hamming(vector1, vector2) * 10
    return round(euclids_dist, 3)

def search_and_sort(person_name):
    #print(person_name)
    Identity = Student_Professional_df[Student_Professional_df["Name"] == person_name]["Identification"].values[0]
    C_Status = Student_Professional_df[Student_Professional_df["Name"] == person_name]["Current Status"].values[0]
    
    #print(Identity, C_Status)
    
    Potential_Matches = Student_Professional_df[(Student_Professional_df["Identification"] == Identity) & (Student_Professional_df["Current Status"] == C_Status)]["Name"].values.tolist()
    Potential_Matches.remove(person_name)
    
    distances = {}
    Neighbors = {}
    
    for name in Potential_Matches:
        distances[name] = calculate_distance(People_df.loc[person_name], People_df.loc[name])
        #weights.append(calculate_distance(People_df.loc[person_name], People_df.loc[name]))
        
    distances = dict(sorted(distances.items(), key = lambda items: items[1], reverse = True))
    Neighbors[person_name] = list(distances.items())[:3]
    
    return distances

#print(search_and_sort("B"))
Student_Professional_df["Neighbors"] = Student_Professional_df["Name"].apply(lambda x: search_and_sort(x))


for idx, person_data in Student_Professional_df.iterrows():
    for neighbor, length in person_data["Neighbors"].items():
        edges.append(
            Edge(
                source = person_data["Name"],
                target = neighbor,
                arrows_to = False,
                arrows_from = False,
                length = length,
                color = "gray"
            )
        )

########################## Experimental Code Ends #####################################



nodes.append( Node(id="Buffalo",
                    title="Buffalo, NY", 
                    label="Buffalo, NY", 
                    size=40,
                    color = "#91CDF2", 
                    shape="dot") 
                )

for idx, node in Node_df.iterrows():

    nodes.append(
        Node(
            id = node["Name"],
            title = node["Identification"],
            label = node["Name"],
            size = node["size"],
            color = node["color"],
            shape = node["shape"]
        )
    )

    if node["Identification"] in ["University", "Firm"]:
        edges.append(
            Edge(
                source = node["Name"],
                target = "Buffalo",
                arrows_to = False,
                arrows_from = False
            )
        )

    if node["Identification"] in ["Student"]:
        edges.append(
            Edge(
                source = node["Name"],
                target = data_df[data_df["Name"] == node["Name"]]["University Name"].values[0],
                arrows_to = False,
                arrows_from = False,
                color = "#ffffff",
                length = 40
            )
        )
    
    if node["Identification"] in ["Professional"]:
        edges.append(
            Edge(
                source = node["Name"],
                target = data_df[data_df["Name"] == node["Name"]]["Tech Firm Name"].values[0],
                arrows_to = False,
                arrows_from = False,
                color = "#ffffff",
                length = 40
            )
        )

config = Config(width=950,
                height=500,
                directed=True, 
                physics=True, 
                hierarchical=False,
            )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)