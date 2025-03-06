
import os  # Import the os module to interact with the file system
import streamlit as st  # Import Streamlit for UI components
from pathlib import Path  # Import Path from pathlib for handling file paths

def rename_files(uploaded_files, prefix):
    try:
        for index, uploaded_file in enumerate(uploaded_files, start=1):  # Loop through uploaded files, starting index from 1
            file_extension = Path(uploaded_file.name).suffix  # Get the file extension
            new_name = f"{prefix}{index}{file_extension}"  # Create new filename using prefix and index

            with open(new_name, "wb") as f:  # Open a new file in write-binary mode
                f.write(uploaded_file.getbuffer())  # Write file content to the new file with the new name

        return "Files renamed and saved successfully!"  # Return success message        
    except Exception as e:
        return f"Error: {e}"  # Return error message if something goes wrong
    

# Streamlit UI
st.title("Bulk File Renamer by Samad")  # Set title for the Streamlit app

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

uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)  # File uploader for multiple files
prefix = st.text_input("Enter prefix for new filenames:", value="file_")  # Text input for filename prefix

if st.button("Rename and Save Files"):  # Button to trigger renaming
    if uploaded_files and prefix:  # Check if files are uploaded and prefix is provided
        result = rename_files(uploaded_files, prefix)  # Call rename function
        st.success(result)  # Display success message
    else:
        st.error("Please upload files and enter a prefix.")  # Show error message if inputs are missing
