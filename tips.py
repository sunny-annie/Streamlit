import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Tips Research",
    page_icon="💸")

site_header = st.container()
dataset = st.container()
new_features = st.container()

with site_header:
    st.title('This Is Tips Dataset Analysis')
    st.write('This data analysis is based on a ***tips.csv*** dataset.')

with dataset:
    st.header('Dataset introduction')
    st.write('The first few lines of the dataset look the following:')

    path = '/home/anya/ds_bootcamp/ds-phase-0/learning/datasets/tips.csv'
    tips = pd.read_csv(path, index_col='Unnamed: 0')
    st.write(tips.head())
    st.write(
        '''We have **total_bill** column, **tip** with the tip size, **sex** indicating the sex of the payer, 
        **smoker** column that shows us if there were any smokers in a company, **day** with the day of the week,
        **time** indicating the type of the meal - *Lunch or Dinner*, **size** showing the number of people 
        in the company.''')

    st.subheader('Total bill count')
    st.write('Describes total bill amount distribution')
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.histplot(data=tips, x='total_bill', edgecolor='white')
    st.pyplot(fig)

    st.subheader('total bill & tip dependence'.title())
    st.write('Describes total bill & tips dependence')
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.scatterplot(data=tips, x='total_bill', y='tip', color='#72ccc0')
    st.pyplot(fig)

    st.subheader('total bill, tip & size dependence'.title())
    st.write('Describes total bill, tip, & group size dependence')
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size')
    st.pyplot(fig)

    st.subheader('Weekday & total bill dependence'.title())
    st.write('Shows dependence between the day of the week & total bill')
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.scatterplot(data=tips, x='total_bill', y='day', hue='day', palette='flare')
    st.pyplot(fig)

    st.subheader('Weekday, gender & tip size dependence'.title())
    st.write('Shows dependence between the day of the week, gender & tip size')
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.scatterplot(data=tips, x='total_bill', y='day', hue='sex', palette='husl')
    st.pyplot(fig)


    def day_sort(y):
        days = ['Thur', 'Fri', 'Sat', 'Sun']
        return y.apply(lambda x: days.index(x))

    sorted_tips = tips.sort_values(by='day', key=day_sort, ascending=True)
    st.subheader('Weekday, gender & tip size dependence'.title())
    st.write('The boxplot shows the sum of all bills for each day split by type of the meal (Dinner/Lunch)')
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.boxplot(data=sorted_tips, x='day', y='total_bill', hue='time', palette='magma')
    st.pyplot(fig)

    st.subheader('tip size & meal type'.title())
    st.write('Shows tip size depending on the meal type')
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.histplot(data=tips, x='tip', hue='time', palette='husl', alpha=0.4, edgecolor='white')
    st.pyplot(fig)

    st.subheader('Total bill & tip size dependence for smoking/non-smoking men & women'.title())
    st.write('Shows dependence between the bill size and tip size for men and women & smokers/non-smokers')
    fig = plt.figure(figsize=(7, 3), dpi=500)
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=tips.loc[tips['sex'] == 'Male'], x='total_bill', y='tip', hue='smoker', palette='flare')
    plt.title('Male')
    plt.subplot(1, 2, 2)
    sns.scatterplot(data=tips.loc[tips['sex'] == 'Female'], x='total_bill', y='tip', hue='smoker', palette='flare')
    plt.title('Female')
    st.pyplot(fig)

    st.subheader('What percentage of the bill do women and men leave as tip?'.title())
    tips['Bill %'] = tips['tip'] / tips['total_bill'] * 100
    fig = plt.figure(figsize=(7, 4), dpi=500)
    sns.scatterplot(data=tips, x='tip', y='Bill %', hue='sex', palette='husl')
    st.pyplot(fig)
