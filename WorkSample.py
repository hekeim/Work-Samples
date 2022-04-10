#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import base64


# In[4]:


#####################
# Header 
st.write('''
# Hannah Keim
##### *Work Samples* 
''')


# In[19]:


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[22]:


st.markdown('## Data Cleaning', unsafe_allow_html=True)
st.write('''
##### *Report* 
''')
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='1'):            
        show_pdf("Data Cleaning Report.pdf")
with col2:
    st.button('Close PDF',key='2')
st.write('''
##### *Code* 
''')
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='3'):            
        show_pdf("Data Cleaning Code.pdf")
with col2:
    st.button('Close PDF',key='4')


# In[23]:


st.markdown('## Multiple Linear Regression', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='5'):            
        show_pdf("Multiple Linear Regression Report.pdf")
with col2:
    st.button('Close PDF',key='6') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='7'):            
        show_pdf("Multiple Linear Regression Code.pdf")
with col2:
    st.button('Close PDF',key='8')


# In[24]:


st.markdown('## Logistic Regression', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='9'):            
        show_pdf("Logistic Regression Report.pdf")
with col2:
    st.button('Close PDF',key='10') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='11'):            
        show_pdf("Logistic Regression Code.pdf")
with col2:
    st.button('Close PDF',key='12')


# In[25]:


st.markdown('## KNN Classification', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='13'):            
        show_pdf("KNN Classification Report.pdf")
with col2:
    st.button('Close PDF',key='14') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='15'):            
        show_pdf("KNN Classification Code.pdf")
with col2:
    st.button('Close PDF',key='16')


# In[26]:


st.markdown('## K-means Clustering', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='17'):            
        show_pdf("K-means Clustering.pdf")
with col2:
    st.button('Close PDF',key='18') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='19'):            
        show_pdf("K-means Clustering.pdf")
with col2:
    st.button('Close PDF',key='20')


# In[27]:


st.markdown('## Principal Component Analysis', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='21'):            
        show_pdf("Principal Component Analysis Report.pdf")
with col2:
    st.button('Close PDF',key='22') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='23'):            
        show_pdf("Principal Component Analysis Code.pdf")
with col2:
    st.button('Close PDF',key='24')


# In[28]:


st.markdown('## Random Forest Classifier', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='25'):            
        show_pdf("Random Forest Classifier Report.pdf")
with col2:
    st.button('Close PDF',key='26') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='27'):            
        show_pdf("Random Forest Classifier Code.pdf")
with col2:
    st.button('Close PDF',key='28')


# In[29]:


st.markdown('## Neural Network', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='29'):            
        show_pdf("Recurrent Neural Network for Sentiment Analysis.pdf")
with col2:
    st.button('Close PDF',key='30') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='31'):            
        show_pdf("Recurrent Neural Network Code.pdf")
with col2:
    st.button('Close PDF',key='32')


# In[30]:


st.markdown('## Time Series Analysis', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='33'):            
        show_pdf("Time Series Analysis Report.pdf")
with col2:
    st.button('Close PDF',key='34') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='35'):            
        show_pdf("Time Series Analysis Code.pdf")
with col2:
    st.button('Close PDF',key='36')


# In[31]:


st.markdown('## Market Basket Analysis', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='37'):            
        show_pdf("Market Basket Analysis.pdf")
with col2:
    st.button('Close PDF',key='38') 


# In[32]:


st.markdown('## Chi-Square Capstone', unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='39'):            
        show_pdf("Chi-Square Analyses of New York City Business Licenses.pdf")
with col2:
    st.button('Close PDF',key='40') 
col1, col2= st.columns(2)
with col1:  
    if st.button('Read PDF',key='41'):            
        show_pdf("Chi-Square Analysis Executive Summary.pdf")
with col2:
    st.button('Close PDF',key='42')


# In[ ]:




