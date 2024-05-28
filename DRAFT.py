import streamlit as st

# Set page title and icon
st.set_page_config(
    page_title='DRAFT',
    page_icon=r'C:\Users\beezl\OneDrive\Documents\Purwadhika\Modul_3\Portofolio\DRAFT_icon.png'
)

# Page title and description
st.image(r'C:\Users\beezl\OneDrive\Documents\Purwadhika\Modul_3\Portofolio\DRAFT_logo.png')
st.markdown('''
**DRAFT** stands for Dota 2 Recommendation And Feature Tool. It is a sophisticated system designed to enhance your Dota 2 gaming experience by providing tailored hero recommendations and insightful features.

How Does **DRAFT** Work?

**DRAFT** employs advanced algori   thms, including content-based filtering and cosine similarity 
calculations, to analyze your gameplay preferences. It suggests alternative heroes based on 
similarities in roles, primary attributes, and attack types with your current favorite hero. 
This personalized approach ensures that the recommendations are not only relevant but also resonate with your gameplay style.

Unique Features of **DRAFT**:

Tier Labels: **DRAFT** includes tier labels for heroes, derived from data in the Dota 2 pro scene.
Using agglomerative clustering, heroes are categorized into 4 tiers (S, A, B, C). These labels 
enhance the relevance of recommendations, considering the current meta and hero effectiveness at a competitive level.

Personalized Recommendations: By understanding your favorite hero and playstyle, **DRAFT** provides you
with the top 5 hero recommendations, tailored to your preferences. This feature helps you discover 
new heroes that match your gameplay style.

Competitive Edge: With **DRAFT**, you can stay ahead in the game by leveraging its comprehensive analysis 
and recommendations. Whether you're a casual player or aiming for the competitive scene, **DRAFT** can help 
you make informed decisions and improve your performance.

In conclusion, **DRAFT** is your ultimate companion in the world of Dota 2, offering personalized 
recommendations and features to enhance your gameplay and elevate your gaming experience.
''')

# Sidebar
st.sidebar.success('Select a page above')

# Add more content or sections as needed
