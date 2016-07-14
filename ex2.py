def ex2():
    rs = np.random.RandomState(112)
    x=np.linspace(0,10,11)
    y=np.linspace(0,10,11)
    X,Y = np.meshgrid(x,y)
    X=X.flatten()
    Y=Y.flatten()
    weights=np.random.random(len(X))
    plt.hist2d(X,Y,weights=weights); #The semicolon here avoids that Jupyter shows the resulting arrays
