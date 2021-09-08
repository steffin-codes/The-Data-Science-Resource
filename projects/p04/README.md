# P04: Real-Time Sentiment Analysis

---

> ## 👀 Quick View 
>
> `Domain :` *Human Resource*
>
> `Algorithm :` *Vader model from NLTK*
>
> > Presenting a simple implementation of the VADER ( Valence Aware Dictionary for Sentiment Reasoning) model form the NLTK package. This web app requires a text input which will then be fed to the model and a corresponding gif is loaded based on the detected emotion. 
>
> `Notebook Link :` [SentimentAnalaysis.ipynb](https://colab.research.google.com/drive/1aF7uNJCu35Hq4-pJ8M7mqd-I70nBdXbG?usp=sharing)
>
> `Source :` [TDS blog](https://towardsdatascience.com/text2emotion-python-package-to-detect-emotions-from-textual-data-b2e7b7ce1153)
>
>  ![ Demo of Real-Time Sentiment Analysis](https://raw.githubusercontent.com/steffincodes/data-scribbles/main/projects/p04/p04_demo.gif)

---

> ## 🔍 Detailed View
> 
> ### **What has been addressed?**
> > To detect the tone of a typed sentence in real-time.
> >
> 
> ### **Why has this been addressed?**
> > By detecting the emotions of the reviews in real-time and automating the response images, we can make better connections between the product user and the product owner (the product being )
> >
> 
> ### **How has this been addressed?**
> > There are 2 main packages to apply sentiment analysis on text data.
> > - VADER (Valence Aware Dictionary for Sentiment Reasoning) from NLTK
> >   - VADER helps in classifying unlabelled text data using polarity and scores
> >   - It Uses a dictionary that maps lexical features to sentiment scores
> > - Text2emotion
> >   - After performing NLP techniques to remove unwanted words, it parses words/phrases and tracks the top 5 emotions (Happy, Angry, Sad, Surprise, and Fear)
> >   - It requrs a dictionary of the emotion and its score for teh inputted text.

---

> ## 📝 Note to Self
>
> ### **Something New**
> > Used API to get a random gif based on the detected emotion from text
> > 
> 
> ### **Work on**
> > Get better gif?
>
> ### **Future Improvement**
> > Use it in a chat bot

---
