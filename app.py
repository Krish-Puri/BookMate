import streamlit as st
from PIL import Image

# --- Page Configuration ---
# Set the page title and icon. This should be the first Streamlit command.
st.set_page_config(
    page_title="BookMate",
    page_icon="📚"
)

# --- Sidebar for Preferences ---
# We'll put the user's preferences in a sidebar.
with st.sidebar:
    st.header("Your Reading Preferences")
    st.write("Enter your favorite authors, genres, or books to help us find a match.")
    
    # st.text_area is a multi-line text box.
    user_preferences = st.text_area(
        "I enjoy books like...", 
        key="user_prefs",
        placeholder="e.g., 'fast-paced sci-fi, books by Neil Gaiman, or anything about dragons'"
    )

# --- Main Page ---
st.title("📚 BookMate")
st.write("Take a photo of a bookshelf to get AI-powered recommendations!")

# st.file_uploader creates a drag-and-drop or browse-to-upload widget.
uploaded_file = st.file_uploader(
    "Upload a bookshelf image",
    type=["png", "jpg", "jpeg"],  # Restrict to image file types
    key="uploader"
)

# --- Logic to run when an image is uploaded ---
if uploaded_file is not None:
    # 'uploaded_file' is a file-like object. We use PIL to open it.
    image = Image.open(uploaded_file)
    
    # st.image displays the image in the app.
    st.image(image, caption="Your Uploaded Books", use_column_width=True)
    
    st.divider() # Adds a horizontal line

    # --- This is where our next steps will go ---
    st.subheader("Analysis Results")
    
    if user_preferences:
        # Check if the user has entered any preferences
        st.write("Analyzing the image based on your preferences...")
        # TODO: Add Google Vision API call here
        # TODO: Add Google Books API call here
        # TODO: Add AI recommendation call here
    else:
        # Prompt the user to fill in their preferences
        st.warning("Please enter your reading preferences in the sidebar to get recommendations.")