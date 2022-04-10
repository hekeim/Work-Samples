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


st.markdown('## Data Cleaning', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Report.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Report.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## Multiple Linear Regression', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Report.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Report.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## Logistic Regression', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Report.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Report.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## KNN Classification', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Report.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Report.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## K-means Clustering', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## Principal Component Analysis', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Report.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Report.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”7Principal Component Analysis00″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## Random Forest Classifier', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Report.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Report.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## Neural Network', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network for Sentiment Analysis.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network for Sentiment Analysis.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## Time Series Analysis', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Report.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Report.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Code.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Code.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[5]:


st.markdown('## Chi-Square Capstone', unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analyses of New York City Business Licenses.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analyses of New York City Business Licenses.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def show_pdf("C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analysis Executive Summary.pdf"):
    with open("C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analysis Executive Summary.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# In[ ]:




