import tensorflow as tf
import tensorflow_hub as hub

# Define the URL for the FaceNet model from TensorFlow Hub
model_url = "https://tfhub.dev/google/tf2-preview/inception_resnet_v2/feature_vector/4"
model_url = "https://tfhub.dev/google/tf2-preview/inception_resnet_v2/feature_vector/4"


# Download the model
model = tf.keras.Sequential([
    hub.KerasLayer(model_url, trainable=False)
])

# Save the model to a file (optional)
model.save("facenet_model.h5")
