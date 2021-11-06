import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text

model = tf.keras.Sequential([
  hub.KerasLayer(
      "https://tfhub.dev/google/universal-sentence-encoder/4",
      input_shape=[],
      dtype=tf.string,
      trainable=False
  )
])

model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    optimizer="Adam"
)
export_path = "use/model/use_v4"
model.save(export_path, save_format=tf)