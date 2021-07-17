# Cartoonifying Image using K-Means

Presenting a simple implementation of the K-means clustering algorithm. This web app requires an image, from which the edges are seperated by bluring using `medianBlur` over the black/white version and applying the `adaptiveThreshold`. This `edge_mask` is then added to the `Quantized` image.Image is `Quantized` by using the `cv2.kmeans` algorithm.

More to this later :)