import streamlit as st
def app():
    st.title('Five Questions for selecting a Statistical Method')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
    variableCount = st.radio(
      label="How many variables do you have?",
      options=("None","One","More than One","Too Many")
    )
    if variableCount == 'None':
      st.markdown(
        '''
        variableCount : {}
        '''
      .format(variableCount))
    if variableCount == 'One':
      st.markdown(
        '''
        variableCount : {}
        '''
      .format(variableCount))
      statisticalObjective = st.radio(
        label="What is your statistical objective?",
        options=("None","Describe","Classify","Compare","Predict","Explain")
      )
      if statisticalObjective == 'None':
        st.markdown(
          '''
          variableCount : {}
          
          statisticalObjective : {}
          '''
        .format(variableCount,statisticalObjective))
      if statisticalObjective == "Describe":
        st.markdown(
          '''
          variableCount : {}
          
          statisticalObjective : {}

          ## Descriptive Statistics:
          ### Discrete Scales
              
              Counts, proportions

          ### Continuous Scales
              
              Means, standard deviations, medians, ranges, quartiles

          ## Distribution Fitting Statistics:
              
              Skewness, kurtosis coefficient of variation

          ## Graphics:
              
              Histograms, box plots, probability plots

          ## Tests:
              
              Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk Lillifors



          '''
        .format(variableCount,statisticalObjective))
      if statisticalObjective == "Classify":
        st.markdown(
          '''
          variableCount : {}
          
          statisticalObjective : {}
          - Filtering
          - Sorting
          - Cluster analysis
          '''
        .format(variableCount,statisticalObjective))
      if statisticalObjective == "Compare":
        st.markdown(
          '''
          variableCount : {}
          
          statisticalObjective : {}
          ## Discrete Scale
              One-Population Test
              Non-parametric statistics
          ## Continuous Scales
              t-tests
              control charts

          '''
        .format(variableCount,statisticalObjective))
      if statisticalObjective == "Predict":
        st.markdown(
          '''
          variableCount : {}
          
          statisticalObjective : {}
          '''
        .format(variableCount,statisticalObjective))
        st.warning("Not possible")
      if statisticalObjective == "Explain":
        st.markdown(
          '''
          variableCount : {}
          
          statisticalObjective : {}
          '''
        .format(variableCount,statisticalObjective))
        st.warning("Not possible")
    if variableCount == 'More than One':
      st.markdown(
        '''
        variableCount : {}
        '''
      .format(variableCount))
    if variableCount == 'Too Many':
      st.markdown(
        '''
        variableCount : {}
        
        Conduct a cluster analysis to select representative variables
        
        Conduct a principal components analysis, factor analysis, correspondence analysis, or multidimensional scaling to reduce the number of variables needed to represent most of the variability

        '''
      .format(variableCount))

    
