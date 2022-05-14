import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils.vis_utils import plot_model
import datatime
import os
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv("data/weight-height.csv")
df.plot(kind="scatter", x="Height", y="Weight", title="Weight(lb) and Height(in) in adults")

x_true = df[["Height"]].values
y_true = df["Weight"].values
y = []

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))
tf.keras.utils.plot_model(model,to_file="img/model01_lin_reg.png",show_shapes=True,show_layer_names=True,)
model.summary()
model.compile(tf.keras.optimizers.Adam(lr=0.6),loss="mean_squared_error",metrics=["mse"])

history = model.fit(x_true, y_true, epochs=50, verbose=1)
history.history.keys()
plt.plot(history.history["mean_squared_error"])
score = model.evaluate(x_true, y_true)
print("Test score:", score)

y_pred = model.predict(x_true)
df.plot(kind="scatter",x="Height",y="Weight",title="Weight and Height in adults",)
plt.plot(x_true, y_pred, color="red")
