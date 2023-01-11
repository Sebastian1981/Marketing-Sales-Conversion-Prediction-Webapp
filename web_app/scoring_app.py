import streamlit as st
import numpy as np
import pandas as pd


from utils import prepare_data, predict_conversion, convert_df, plot_cluster_distribution, plot_numeric_features, plot_categorical_features, pie_plot_cluster_distribution


def run_scoring_app():

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        ############################################
        # Read Raw CSV File
        ############################################
        df = pd.read_csv(uploaded_file, sep=';')

        # drop a few columns which are typically not available in many scenarios or columns which leads to leakage b/c it cannot be known beforehand!
        df.drop(labels=['y', 'duration', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx','euribor3m', 'nr.employed'], axis=1, inplace=True)
        # make feature denoting if there was a previous contact
        df['previous_contact'] = (df['pdays'] != 999).apply(lambda x: 'no' if x==False else 'yes')
        # insert random value if value equal 999 since the values is not defined
        df['pdays'] = df['pdays'].apply(lambda x: np.nan if x==999 else x)

        ############################################
        # Prepare Dataset
        ############################################

        # get numeric and categorical columns
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        numeric_columns = df.select_dtypes(include=numerics).columns.to_list()
        categorical_columns = df.select_dtypes(exclude=numerics).columns.to_list()

        df = prepare_data(df, numeric_columns, categorical_columns)

        ############################################
        # Predict Conversion
        ############################################

        df = predict_conversion(df, numeric_columns, categorical_columns)
        
        st.write(df)

        # download labeled dataset
        st.download_button(
            label="Download Data as CSV",
            data=convert_df(df),
            file_name='df_clustered.csv',
            mime='text/csv',
        )


        ############################################
        # Visualize Cluster
        ############################################
        
        # visualize cluster distribution
        st.subheader('Converter Distribution')
        pie_plot_cluster_distribution(df)
        plot_cluster_distribution(df)

        ## visualize numeric features for each cluster
        #st.subheader('Plot Univariate Distributions')
        #plot_numeric_features(df, numeric_columns)

        ## visualize categorical features for each cluster
        #plot_categorical_features(df, categorical_columns)

        
         
        
        