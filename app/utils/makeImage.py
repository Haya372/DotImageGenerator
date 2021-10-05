import cv2
from sklearn.cluster import KMeans
import numpy as np

#img = cv2.imread('images/IMG_7298.PNG')

# 色をr種類にクラスタリングする
def roundColor(dst, r = 10):
  h, w = dst.shape[:2]
  data = dst.reshape(h * w, 3)

  # k-means法による学習
  kmeans_model = KMeans(n_clusters=r, random_state=10).fit(data)
  labels = kmeans_model.labels_

  # ラベルに基づいてr色に分ける
  colors = np.zeros((r, 3))
  cnt = np.zeros(r)
  for i in range(len(data)):
    c = labels[i]
    cnt[c] += 1
    colors[c] += data[i]
  # 平均をとる
  for c in range(r):
    colors[c] //= cnt[c]
  for i in range(len(data)):
    c = labels[i]
    data[i] = colors[c]
  data = data.reshape((h, w, 3))
  return data

def makeDotImg(img, height = 100, width = 100, r = 10):
  dst = cv2.resize(img, dsize=(width, height))
  dst = roundColor(dst, r)
  return cv2.resize(dst, dsize=(500, 500))

#cv2.imshow('before', cv2.resize(img, dsize=(500, 500)))
#cv2.imshow('after', makeDotImg(img))
#cv2.waitKey(0)
#cv2.destroyAllWindows()
