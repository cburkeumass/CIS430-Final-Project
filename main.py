import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

#import the dataset
data = pd.read_csv("/Users/Cameron/PycharmProjects/MLBDataProject/MLBData - Sheet1.csv")
data.head()

#plot the initial graph of the data
X = data[["Run Dif", "Inc Calls"]]
plt.scatter(X["Run Dif"], X["Inc Calls"], c="blue")
plt.xlabel("Run Differential")
plt.ylabel("Incorrect Calls")
plt.show()

#claim 3 clusters
K=3

#plot the initial cluster points
Centroids = (X.sample(n=K))
plt.scatter(X["Run Dif"], X["Inc Calls"], c="blue")
plt.scatter(Centroids["Run Dif"], Centroids["Inc Calls"], c="red")
plt.xlabel("Run Differential")
plt.ylabel("Incorrect Calls")
plt.show()

#Set differece to 1 and j to 0
diff = 1
j = 0

#Assign points to centroid, recompute the centroid, and repeat until the clusters are complete
while (diff != 0):
    XD = X
    i = 1
    for index1, row_c in Centroids.iterrows():
        ED = []
        for index2, row_d in XD.iterrows():
            d1 = (row_c["Run Dif"] - row_d["Run Dif"]) ** 2
            d2 = (row_c["Inc Calls"] - row_d["Inc Calls"]) ** 2
            d = sqrt(d1 + d2)
            ED.append(d)
        X[i] = ED
        i = i + 1
    C = []
    for index, row in X.iterrows():
        min_dist = row[1]
        pos = 1
        for i in range(K):
            if row[i + 1] < min_dist:
                min_dist = row[i + 1]
                pos = i + 1
        C.append(pos)
    X["Cluster"] = C
    #Calculates the mean of the centroids
    Centroids_new = X.groupby(["Cluster"]).mean()[["Inc Calls", "Run Dif"]]
    #If the difference between the new and old centroids are 0, the the program ends
    if j == 0:
        diff = 1
        j = j + 1
    else:
        #Finds the difference between the New centroid and the old centroid
        diff = (Centroids_new['Inc Calls'] - Centroids['Inc Calls']).sum() + (
                    Centroids_new['Run Dif'] - Centroids['Run Dif']).sum()
        #Print the difference between the new and old centroid
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Inc Calls", "Run Dif"]]

    #Plot the points in different colors to diffentiate between clusters
    color = ['blue', 'green', 'purple']
    for k in range(K):
        data = X[X["Cluster"] == k + 1]
        plt.scatter(data["Run Dif"], data["Inc Calls"], c=color[k])
    plt.scatter(Centroids["Run Dif"], Centroids["Inc Calls"], c='red')
    plt.xlabel('Run Differential')
    plt.ylabel('Incorrect Calls')
    plt.show()
    #Plots every graph for ever computation of centroids, once the difference between the new and old centroids is 0 then the final graph will show