def opt_nn():
    from keras.models import Sequential
    from keras.layers import Dense, Activation, Flatten, Dropout
    from keras.layers.convolutional import Convolution2D, MaxPooling2D
    from keras.layers import Embedding
    from keras.layers.recurrent import LSTM
    #Code for Convolutional Neural Network (it doesn't work)

    # First we have to initialize the neural network using Sequential()
    #cnn = Sequential()
    # process the data to fit in a keras CNN properly
    # input data needs to be (N, C, X) - shaped where
    # N - number of samples
    # C - number of channels per sample
    # X - sample size

    #cnn.add(Convolution1D(64, 4,
    #    border_mode="same",
    #    activation="relu",
    #    input_shape=(1, 4)))
    #cnn.add(Convolution1D(64, 2, border_mode="same"))
    #cnn.add(Convolution1D(64, 1, border_mode="same"))
    #cnn.add(Flatten())
    #cnn.add(Dense(256, activation="relu"))
    #cnn.add(Dropout(0.5))
    #cnn.add(Dense(32, activation="relu"))
    #cnn.add(Dense(1, activation="softmax"))
    #cnn.compile(loss="mse", optimizer="rmsprop")

    #Code for LTSM RNN
    model = Sequential()
    model.add(LSTM(64,input_dim=4, return_sequences=False, activation='tanh'))
    model.add(Dense(128))
    model.add(Dense(64, init='normal', activation='tanh'))
    model.add(Dense(4, init='normal', activation='tanh'))
    model.add(Dense(1, init='normal'))
    model.compile(loss='mse', optimizer='rmsprop')

    colors = np.vstack([quasar_table['PSFMAG_%d' % f]-quasar_table['PSFMAG_%d' % (f+1)] for f in range(0,4)]).T
    color_train = colors[::5]
    color_test = colors[::18]
    batch_size = len(z_train)
    model.fit(color_train.reshape(-1,1,4), z_train, batch_size=batch_size, nb_epoch=300, verbose=0, validation_split=0.5)
    predicted_output = model.predict_on_batch(color_test.reshape(-1,1,4))
    rms_lstm = np.mean(np.sqrt((z_test-predicted_output)**2))
    plt.scatter(z_test,predicted_output, color='k', s=0.1)
    plt.plot([-0.1, 6], [-0.1, 6], ':k')
    plt.text(0.04, 5, "rms = %.3f" % (rms_lstm))
    plt.xlabel('$z_{true}$')
    plt.ylabel('$z_{fit}$')


