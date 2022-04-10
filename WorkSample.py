{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5ed8c7b7-d6cd-4dd8-87f0-587098cd8f78",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import base64"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "48f87236-5035-43c6-b601-d6aec85158f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-04-10 15:10:14.039 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\hkeim\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "#####################\n",
    "# Header \n",
    "st.write('''\n",
    "# Hannah Keim\n",
    "##### *Work Samples* \n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f9aff163-9bb6-4377-8792-b47e88aa0a11",
   "metadata": {},
   "outputs": [],
   "source": [
    "def st_display_pdf(pdf_file):\n",
    "    with open(pdf_file,\"rb\") as f:\n",
    "      base64_pdf = base64.b64encode(f.read()).decode('utf-8')\n",
    "    pdf_display = F'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'\n",
    "    st.markdown(pdf_display, unsafe_allow_html=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "af1428ca-4eb2-492e-aadb-670e35caf0b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Data Cleaning', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Data Cleaning Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c2e525ca-a662-43b6-a1cd-4b4ed45af6ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Multiple Linear Regression', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Multiple Regression Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cf51a0fa-d4c8-4a14-ae6c-90d8ec1f8dbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Logistic Regression', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Logistic Regression Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8764eb75-76bb-4611-8431-a0e3f1483ff0",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## KNN Classification', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/KNN Classification Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4bdc002a-d6bb-4751-a723-f4cdfaf09727",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## K-means Clustering', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/K-means Clustering Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fe492a3f-71c5-49bb-b8b3-5a9b01082f60",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Principal Component Analysis', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Principal Component Analysis Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "284c286f-8ae6-4589-a6a8-6f835818f56c",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Random Forest Classifier', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Random Forest Classifier Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "709750cc-a17a-4a5f-8466-05e7f81e088c",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Neural Network', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network for Sentiment Analysis.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Recurrent Neural Network Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "46ad1f92-fe6b-4036-b805-0986444fea32",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Time Series Analysis', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Report.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Time Series Analysis Code.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "25aadaab-9db7-40ad-8157-397043f0a805",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown('## Chi-Square Capstone', unsafe_allow_html=True)\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analyses of New York City Business Licenses.pdf\")\n",
    "st_display_pdf(\"C:/Users/hkeim/OneDrive/Documents/Worksamples/Chi-Square Analysis Executive Summary.pdf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4e220e0-6c7f-49a8-aec0-e6b8ebe2d4f1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
