import streamlit as st
import datetime # to take in time of when the request was made!
# TODO: use DB to store request
def app():
    st.title('Request')
    requestor_name = st.text_input("What do I call you?",max_chars=10)
    requestor_contact = st.text_input("How do I contact you (IG or Twitter link please)?",max_chars=50)
    request = st.text_area("What do you think I should work on?",height=200)
    if st.button("Request"):
        request_date = datetime.datetime.now()
        st.success("Request added to the queue successfully!")
        st.info("Want immediate response? My IG/twitter @steffincodes is open!")
    SAMPLE_REQUEST = [
        {
            "name": "John Doe",
            "link": "https://twitter.com/johndoe",
            "text": "FUN FACT: Barack Obama and Joe Biden are the only Presidents since 2008 to win BOTH the popular vote AND the Electoral College.",
            "date": "2021/10/01",
            "reaction": {
                "🙅":10,
                "🙅‍♂️":2,
                "🙆":4,
                "🙆‍♀️":3,

            }
        },{
            "name": "Jane Doe",
            "link": "https://twitter.com/janedoe",
            "text": "Immense gratitude to our FY22 budget champions @repblais @SenMikeMoore for their commitment to uplifting the needs of survivors. Your leadership has ensured that survivors across the Commonwealth have access to services from local community-based providers. #mapoli",
            "date": "2021/10/01",
            "reaction": {
                "🙅":10,
                "🙅‍♂️":2,
                "🙆":4,
                "🙆‍♀️":3,

            }
        }
    ]
    for request in SAMPLE_REQUEST:
        st.success("{} has requested for \"{}\" on {}".format(
            request["name"],
            request["text"],
            request["date"]))