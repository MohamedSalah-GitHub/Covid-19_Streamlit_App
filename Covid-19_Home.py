# Main Streamlit page
#  To run the app , !python -m streamlit run Covid-19_Home.py  ## this code is worrking to run 

import streamlit as st

st.title('Covid-19 Data Analysis')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')



with st.container():
    cal1 , cal2 =st.columns(2)
    with cal1:
        st.markdown('The World Health Organization (WHO) is a specialized agency of the United Nations responsible for international public health. It is headquartered in Geneva, Switzerland, and has six regional offices and 150 field offices worldwide.')
    with cal2 :
        # Image
        st.image('https://www.emro.who.int/images/stories/about-who/who_emro_logo_twitter.png', width=300)
# Image
st.image('https://raw.githubusercontent.com/MohamedSalah-GitHub/Covid-19_Streamlit_App/main/World_Health_Organisation_headquarters.jpg')

####################
#To import image from guthub , use below convertion rule 
#Original image link
#https://github.com/MohamedSalah-GitHub/Covid-19_Streamlit_App/blob/main/World_Health_Organisation_headquarters.jpg

#New Link , add "https://raw.githubusercontent.com/" at the begining and remove "/blob" from the midle
#https://raw.githubusercontent.com/MohamedSalah-GitHub/Covid-19_Streamlit_App/main/World_Health_Organisation_headquarters.jpg
################

# Descriptions
st.header('Description')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')