# The Data Scribbles

This is a work in progress please be warned...🖖🏼

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/steffincodes/data-scribbles/main/app.py)

## Reproducing this web app locally
To recreate this web app on your own computer, do the following.

### Create conda environment
1. Firstly, we will create a conda environment called *streamlit*
    ```
    conda create -n streamlit python=3.7.9
    ```
2. Secondly, we will login to the *streamlit* environement
    ```
    conda activate streamlit
    ```
### Install prerequisite libraries

1. Download requirements.txt file
    ```
    wget https://raw.githubusercontent.com/steffincodes/data-scribbles/main/requirements.txt
    ```

2. Pip install libraries
    ```
    pip install -r requirements.txt
    ```

###  Launch the app locally

```
streamlit run app.py
```