import os
import cv2
import face_recognition
from sklearn.cluster import DBSCAN
import numpy as np

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def detect_and_encode_faces(images):
    encodings = []
    for img in images:
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Detect faces using face_recognition (which uses dlib under the hood)
        face_locations = face_recognition.face_locations(rgb_img)
        # Encode faces
        face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
        encodings.extend(face_encodings)
    return encodings

def cluster_faces(encodings):
    # Use DBSCAN clustering algorithm to group similar faces
    clustering_model = DBSCAN(metric='euclidean', n_jobs=-1)
    clustering_model.fit(encodings)
    return clustering_model.labels_

def save_grouped_faces(images, labels, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for idx, label in enumerate(labels):
        label_folder = os.path.join(output_folder, str(label))
        if not os.path.exists(label_folder):
            os.makedirs(label_folder)
        img_path = os.path.join(label_folder, f"face_{idx}.jpg")
        cv2.imwrite(img_path, images[idx])

def main():
    input_folder = input("Enter the path to your photos and videos folder: ")
    output_folder = input("Enter the path to save grouped faces: ")
    images = load_images_from_folder(input_folder)
    encodings = detect_and_encode_faces(images)
    labels = cluster_faces(encodings)
    save_grouped_faces(images, labels, output_folder)

if __name__ == "__main__":
    main()
