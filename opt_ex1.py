def opt_ex1():
    from sklearn.neighbors import KNeighborsRegressor
    knn = KNeighborsRegressor(12, weights='distance')
    #Train the KNN
    knn.fit(mag_train, z_train)
    #Test it!
    z_fit_train = knn.predict(mag_train)
    z_fit = knn.predict(mag_test)
    #Compute rms in the training set and test set
    rms_train = np.mean(np.sqrt((z_fit_train - z_train) ** 2))
    rms_test = np.mean(np.sqrt((z_fit - z_test) ** 2))
    plt.scatter(z_test,z_fit, color='k', s=0.1)
    plt.plot([-0.1, 6], [-0.1, 6], ':k')
    plt.text(0.04, 5, "rms = %.3f" % (rms_test))
    plt.xlabel('$z_{true}$')
    plt.ylabel('$z_{fit}$')


