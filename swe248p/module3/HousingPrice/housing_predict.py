import keras
import numpy as np
from keras.datasets import boston_housing
from keras import models
from keras import layers
import matplotlib.pyplot as plt

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
# print(train_data.shape)
# print(test_data.shape)
# print(train_targets)

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std


def build_model(hidden_units=64, activation_func='relu', n_layers=2):
    # Because we will need to instantiate
    # the same model multiple times,
    # we use a function to construct it.
    model = models.Sequential()
    model.add(layers.Dense(hidden_units, activation=activation_func,
                           input_shape=(train_data.shape[1],)))
    for _ in range(n_layers-1):
        model.add(layers.Dense(hidden_units, activation=activation_func))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


def k_fold_validation():
    k = 4
    num_val_samples = len(train_data) // k
    num_epochs = 100
    all_scores = []
    for i in range(k):
        print('processing fold #', i)
        # Prepare the validation data: data from partition # k
        val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
        val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]

        # Prepare the training data: data from all other partitions
        partial_train_data = np.concatenate(
            [train_data[:i * num_val_samples],
             train_data[(i + 1) * num_val_samples:]],
            axis=0)
        partial_train_targets = np.concatenate(
            [train_targets[:i * num_val_samples],
             train_targets[(i + 1) * num_val_samples:]],
            axis=0)

        # Build the Keras model (already compiled)
        model = build_model()
        # Train the model (in silent mode, verbose=0)
        model.fit(partial_train_data, partial_train_targets,
                  epochs=num_epochs, batch_size=1, verbose=0)
        # Evaluate the model on the validation data
        val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
        all_scores.append(val_mae)
    print(all_scores)
    print(np.mean(all_scores))


def longer_kfold():
    from keras import backend as K
    # Some memory clean-up
    K.clear_session()
    k = 4
    num_val_samples = len(train_data) // k
    num_epochs = 500
    all_mae_histories = []
    for i in range(k):
        print('processing fold #', i)
        # Prepare the validation data: data from partition # k
        val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
        val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]

        # Prepare the training data: data from all other partitions
        partial_train_data = np.concatenate(
            [train_data[:i * num_val_samples],
             train_data[(i + 1) * num_val_samples:]],
            axis=0)
        partial_train_targets = np.concatenate(
            [train_targets[:i * num_val_samples],
             train_targets[(i + 1) * num_val_samples:]],
            axis=0)

        # Build the Keras model (already compiled)
        model = build_model()
        # Train the model (in silent mode, verbose=0)
        history = model.fit(partial_train_data, partial_train_targets,
                            validation_data=(val_data, val_targets),
                            epochs=num_epochs, batch_size=1, verbose=0)
        mae_history = history.history['val_mae']
        all_mae_histories.append(mae_history)

    average_mae_history = [
        np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]


    plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
    plt.xlabel('Epochs')
    plt.ylabel('Validation MAE')
    plt.show()

    def smooth_curve(points, factor=0.9):
        smoothed_points = []
        for point in points:
            if smoothed_points:
                previous = smoothed_points[-1]
                smoothed_points.append(previous * factor + point * (1 - factor))
            else:
                smoothed_points.append(point)
        return smoothed_points

    smooth_mae_history = smooth_curve(average_mae_history[10:])

    plt.plot(range(1, len(smooth_mae_history) + 1), smooth_mae_history)
    plt.xlabel('Epochs')
    plt.ylabel('Validation MAE')
    plt.show()


def main(n_epochs, hidden_units, activation_func, n_layers):
    # Get a fresh, compiled model.
    model = build_model(hidden_units, activation_func, n_layers)
    # Train it on the entirety of the data.
    model.fit(train_data, train_targets,
              epochs=n_epochs, batch_size=16, verbose=0)
    test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
    f = open('result.txt', 'a')
    f.write(str(n_epochs) + '\t' + str(hidden_units) + '\t' + str(activation_func) + '\t' + str(n_layers) + '\t' + str(test_mse_score) + '\t' + str(test_mae_score) + '\n' )
    f.close()


if __name__ == "__main__":
    config = [
        (80, 64, 'relu', 2),
        (80, 64, 'relu', 3),
        (80, 64, 'relu', 4),
        (80, 64, 'relu', 1),
        (80, 64, 'tanh', 2),
        (80, 128, 'relu', 2),
        (80, 128, 'relu', 3),
        (80, 128, 'relu', 4),
    ]
    for (n_epochs, hidden_units, activation_func, n_layers) in config:
        main(n_epochs, hidden_units, activation_func, n_layers)





