def ex6():
    colors = np.vstack([quasar_table['PSFMAG_%d' % f]-quasar_table['PSFMAG_%d' % (f+1)] for f in range(0,4)]).T
    color_train = colors[::5]
    color_test = colors[::20]
    clf.fit(color_train, z_train)
    #Test it!
    z_fit_train = clf.predict(color_train)
    z_fit = clf.predict(color_test)
    #Compute rms in the training set and test set
    rms_train = np.mean(np.sqrt((z_fit_train - z_train) ** 2))
    rms_test = np.mean(np.sqrt((z_fit - z_test) ** 2))
    plt.scatter(z_test,z_fit, color='k', s=0.1)
    plt.plot([-0.1, 6], [-0.1, 6], ':k')
    plt.text(0.04, 5, "rms = %.3f" % (rms_test))
    plt.xlabel('$z_{true}$')
    plt.ylabel('$z_{fit}$')
