import os  # Import the os module to interact with the file system
import streamlit as st  # Import Streamlit for UI components
from urllib.parse import urlparse  # Import urlparse to extract filename from URL
import requests  # Import requests to download files from URLs

def rename_file(url, prefix):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            parsed_url = urlparse(url)  # Parse the URL
            original_filename = os.path.basename(parsed_url.path)  # Extract filename from URL
            file_extension = os.path.splitext(original_filename)[1]  # Get file extension
            new_name = f"{prefix}{file_extension}"  # Create new filename with prefix
            
            with open(new_name, "wb") as f:
                f.write(response.content)  # Save the file with the new name
            
            return new_name  # Return renamed file name
        else:
            return None
    except Exception as e:
        return None

# Streamlit UI
st.title("File Renamer from URL")  # Set title for the Streamlit app

# Custom CSS for black background
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True  # Allow unsafe HTML for custom styling
)

# URL input
url = st.text_input("Enter file URL:")  # Input field for file URL
prefix = st.text_input("Enter prefix for new filename:", value="file_")  # Text input for filename prefix

if st.button("Download and Rename File"):  # Button to trigger renaming
    if url and prefix:
        renamed_file = rename_file(url, prefix)  # Call rename function
        if renamed_file:
            st.success("File renamed successfully! Click below to download.")
            with open(renamed_file, "rb") as f:
                st.download_button(label=f"Download {renamed_file}", data=f, file_name=renamed_file)  # Provide download link
        else:
            st.error("Failed to download or rename the file. Check the URL.")
    else:
        st.error("Please enter a valid URL and a prefix.")  # Show error message if inputs are missing
# import os  # Import the os module to interact with the file system
# import streamlit as st  # Import Streamlit for UI components
# from pathlib import Path  # Import Path from pathlib for handling file paths

# def rename_files(uploaded_files, prefix):
#     try:
#         for index, uploaded_file in enumerate(uploaded_files, start=1):  # Loop through uploaded files, starting index from 1
#             file_extension = Path(uploaded_file.name).suffix  # Get the file extension
#             new_name = f"{prefix}{index}{file_extension}"  # Create new filename using prefix and index

#             with open(new_name, "wb") as f:  # Open a new file in write-binary mode
#                 f.write(uploaded_file.getbuffer())  # Write file content to the new file with the new name

#         return "Files renamed and saved successfully!"  # Return success message        
#     except Exception as e:
#         return f"Error: {e}"  # Return error message if something goes wrong
    

# # Streamlit UI
# st.title("Bulk File Renamer by Samad")  # Set title for the Streamlit app

# # Custom CSS for black background
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: black;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True  # Allow unsafe HTML for custom styling
# )

# uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)  # File uploader for multiple files
# prefix = st.text_input("Enter prefix for new filenames:", value="file_")  # Text input for filename prefix

# if st.button("Rename and Save Files"):  # Button to trigger renaming
#     if uploaded_files and prefix:  # Check if files are uploaded and prefix is provided
#         result = rename_files(uploaded_files, prefix)  # Call rename function
#         st.success(result)  # Display success message
#     else:
#         st.error("Please upload files and enter a prefix.")  # Show error message if inputs are missing
