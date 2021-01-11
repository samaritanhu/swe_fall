import keras
import numpy as np
from keras.datasets import imdb
from keras import models
from keras import layers
import matplotlib.pyplot as plt
from keras import optimizers

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
# print(keras.__version__)
# print(train_data[0])
# print(train_labels[0])
# print(max([max(sequence) for sequence in train_data]))

# word_index is a dictionary mapping words to an integer index
word_index = imdb.get_word_index()
# We reverse it, mapping integer indices to words
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# We decode the review; note that our indices were offset by 3
# because 0, 1 and 2 are reserved indices for "padding", "start of sequence", and "unknown".
decoded_review = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])
print(decoded_review)


def vectorize_sequences(sequences, dimension=10000):
    # Create an all-zero matrix of shape (len(sequences), dimension)
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.  # set specific indices of results[i] to 1s
    return results


# Our vectorized training data
x_train = vectorize_sequences(train_data)
# Our vectorized test data
x_test = vectorize_sequences(test_data)
print(x_train[0])

# Our vectorized labels
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')


def model_train_test_split():
    model = models.Sequential()
    model.add(layers.Dense(8, activation='relu', input_shape=(10000,)))
    # model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    x_val = x_train[:10000]
    partial_x_train = x_train[10000:]

    y_val = y_train[:10000]
    partial_y_train = y_train[10000:]

    history = model.fit(partial_x_train,
                        partial_y_train,
                        epochs=4,
                        batch_size=512,
                        validation_data=(x_val, y_val))

    history_dict = history.history
    print(history_dict.keys())

    acc = history.history['binary_accuracy']
    val_acc = history.history['val_binary_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    # "bo" is for "blue dot"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

    plt.clf()  # clear figure
    acc_values = history_dict['binary_accuracy']
    val_acc_values = history_dict['val_binary_accuracy']

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()


def train(n_layers, activation_function, learning_rate, loss, hidden_units):
    model = models.Sequential()
    model.add(layers.Dense(hidden_units, activation=activation_function, input_shape=(10000,)))
    for i in range(n_layers - 1):
        model.add(layers.Dense(hidden_units, activation=activation_function))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=optimizers.RMSprop(lr=learning_rate),
                  loss=loss,
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=4, batch_size=512)

    results = model.evaluate(x_test, y_test)
    print(model.metrics_names)
    print(results)
    f = open('result.txt', 'a')
    f.write(str(n_layers) + '\t' + activation_function + '\t' + str(learning_rate) + '\t' + loss + '\t' + str(
        hidden_units) + '\t' + str(results[1]) + '\n')
    f.close()


if __name__ == "__main__":
    # config = [
    #     (2, 'relu', 0.001, 'binary_crossentropy', 16),
    #     (1, 'relu', 0.001, 'binary_crossentropy', 16),
    #     (3, 'relu', 0.001, 'binary_crossentropy', 16),
    #     (1, 'relu', 0.001, 'binary_crossentropy', 32),
    #     (1, 'relu', 0.001, 'binary_crossentropy', 64),
    #     (1, 'relu', 0.001, 'binary_crossentropy', 8),
    #     (1, 'relu', 0.001, 'binary_crossentropy', 10),
    #     (2, 'relu', 0.001, 'binary_crossentropy', 32),
    #     (2, 'relu', 0.001, 'binary_crossentropy', 64),
    #     (2, 'relu', 0.001, 'binary_crossentropy', 8),
    #     (2, 'relu', 0.001, 'binary_crossentropy', 10),
    #     (3, 'relu', 0.001, 'binary_crossentropy', 32),
    #     (3, 'relu', 0.001, 'binary_crossentropy', 64),
    #     (3, 'relu', 0.001, 'binary_crossentropy', 8),
    #     (3, 'relu', 0.001, 'binary_crossentropy', 10),
    #     (2, 'tanh', 0.001, 'binary_crossentropy', 16),
    #     (1, 'tanh', 0.001, 'binary_crossentropy', 16),
    #     (3, 'tanh', 0.001, 'binary_crossentropy', 16),
    # ]

    config = [(2, 'relu', 0.001, 'binary_crossentropy', 16)]
    for (n_layers, activation_function, learning_rate, loss, hidden_units) in config:
        train(n_layers, activation_function, learning_rate, loss, hidden_units)
