# Explore images in cluster 1
# cluster1 variable holds the data that has been grouped into the first cluster
cluster1 = mnist_data[model.labels_==0]
# Pick 5 random images from cluster 1
cluster1_imgs = cluster1.iloc[[np.random.randint(0,cluster1.shape[0]) for i in range(0,5)]]
# Plot the images in cluster 1
for i in range(0,cluster1_imgs.shape[0]):
    plt.subplot(1,5,i+1)
    img_fig = np.asarray(cluster1_imgs[i:i+1]).reshape(28,28)
    plt.imshow(img_fig,cmap=plt.cm.gray)
#################################################
    # Explore images in cluster 2
cluster2 = mnist_data[model.labels_==1]
cluster2_imgs = cluster2.iloc[[np.random.randint(0,cluster2.shape[0]) for i in range(0,5)]]
for i in range(0,cluster2_imgs.shape[0]):
    plt.subplot(1,5,i+1)
    img_fig = np.asarray(cluster2_imgs[i:i+1]).reshape(28,28)
    plt.imshow(img_fig,cmap=plt.cm.gray)
