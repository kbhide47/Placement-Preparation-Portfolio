# ==========================================================
# DAY 14 - UNSUPERVISED LEARNING
#
# Topics:
# 1. K-Means Clustering
# 2. Elbow Method
# 3. Silhouette Score
# 4. Hierarchical Clustering
# 5. PCA
# 6. Dimensionality Reduction
# 7. Visualization
# ==========================================================


import pandas as pd
import matplotlib.pyplot as plt


from sklearn.datasets import load_iris

from sklearn.preprocessing import StandardScaler

from sklearn.cluster import (
    KMeans,
    AgglomerativeClustering
)

from sklearn.metrics import silhouette_score

from sklearn.decomposition import PCA


# ----------------------------------------------------------

print("="*60)
print("Question 1 : Load Dataset")
print("="*60)


iris = load_iris()


X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)


print(X.head())



# ----------------------------------------------------------

print("\nQuestion 2 : Dataset Shape")

print(X.shape)



# ----------------------------------------------------------

print("\nQuestion 3 : Feature Scaling")


scaler = StandardScaler()


X_scaled = scaler.fit_transform(X)


print(X_scaled[:5])



# ----------------------------------------------------------

print("\nQuestion 4 : Elbow Method")


inertia = []


for k in range(1,11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    inertia.append(
        kmeans.inertia_
    )


print(inertia)



# Visualization

plt.figure(figsize=(8,5))

plt.plot(
    range(1,11),
    inertia,
    marker="o"
)

plt.title("Elbow Method")

plt.xlabel("Number of Clusters")

plt.ylabel("Inertia")

plt.show()



# ----------------------------------------------------------

print("\nQuestion 5 : K-Means Clustering")


kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)


clusters = kmeans.fit_predict(
    X_scaled
)


X["Cluster"] = clusters


print(X.head())



# ----------------------------------------------------------

print("\nQuestion 6 : Silhouette Score")


score = silhouette_score(
    X_scaled,
    clusters
)


print(
    "Silhouette Score:",
    score
)



# ----------------------------------------------------------

print("\nQuestion 7 : Cluster Centers")


print(
    kmeans.cluster_centers_
)



# ----------------------------------------------------------

print("\nQuestion 8 : Hierarchical Clustering")


hierarchical = AgglomerativeClustering(
    n_clusters=3
)


hierarchical_labels = hierarchical.fit_predict(
    X_scaled
)


print(
    hierarchical_labels[:10]
)



# ----------------------------------------------------------

print("\nQuestion 9 : PCA Dimensionality Reduction")


pca = PCA(
    n_components=2
)


X_pca = pca.fit_transform(
    X_scaled
)


print(
    X_pca[:5]
)



# ----------------------------------------------------------

print("\nQuestion 10 : PCA Explained Variance")


print(
    pca.explained_variance_ratio_
)



# ----------------------------------------------------------

print("\nQuestion 11 : PCA Visualization")


plt.figure(figsize=(8,5))


plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=clusters
)


plt.title(
    "PCA Cluster Visualization"
)


plt.xlabel(
    "Principal Component 1"
)


plt.ylabel(
    "Principal Component 2"
)


plt.show()



# ----------------------------------------------------------

print("\nQuestion 12 : Cluster Count")


print(
    X["Cluster"].value_counts()
)



# ----------------------------------------------------------

print("\nQuestion 13 : Original Features")


print(
    iris.feature_names
)



# ----------------------------------------------------------

print("\nQuestion 14 : Compare Clusters")


print(
    X.groupby("Cluster").mean()
)



# ----------------------------------------------------------

print("\nQuestion 15 : Final Summary")


print(
    "Total Data Points:",
    len(X)
)


print(
    "Number of Clusters:",
    len(X["Cluster"].unique())
)



print("\nDay 14 Completed Successfully!")
