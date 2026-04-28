import cv2
import numpy as np
from numpy.linalg import norm

image1 = cv2.imread(r"lee.png")
image2 = cv2.imread(r"lee4.png")
if image1 is None or image2 is None:
                print("could not read one or both images")
else:
     print("image read successfully")
     gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
     gray_image2 =cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
     resized_image1 = cv2.resize(gray_image1, (50,50))
     resized_image2 = cv2.resize(gray_image2, (50,50))

     vector_image1 = resized_image1.flatten().astype(float)
     vector_image2 = resized_image2.flatten().astype(float)
     print(f"Vector image1: {vector_image1}")
     print(f"Vector image2: {vector_image2}")
     print(f"AI processing completed successfully:\n{vector_image1[:10]}")
     print(f"AI processing completed successfully:\n{vector_image2[:10]}")
     print("Processing completed.")
     print("_"*40)
     dot_product = np.dot(vector_image1, vector_image2)

     mag1=norm(vector_image1)
     mag2=norm(vector_image2)
ai_dot= dot_product/(mag1*mag2)
math_cosine= ai_dot * 100
print(f"cosine similarity:{math_cosine:.2f}%")
print("Cosine similarity calculation completed.")