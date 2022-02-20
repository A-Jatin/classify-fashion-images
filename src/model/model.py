import tensorflow as tf


class CNN:

    @staticmethod
    def create_model(config):
        """
        Creates a simple sequential model
        """

        cnn = tf.keras.Sequential()

        cnn.add(tf.keras.layers.InputLayer(input_shape=(
        config["image_dimension"]["img_width"], config["image_dimension"]["img_height"],
        config["image_dimension"]["channels"])))

        # Normalization
        cnn.add(tf.keras.layers.BatchNormalization())

        # Conv + Maxpooling
        cnn.add(tf.keras.layers.Convolution2D(64, (4, 4), padding='same', activation='relu'))
        cnn.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

        # Dropout
        cnn.add(tf.keras.layers.Dropout(0.1))

        # Conv + Maxpooling
        cnn.add(tf.keras.layers.Convolution2D(64, (4, 4), activation='relu'))
        cnn.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

        # Dropout
        cnn.add(tf.keras.layers.Dropout(0.3))

        # Converting 3D feature to 1D feature Vektor
        cnn.add(tf.keras.layers.Flatten())

        # Fully Connected Layer
        cnn.add(tf.keras.layers.Dense(256, activation='relu'))

        # Dropout
        cnn.add(tf.keras.layers.Dropout(0.5))

        # Fully Connected Layer
        cnn.add(tf.keras.layers.Dense(64, activation='relu'))

        # Normalization
        cnn.add(tf.keras.layers.BatchNormalization())

        cnn.add(tf.keras.layers.Dense(config["num_classes"], activation='softmax'))
        cnn.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(), metrics=['accuracy'])

        return cnn
