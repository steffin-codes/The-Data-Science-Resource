# P03: Handwritten Digit Recognition

---

> ## 👀 Quick View 
>
> `Domain :` *Finance*
>
> `Algorithm :` *Convolutional Neural Networks from Tensorflow-Keras*
>
> > A simple Handwritten Digit Recognition using CNN on the MINST dataset that accepts data from canvas
>
> `Notebook Link :` [HandwrittenNumberRecognition.ipynb](https://colab.research.google.com/drive/1VkM7x3Qf_NGQt9t10tprv1662duWPPrM?usp=sharing)
>
> `Original :` [Analytics Vidhya](https://medium.com/analytics-vidhya/deep-learning-project-handwritten-digit-recognition-using-python-26da7ed11d1c)
>
>  ![Demo of Handwritten Digit Recognition](https://raw.githubusercontent.com/steffincodes/data-scribbles/main/projects/p03/p03_demo.gif)

---

> ## 🔍 Detailed View
> 
> ### **What has been addressed?**
> > To recogonize hand written digits and digitalize them.
> >
> 
> ### **Why has this been addressed?**
> > To serve as the base for implementing OCR of handwritten documents using tensorflowand keras
> >
> 
> ### **How has this been addressed?**
> > ~~Using the ... I am a few courses too early to comment on this. I am going with a "so it works let's not touch it" mindset 🤷🏼‍♀️~~
> > The algorithm is split into 2 parts
> > - Model Building
> >   - Load and split the `MINST` dataset
> >   - Create a `sequential` model with 3 layers using .add() of 300,50 and 10 neurons
> >   - Compile the configured model using `sparse_categorical_crossentropy` & `Adam` optimizer
> >   - Train and save the model
> > - Model Deployment
> >   - Load the saved model
> >   - Enable inputtable canvas for the model to get processed data
> >   - Since the MINST dataset is white digit on back background, the user input is prepared to be like so
> >   - Also it is to be noted that the size 28*28 is used when model building, the same is used while preparing the user input
> >   - This image is captured and fed into the loaded model
> >   - The predicted values are charted out
> > 

---

> ## 📝 Note to Self
>
> ### **Something New**
> > Deployed Tensor model!
> 
> ### **Work on**
> > Use one-hot encoding and increase the accuracy
> > Learn to debug, please !!
>
> ### **Future Improvement**
> > Detect multiple digits

---