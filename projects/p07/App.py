import streamlit as st
import pandas as pd
import numpy as np
import re
# from random import shuffle
#TODO: Whatsapp Chat Analyzer
def app():
    #? Project Inputs
    st.title("P07: Whatsapp Chat Analyzer")
    st.sidebar.subheader("Project Inputs:")
    uploaded_file = st.sidebar.file_uploader("Upload a file",type=['txt'])
    privacy = st.sidebar.checkbox("Privacy")
    Analyse = False
    if uploaded_file: Analyse = st.sidebar.button("Analyse") 
    def startsWithDate(s):
        # 07/01/21, 4:35 pm
        pattern = '^[0-1][0-9]\/[0-1][0-9]\/[0-9][0-9], [0-1]?[0-9]:[0-5][0-9] a?p?m? -'
        result = re.match(pattern, s)
        if result:
            return True
        return False
    def startsWithAuthor(s):
        patterns = [
            '([\w]+):',                        # First Name
            '([\w]+[\s]+[\w]+):',              # First Name + Last Name
            '([\w]+[\s]+[\w]+[\s]+[\w]+):',    # First Name + Middle Name + Last Name
            '([+]\d{2} \d{5} \d{5}):',         # Mobile Number (India)
            '([+]\d{2} \d{3} \d{3} \d{4}):',   # Mobile Number (US)
            '([+]\d{2} \d{4} \d{7})',          # Mobile Number (Europe)
            '([+]\d{2} \d{2}-\d{4} \d{4})',    # +nn nn-nnnn nnnn
            '([+]\d{1} \(\d{3}\) \d{3}-\d{4})',# +n (nnn) nnn-nnnn
        ]
        pattern = '^' + '|'.join(patterns)
        result = re.match(pattern, s)
        if result:
            return True
        return False
    def getDataPoint(line):
        splitLine = line.split(' - ')
        dateTime = splitLine[0] 
        date, time = dateTime.split(', ') 
        message = ' '.join(splitLine[1:]) 
        if startsWithAuthor(message): 
            splitMessage = message.split(': ') 
            author = splitMessage[0] 
            message = ' '.join(splitMessage[1:]) 
        else:
            author = None
        return date, time, author, message
    if Analyse:
        parsedData = [] 
        messageBuffer = []
        date, time, author = None, None, None
        for line in uploaded_file:
            line = str(line,"utf-8")
            if not line: break
            line = line.strip()
            if startsWithDate(line): 
                if len(messageBuffer) > 0: 
                    parsedData.append([date, time, author, ' '.join(messageBuffer)]) 
                messageBuffer.clear() 
                date, time, author, message = getDataPoint(line) 
                messageBuffer.append(message) 
            else:
                messageBuffer.append(line) 
                pass
            pass
        df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message'])
        author_list = list(df.Author.unique())
        df.replace({author_list[0]:"WhatsApp"}, inplace=True)
        author_list[0] = "WhatsApp"
        if privacy:
            def generate_alias(name):
                # returning initials
                name = [ s[0] for s in name.split() ]
                return ''.join(name)
            aliases = [str(index)+"-"+generate_alias(str(author)) for index,author in enumerate(author_list)]
            df['Author'].replace(author_list, aliases, inplace=True)
        df["Date"] = pd.to_datetime(df["Date"])
        weeks = {
            0 : 'Monday',
            1 : 'Tuesday',
            2 : 'Wednesday',
            3 : 'Thrusday',
            4 : 'Friday',
            5 : 'Saturday',
            6 : 'Sunday'
        }
        df['Day'] = df['Date'].dt.weekday.map(weeks)
        df = df[['Date','Day','Time','Author','Message']]
        df['Letters'] = df['Message'].apply(lambda s : len(s))
        df['Words'] = df['Message'].apply(lambda s : len(s.split(' ')))
        URLPATTERN = r'(https?://S+)'
        df['Url_Count'] = df.Message.apply(lambda x: re.findall(URLPATTERN, x)).str.len()
        links = np.sum(df.Url_Count)
        total_messages = df.shape[0]
        media_messages = df[df['Message'] == '<Media omitted>'].shape[0]
        links = np.sum(df.Url_Count)
        def display_group_stats():
            st.markdown('''
            ## Group Chatting Stats : 
                Total Number of Messages : {}
                Total Number of Media Messages : {}
                Total Number of Links : {}
            '''.format(
                total_messages,
                media_messages,
                links
            ))
            pass
        def display_group_member_stats():
            author_list = df.Author.unique()
            for i in range(len(author_list)):
                req_df = df[df["Author"] == author_list[i]]
                words_per_message = (np.sum(req_df['Words']))/req_df.shape[0]
                w_p_m = ("%.3f" % round(words_per_message, 2))  
                media = sum(req_df["Media_Count"])
                links = sum(req_df["Url_Count"])   
                st.markdown('''
                ## Stats of {}
                    Total Messeges Typed: {}
                    Average Words per Message : {}
                    Total Media Message Sent : {}
                    Total Links Sent : {}
                '''.format(
                    author_list[i],
                    req_df.shape[0],
                    w_p_m,
                    media,
                    links,
                ))
            pass
        col1, col2 = st.columns([1, 3])
        with col1:
            display_group_stats()
            display_group_member_stats()
        with col2:
            def display_timeline_chart():
                df['Year'] = df['Date'].dt.year
                df['Mon'] = df['Date'].dt.month
                months = {
                    1 : 'Jan',
                    2 : 'Feb',
                    3 : 'Mar',
                    4 : 'Apr',
                    5 : 'May',
                    6 : 'Jun',
                    7 : 'Jul',
                    8 : 'Aug',
                    9 : 'Sep',
                    10 : 'Oct',
                    11 : 'Nov',
                    12 : 'Dec'
                }
                df['Month'] = df['Mon'].map(months)
                df.drop('Mon',axis=1,inplace=True)
                st.subheader("Time line...")
                df['Month_Year'] = df['Month'].astype(str) + " " + df["Year"].astype(str)
                active_month = df['Month_Year'].value_counts()
                st.line_chart(active_month)
            display_timeline_chart()
            st.subheader("Most Active member of the group:")
            most_active_member = df['Author'].value_counts()
            st.bar_chart(most_active_member)
            st.subheader("Most Active day:")
            most_active_day = df['Day'].value_counts()
            st.bar_chart(most_active_day)
            st.subheader("The most active time of the group:")
            active_time = df['Time'].value_counts().sort_index()
            st.line_chart(active_time)
            st.subheader("Who types the most:")
            max_words = df[['Author','Words']].groupby('Author').sum()
            m_w = max_words.sort_values('Words',ascending=False)
            st.bar_chart(m_w)
            if df[df['Message'] == '<Media omitted>'].shape[0] > 0:
                st.subheader("Highest Media Sharer:")
                media_omitted = df[df['Message'] == '<Media omitted>']
                media_sharer = media_omitted['Author'].value_counts()
                st.bar_chart(media_sharer)
            if np.sum(df.Url_Count) > 0:
                st.subheader("Who shared the most links:")
                max_words = df[['Author','Url_Count']].groupby('Author').sum()
                m_w = max_words.sort_values('Url_Count',ascending=False)
                st.bar_chart(m_w)
    else: 
        st.warning("👈🏼 Head over to the sidebar and upload an your Whatsapp Chat to be analysed!")
    pass