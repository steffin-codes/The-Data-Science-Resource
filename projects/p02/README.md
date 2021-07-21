# Cartoonifying Image using K-Means

---

> ## 👀 Quick View 
>
> `Domain :` *Arts & Design*
>
> `Algorithm :` *K-means Algorithm from OpenCV*
>
> > Presenting a simple implementation of the K-means clustering algorithm provided by `OpenCV`. 
>
> `Notebook Link :` [ImageCartoonifyer.ipynb](https://colab.research.google.com/drive/15osRtroUiBjkDyZxuAtKTaXtdc24cjg2?usp=sharing)
>
> `Original :` [Datahacker Blog](http://datahacker.rs/002-opencv-projects-how-to-cartoonize-an-image-with-opencv-in-python/)
>
<!-- >  ![Demo of Cartoonifying Image using K-Means](https://raw.githubusercontent.com/steffincodes/data-scribbles/main/projects/p02/p02_demo.gif) -->

---

> ## 🔍 Detailed View
> 
> ### **What has been addressed?**
> >
> > A customized image filter, to give a comic effect to your photos.
> 
> ### **Why has this been addressed?**
> > 
> > Ever wanted to apply a customized comic filter to your photos? I am a thick outline person, and this was addressed in this tool.
> 
> ### **How has this been addressed?**
> >
> > This web app requires an image, from which the edges are seperated by bluring using the `medianBlur` function on the black/white version of the original image and then applying the `adaptiveThreshold`. This `edge_mask` is then added to the `Quantized` image. The Image is `Quantized` by using the `cv2.kmeans` algorithm, which helps control the number of colors present in the image.

---

> ## 📝 Note to Self
>
> ### **Something New**
> > `OpenCV` also has K-Means Algorithm!
> 
> ### **Work on**
> > Better way to explaing the `How has this been addressed?` par of the writeup.
>
> ### **Future Improvement**
> > Do a comparision between `OpenCV`'s and `Scikit-learn`'s `K-means` algorithm

---