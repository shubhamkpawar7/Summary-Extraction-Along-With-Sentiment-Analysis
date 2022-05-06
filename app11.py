import streamlit as st

#NLP packages
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
nlp=spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')


import PyPDF2 

def sentiment_analyzer(my_text):
    
    docx= nlp(my_text)
    sentiment=docx._.polarity
    return sentiment
    
#pkgs


def main():
    st.title("Sentiment Analyzer")
    st.subheader("Let us check the Sentiment")
    
    #Sentiment_Analysis
    if st.checkbox("Show Sentiment of a Pdf File"):
        
        
        uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
        
        if uploaded_file is not None:
            a=PyPDF2.PdfFileReader(uploaded_file)
            

            b=a.getNumPages()

            str=""
            for i in range(1,b):
                str+= a.getPage(i).extractText()
                message=str
        if st.button("Analyze"):
            st.text("ANALYZING THE TEXT......")
            nlp_result= sentiment_analyzer(message)
            st.write(nlp_result)
           
            if nlp_result > 0:
                st.success("The Sentiment is postive")
            elif nlp_result == 0:
                 st.success("The Sentiment is neutral")
            else:
                st.success("The Sentiment is negative")
    # enter text sentiment
    if st.checkbox("Show Sentiment of Text"):
          
        message = st.text_area("Enter the Summary to be analysed",)
        if st.button("Analyzee"):
            nlp_result= sentiment_analyzer(message)
            st.write(nlp_result)
            
            if nlp_result > 0:
                st.success("The Sentiment is postive")
            elif nlp_result == 0:
                st.success("The Sentiment is neutral")
                
            else:
                st.success("The Sentiment is negative")                
                
                
                
st.sidebar.subheader("About the App")
st.sidebar.text("NLP BASED SENTIMENT ANLYSIS")

	
st.sidebar.subheader("By Group 5")
st.sidebar.info("Achyut Kumar")
st.sidebar.info("Shubham Pawar")
st.sidebar.info("Pranita Fulzele")            
st.sidebar.info("Dhanashri Desale")
st.sidebar.info("Renuka Muley")  
st.sidebar.info("Kirti Saindane")  
st.sidebar.info("Jayashri Patil")   


st.sidebar.subheader("Mentor:")
st.sidebar.info("Kartik Muskula")
                
                
if __name__ == '__main__':
    main()
