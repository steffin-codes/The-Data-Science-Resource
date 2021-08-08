import streamlit as st
from Helper import IS_LOCAL
def app():
    st.title('Five Questions for selecting a Statistical Method')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    variableCount = st.radio(
      label="How many variables do you have?",
      options=("None","One","More than One","Too Many"),
      key="variableCount"
    )
    if IS_LOCAL: st.markdown('''variableCount : {}'''.format(variableCount))
    if variableCount == 'None':
      pass
    if variableCount == 'One':
      statisticalObjective = st.radio(
        label="What is your statistical objective?",
        options=("None","Describe","Classify","Compare","Predict","Explain"),
        key="statisticalObjective_oneVariable"
      )
      if IS_LOCAL: st.markdown('''statisticalObjective : {}'''.format(statisticalObjective))
      if statisticalObjective == 'None':
        pass
      if statisticalObjective == "Describe":
        st.markdown(
          '''
          ## Descriptive Statistics:
          ### Discrete Scales:
              Counts, proportions
          ### Continuous Scales:
              Means, standard deviations, medians, ranges, quartiles
          ## Distribution Fitting:
          ### Statistics:
              Skewness, kurtosis coefficient of variation
          ### Graphics:
              Histograms, box plots, probability plots
          ### Tests:
              Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk Lillifors
          '''
        )
      if statisticalObjective == "Classify":
        st.markdown(
          '''
          - Filtering
          - Sorting
          - Cluster analysis
          '''
        )
      if statisticalObjective == "Compare":
        st.markdown(
          '''
          ## One-Population Test:
          ### Discrete Scale:
              Non-parametric statistics
          ### Continuous Scales:
              t-tests, control charts
          '''
        )
      if statisticalObjective == "Predict":
        st.warning("Not possible")
      if statisticalObjective == "Explain":
        st.warning("Not possible")
    if variableCount == 'More than One':
      variableDependency = st.radio(
        label="Are some variables dependent and others independent?",
        options=("None","Yes","No"),
        key="variableDependency"
      )
      if IS_LOCAL: st.markdown('''variableDependency : {}'''.format(variableDependency))
      if variableDependency == 'None':
        pass
      if variableDependency == 'Yes':
        variableCorrelated = st.radio(
          label="Are the dependent variables autocorrelated?",
          options=("None","Yes","No"),
          key="variableCorrelated"
        )
        if IS_LOCAL: st.markdown('''variableCorrelated : {}'''.format(variableCorrelated))
        if variableCorrelated == 'None':
          pass
        if variableCorrelated == 'Yes':
          typeOfDependency = st.radio(
            label="Is it time or location dependent?",
            options=("None","Location Dependent","Time Dependent"),
            key="typeOfDependency"
          )
          if IS_LOCAL: st.markdown('''typeOfDependency : {}'''.format(typeOfDependency))
          if typeOfDependency == 'None':
            pass
          if typeOfDependency == 'Location Dependent':
            statisticalObjective = st.radio(
                label="What is your statistical objective?",
                options=("None","Describe","Classify","Compare","Predict","Explain"),
                key="statisticalObjective_location"
            )
            if IS_LOCAL: st.markdown('''statisticalObjective : {}'''.format(statisticalObjective))
            if statisticalObjective == "None":
                pass
            if statisticalObjective == "Describe":
                st.info("With location dependent variable as grouping factor")
                st.markdown('''
                ## Descriptive Statistics:
                ### Discrete Scales:
                    Counts, proportions
                ### Continuous Scales:
                    Means, standard deviations, medians, ranges, quartiles
                ## Distribution Fitting:
                ### Statistics:
                    Skewness, kurtosis coefficient of variation
                ### Graphics:
                    Histograms, box plots, probability plots
                ### Tests:
                    Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk Lillifors
                Cross-tabulations
                ## Correlations:
                ### Discrete Scales:
                    Spearman Rho, Kendall Tau, gamma
                ### Continuous Scales:
                    Pearson Product,Moment Correlation
                ''')
                pass
            if statisticalObjective == "Classify":
                st.info("With location dependent variable as grouping factor")
                st.markdown('''
                - Cluster Analysis
                - Discriminant Anlaysis
                ''')
                pass
            if statisticalObjective == "Compare":
                st.info("With location dependent variable as grouping factor")
                st.markdown('''
                ## One-Population Test:
                ### Discrete Scale:
                    Non-parametric statistics
                ### Continuous Scales:
                    t-tests, control charts
                ## Multi-Population Test:
                    ANOVA, ANCOVA, Non Parameteric Test
                ''')
                pass
            if statisticalObjective == "Predict":
                st.markdown('''
                - Smoothing interpolation
                - trend-surfaces
                - geostatistics (variogramming and kring)
                ''')
                pass
            if statisticalObjective == "Explain":
                st.markdown('''
                - geostatistics (variogramming and kring)
                ''')
                pass
            pass
          if typeOfDependency == 'Time Dependent':
            statisticalObjective = st.radio(
                label="What is your statistical objective?",
                options=("None","Describe","Classify","Compare","Predict","Explain"),
                key="statisticalObjective_time"
            )
            if IS_LOCAL: st.markdown('''statisticalObjective : {}'''.format(statisticalObjective))
            if statisticalObjective == "None":
                pass
            if statisticalObjective == "Describe":
                st.info("With time dependent variable as grouping factor")
                st.markdown('''
                ## Descriptive Statistics:
                ### Discrete Scales:
                    Counts, proportions
                ### Continuous Scales:
                    Means, standard deviations, medians, ranges, quartiles
                ## Distribution Fitting:
                ### Statistics:
                    Skewness, kurtosis coefficient of variation
                ### Graphics:
                    Histograms, box plots, probability plots
                ### Tests:
                    Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk Lillifors
                Cross-tabulations
                ## Correlations:
                ### Discrete Scales:
                    Spearman Rho, Kendall Tau, gamma
                ### Continuous Scales:
                    Pearson Product,Moment Correlation
                ''')
                pass
            if statisticalObjective == "Classify":
                st.info("With time dependent variable as grouping factor")
                st.markdown('''
                - Cluster Analysis
                - Discriminant Anlaysis
                ''')
                pass
            if statisticalObjective == "Compare":
                st.info("With time dependent variable as grouping factor")
                st.markdown('''
                ## One-Population Test:
                ### Discrete Scale:
                    Non-parametric statistics
                ### Continuous Scales:
                    t-tests, control charts
                ## Multi-Population Test:
                    ANOVA, ANCOVA, Non Parameteric Test
                ''')
                pass
            if statisticalObjective == "Predict":
                st.markdown('''
                - Smoothing interpolation
                - time-series regression
                - ARIMA 
                - spectral analysis 
                - neural networks
                ''')
                pass
            if statisticalObjective == "Explain":
                st.markdown('''
                - time-series regression
                - ARIMA 
                - spectral analysis 
                ''')
                pass
            pass
          pass
        if variableCorrelated == 'No':
          statisticalObjective = st.radio(
              label="What is your statistical objective?",
              options=("None","Describe","Classify","Compare","Predict","Explain"),
              key="statisticalObjective_notCorrelated"
          )
          if IS_LOCAL: st.markdown('''statisticalObjective : {}'''.format(statisticalObjective))
          if statisticalObjective == "None":
              pass
          if statisticalObjective == "Describe":
              st.markdown(
                '''
                ## Descriptive Statistics:
                ### Discrete Scales:
                    Counts, proportions
                ### Continuous Scales:
                    Means, standard deviations, medians, ranges, quartiles
                ## Distribution Fitting:
                ### Statistics:
                    Skewness, kurtosis coefficient of variation
                ### Graphics:
                    Histograms, box plots, probability plots
                ### Tests:
                    Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk Lillifors
                Cross-tabulations
                ## Correlations:
                ### Discrete Scales:
                    Spearman Rho, Kendall Tau, gamma
                ### Continuous Scales:
                    Pearson Product,Moment Correlation
                '''
              )
              pass
          if statisticalObjective == "Classify":
              st.markdown('''
              - Cluster Analysis
              - Discriminant Anlaysis
              ''')
              pass
          if statisticalObjective == "Compare":
              st.markdown('''
              ## One-Population Test:
              ### Discrete Scale:
                  Non-parametric statistics
              ### Continuous Scales:
                  t-tests, control charts
              ## Multi-Population Test:
                  ANOVA, ANCOVA, Non Parameteric Test
              ''')
              pass
          if statisticalObjective == "Predict":
              st.markdown('''
              ## Discrete scale dependent variable:
                  Logistic regression, classification trees, discriminant analysis
              ## Continuous scale dependent variables:
                  Regression
              ''')
              pass
          if statisticalObjective == "Explain":
              st.markdown('''
              ## Discrete scale dependent variable:
                  Logistic regression, classification trees, discriminant analysis
              ## Continuous scale dependent variables:
                  Regression, Canonical Correlation
              ''')
              pass
          pass
        pass
      if variableDependency == 'No':
        statisticalObjective = st.radio(
            label="What is your statistical objective?",
            options=("None","Describe","Classify","Compare","Predict","Explain"),
            key="statisticalObjective_independent"
        )
        if IS_LOCAL: st.markdown('''statisticalObjective : {}'''.format(statisticalObjective))
        if statisticalObjective == "None":
            pass
        if statisticalObjective == "Describe":
          st.markdown(
            '''
            ## Descriptive Statistics:
            ### Discrete Scales:
                Counts, proportions
            ### Continuous Scales:
                Means, standard deviations, medians, ranges, quartiles
            ## Distribution Fitting:
            ### Statistics:
                Skewness, kurtosis coefficient of variation
            ### Graphics:
                Histograms, box plots, probability plots
            ### Tests:
                Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk Lillifors
            ## Correlations:
            ### Discrete Scales:
                Spearman Rho, Kendall Tau, gamma
            ### Continuous Scales:
                Pearson Product, Moment Correlation
            '''
          )
        if statisticalObjective == "Classify":
          st.markdown(
            '''
            - Filtering
            - Sorting
            - Cluster analysis
            '''
          )
        if statisticalObjective == "Compare":
          st.markdown(
            '''
            ## One-Population Test:
            ### Discrete Scale:
                Non-parametric statistics
            ### Continuous Scales:
                t-tests, control charts
            '''
          )
        if statisticalObjective == "Predict":
            st.warning("Not possible")
            pass
        if statisticalObjective == "Explain":
            st.markdown('''
            - Cluster analysis
            - multi dimensional scaling 
            - principal components analysis
            - correspondence analysis
            ''')
            pass
        pass
      pass
    if variableCount == 'Too Many':
      st.markdown(
        '''
        Conduct a cluster analysis to select representative variables
        Conduct a principal components analysis, factor analysis, correspondence analysis, or multidimensional scaling to reduce the number of variables needed to represent most of the variability
        '''
      )
      pass
