# Fake News Detection

---

> ## 👀 Quick View 
>
> `Domain :` *Journalism & Mass Communication*
>
> `Algorithm :` *Multinomial Naive Bayes classifier*
>
> > Classify if the provided headline is fake or not. As is with all models, this model is not accurate
>
> `Notebook Link :` [FakeNewsDetection.ipynb](https://colab.research.google.com/drive/1SlU97eciVJys1mHL3Muhi0oCDr0oc0ta?usp=sharing)
>
> `Original :` [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/06/build-your-own-fake-news-classifier-with-nlp/)
>
>  ![Demo of Fake News Detection](https://raw.githubusercontent.com/steffincodes/data-scribbles/main/projects/p08/p08_demo.gif)

---

> ## 🔍 Detailed View
> 
> ### **What has been addressed?**
> > Classification of News headlines into fake or real.
> >
> 
> ### **Why has this been addressed?**
> > Fake news is one of the biggest problems with online social media and even some news sites.
> >
> 
> ### **How has this been addressed?**
> > Copy the headline. Give it as an input to this model. Click the Classify button and let the model do its job for you!
> > The classification is implemented on a labelled set of data using the `MultinomialNB` from `sklearn.naive_bayes`
> > It is a pretty straight forward implementation.
> > - Read the dataset using read_csv from pandas
> > - Split the dataset using `train_test_split` form `sklearn.model_selection`
> > - Train the model `MultinomialNB` on the split dataset
> > - Get the headline from user
> > - Apply the trained model on the inputted text data

---

> ## 📝 Note to Self
>
> ### **Something New**
> > Need to use pickel to save and load model
> 
> ### **Work on**
> > My blogcli is not working
>
> ### **Future Improvement**
> > Give link of the news, auto scrap the headline and detect if fake or real.
> > Maybe find the link of the real news? idk 🤷‍♀️

---