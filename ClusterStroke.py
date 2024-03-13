import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample stroke data (replace with your actual data)
strokes = [
    [(10, 20), (15, 25), (20, 30), (25, 28), (30, 25)],  # Character A
    [(35, 40), (40, 35), (45, 40), (40, 45), (35, 40)],  # Character O
    # ... add more strokes for other characters
]

# Extract features (replace with your chosen features)
features = []
for stroke in strokes:
  # Calculate features (e.g., bounding box, aspect ratio, curvature)
  # ... (implementation details omitted for brevity)
  features.append(extracted_features)

# K-Means clustering (adjust parameters as needed)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(features)

# Visualize strokes and clusters
colors = ['red', 'green', 'blue']  # Adjust colors for more clusters
for i, stroke in enumerate(strokes):
  x, y = zip(*stroke)
  plt.plot(x, y, marker='o', color=colors[kmeans.labels_[i]])

plt.title("Strokes and Clusters")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.show()