# import streamlit as st
# import pymongo
# import json
# from bson import ObjectId
# from bson import *
# from streamlit_quill import st_quill
# from pymongo.server_api import ServerApi
# # from helper import Helper
# from pages.Login import authenticator

# # if not Helper.get_authen_status():
# #     st.warning("Please login first!")
# #     st.stop()

# name, authentication_status, username = authenticator.login(location="unrendered")


# def get_json_content(file_path: str) -> dict:
#     """
#     Get the content of json file consists of raw data

#     Agrs:
#         file_path (str): path to the file want to get content
#     Output:
#         dictionary is the content of the raw file
#     """

#     try:
#         f = open(file=file_path)
#         return json.load(f)
#     except:
#         raise f"File {file_path} not foud"


# # MongoDB setup
# client = pymongo.MongoClient("mongodb+srv://root:123@cluster0.ss6bc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", server_api=ServerApi('1'))
# db = client['database']
# collection = db['new_info_DN']

# def get_json_from_mongo(doc_id):
#     document = collection.find_one({"_id": ObjectId(doc_id)})
#     return document

# # Function to get all the current ids in the MongoDB
# def get_all_id():
#     """
#     To get all the ids group by their category from all config cluster's docs
#     Output:
#         (dict): a dictionary with key is the category and value is the list of ids
#     """

#     ids = {}
#     for doc in collection.find():
#         if "ID" in doc:
#             if doc["Category"] not in ids:
#                 ids[doc["Category"]] = {}
#             ids[doc["Category"]][doc["ID"]] = doc["_id"]             
#     return ids




# # Function to generate a unique key for the form
# def gen_key(doc_id: str, inf_name: str) -> str:
#     return f"{doc_id}_{inf_name}"

# # doc_id = "66c8473ebb5746bb1e9768e1"



# with st.sidebar:
#     ids_by_category = get_all_id()
#     st.title("Verify data platform")
#     categories = ids_by_category.keys()
#     category = st.sidebar.selectbox("Choose a category", categories)


# html_id = st.selectbox("Choose a document to veify", ids_by_category[category].keys())
# doc_id =  ids_by_category[category][html_id]

# content = get_json_from_mongo(doc_id)


# with st.form(key=gen_key(doc_id, "form")):
#     # Display the title
#     st.title(f"Edit the content of document with ID {doc_id}")

#     # if content["verified_info_fromDN"]["is_verified"]:
#     #     st.success("You have verified this document")
    
#     # Loop through the content dictionary
#     for key, value in content.items():
#         if key == "Link hình ảnh":
#             st.write(f"**{key}**")
#             # Display image links
#             for img_url in value:
#                 st.image(img_url, use_column_width=True)
#         elif isinstance(value, str):
#             st.write(f"**{key}**")
#             # Allow editing of text content
#             content[key] = st.text_area(label=f"Edit {key}", value=value, height=150)
#         elif isinstance(value, list):
#             st.write(f"**{key}**")
#             # For lists of images, handle them specifically
#             for i, item in enumerate(value):
#                 st.write(f"{i + 1}. {item}")
#                 # Allow editing of list items if needed
#                 value[i] = st.text_input(f"Edit link {i + 1}", value=item)
#         elif isinstance(value, dict):
#             st.write(f"**{key}**")
#             # Handle nested dictionaries if needed
#             st.write(value)

#     # Add checkboxes for verification and editing status
#     st.write("**Verification Status**")
#     is_verified = st.checkbox("Verified", value=content.get("is_verified", False))
#     content["is_verified"] = is_verified

#     st.write("**Edit Status**")
#     is_edited = st.checkbox("Edited", value=content.get("is_edited", False))
#     content["is_edited"] = is_edited

#     submit = st.form_submit_button("Save Changes")

#     # if submit:
#     #     # Save changes to MongoDB
#     #     collection.update_one({"_id": ObjectId(doc_id)}, {"$set": content})
#     #     st.success("Changes saved successfully!")







# # with st.sidebar:
# #     st.title("Verify data platform")
# #     cate = st.selectbox("Choose a category", list(ids.keys()))
# #     category_ids = ids[cate]

# # id = st.selectbox("Choose a document to veify", category_ids)

# # file = open(f"data/{id}.json")
# # data = json.load(file)
# # st.markdown(data)



# New code

import streamlit as st
import pymongo
import json
from bson import ObjectId
from bson import *
from streamlit_quill import st_quill
from pymongo.server_api import ServerApi
 
 
 
def get_json_content(file_path: str) -> dict:
    """
    Get the content of json file consists of raw data
 
    Agrs:
        file_path (str): path to the file want to get content
    Output:
        dictionary is the content of the raw file
    """
 
    try:
        f = open(file=file_path)
        return json.load(f)
    except:
        raise f"File {file_path} not foud"
 
 
# MongoDB setup
client = pymongo.MongoClient("mongodb+srv://root:123@cluster0.ss6bc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", server_api=ServerApi('1'))
db = client['database']
collection = db['new_info_DN']
 
 
 
# Function to get all the current ids in the MongoDB
def get_all_id():
    """
    To get all the ids group by their category from all config cluster's docs
    Output:
        (dict): a dictionary with key is the category and value is the list of ids
    """
 
    ids = {}
    for doc in collection.find():
        if "ID" in doc:
            if doc["Category"] not in ids:
                ids[doc["Category"]] = {}
            ids[doc["Category"]][doc["ID"]] = doc["_id"]
    return ids
 
 
 
 
def get_json_from_mongo(doc_id):
    document = collection.find_one({"_id": ObjectId(doc_id)})
    return document
 
# Tạo một key duy nhất cho form
def gen_key(doc_id: str, inf_name: str) -> str:
    return f"{doc_id}_{inf_name}"
 
# Sidebar để chọn document
with st.sidebar:
    ids_by_category = get_all_id()
    st.title("Verify data platform")
    categories = ids_by_category.keys()
    category = st.sidebar.selectbox("Choose a category", categories)
 
 
html_id = st.selectbox("Choose a document to veify", ids_by_category[category].keys())
doc_id =  ids_by_category[category][html_id]
 
 
 
 
content = get_json_from_mongo(doc_id)
 
# Tạo danh sách các phần cần chỉnh sửa dựa trên category
edit_fields = []
 
if category == "Khách sạn":
    edit_fields = [
        ("verified_info_fromDN", "content", "Content"),
        ("new_info", "Giới thiệu", "Giới thiệu"),
        ("new_info", "Các loại phòng", "Các loại phòng")
    ]
elif category == "Nhà hàng":
    edit_fields = [
        ("verified_info_fromDN", "content", "Content"),
        ("new_info", "Giới thiệu", "Giới thiệu"),
        ("new_info", "Các món ăn", "Các món ăn")
    ]
else:
    edit_fields = [
        ("verified_info_fromDN", "content", "Content"),
        ("new_info", "Giới thiệu", "Giới thiệu")
    ]
 
# Main form để chỉnh sửa
with st.form(key=gen_key(doc_id, "form")):
    st.title("Thông tin")
    
    for section, field, label in edit_fields:
        if section in content and field in content[section]:
            st.write(f"**{label}**")
            content[section][field] = st.text_area(label=f"Edit {label}", value=content[section][field], height=150)
 
    submit = st.form_submit_button("Save Changes")
    if submit:
        # Lưu thay đổi vào MongoDB
        update_fields = {}
        if "new_info" in content:
            update_fields["new_info.Giới thiệu"] = content["new_info"].get("Giới thiệu", "")
        if "verified_info_fromDN" in content:
            update_fields["verified_info_fromDN.content"] = content["verified_info_fromDN"].get("content", "")
        collection.update_one({"_id": ObjectId(doc_id)}, {"$set": update_fields})
        st.success("Content saved successfully!")
 