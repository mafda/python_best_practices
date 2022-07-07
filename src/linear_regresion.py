"""Linear regression is a simple machine learning algorithm.
"""

import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam


def main():
    """Main function to solve a linear regression problem."""
    weight_height_df = pd.read_csv("data/weight-height.csv")
    weight_height_df.plot(
        kind="scatter",
        x="Height",
        y="Weight",
        title="Weight(lb) and Height(in) in adults",
    )

    x_true = weight_height_df[["Height"]].values
    y_true = weight_height_df["Weight"].values

    model = Sequential()
    model.add(Dense(1, input_shape=(1,)))

    model.compile(
        Adam(learning_rate=0.6),
        loss="mean_squared_error",
        metrics=["mse"],
    )

    history = model.fit(x_true, y_true, epochs=50, verbose=1)
    history.history.keys()
    plt.plot(history.history["mse"])

    score = model.evaluate(x_true, y_true)
    print("Test score:", score)

    y_pred = model.predict(x_true)
    weight_height_df.plot(
        kind="scatter",
        x="Height",
        y="Weight",
        title="Weight and Height in adults",
    )

    plt.plot(x_true, y_pred, color="red")


if __name__ == "__main__":
    main()
