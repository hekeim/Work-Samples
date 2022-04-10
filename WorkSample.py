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


# In[5]:


def st_display_pdf(pdf_file):
    with open(pdf_file,"rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[6]:


st.markdown('## Data Cleaning', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Code.pdf")


# In[7]:


st.markdown('## Multiple Linear Regression', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Code.pdf")


# In[8]:


st.markdown('## Logistic Regression', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Code.pdf")


# In[11]:


st.markdown('## KNN Classification', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Code.pdf")


# In[12]:


st.markdown('## K-means Clustering', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering Code.pdf")


# In[13]:


st.markdown('## Principal Component Analysis', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Code.pdf")


# In[14]:


st.markdown('## Random Forest Classifier', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Code.pdf")


# In[15]:


st.markdown('## Neural Network', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network for Sentiment Analysis.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network Code.pdf")


# In[16]:


st.markdown('## Time Series Analysis', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Report.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Code.pdf")


# In[17]:


st.markdown('## Chi-Square Capstone', unsafe_allow_html=True)
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analyses of New York City Business Licenses.pdf")
st_display_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analysis Executive Summary.pdf")


# In[ ]:




