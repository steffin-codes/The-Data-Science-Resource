# The Data Scribbles

This is a work in progress please be warned...🖖🏼

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://steffin-datascribbles.streamlit.app/)

## Reproducing this web app locally
To recreate this web app on your own computer, do the following.

### Create Virtual Environment

1. Open the project in VS Code 
2. Use the `ctrl+p` hotkey to open the menu. 
3. Create the Python Virtual Environment using the wizard.
4. Make sure the `requirements.txt` is installed inside the environment
5. Activate the environment

### Create launch file for debugging

1. From the debug menu, create a `launch.json` for python file and select the `Run Python File from Module` option.
2. Add the streamlit entry file in the args. The `launch.json` for this project looks like below
    ```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Module",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "justMyCode": true,
            "args": ["run","🏠_Home.py"]
        }
    ]
}
    ```
###  Launch the app locally

1. Launch from the debug menu [press `F5`] or run it from the terminal using the command `streamlit run 🏠_Home.py`