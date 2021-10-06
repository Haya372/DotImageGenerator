import cv2
from sklearn.cluster import KMeans
import numpy as np

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

OUTPUT_DIR = 'outputs'
def makeDotImg(filepath, r = 0.2, c = 10):
  img = cv2.imread(filepath)
  w, h = img.shape[:2]
  dst = cv2.resize(img, dsize=(int(w * r), int(h * r)))
  dst = roundColor(dst, c)
  output = cv2.resize(dst, dsize=(int(w), int(h)))
  return output


# img = cv2.imread('/Users/mitomihayato/dot-image/uploads/cat_img_1633269692472.png')
# cv2.imshow('before', img)
# cv2.imshow('after', makeDotImg(img))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
