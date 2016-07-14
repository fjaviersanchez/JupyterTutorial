def ex3():
    rs = np.random.RandomState(112)
    x=np.linspace(0,10,11)
    y=np.linspace(0,10,11)
    X,Y = np.meshgrid(x,y)
    X=X.flatten()
    Y=Y.flatten()
    weights=np.random.random(len(X))
    sns.jointplot(X,Y,kind='hex',joint_kws={'C':weights}); #The semicolon here avoids that Jupyter shows the resulting arrays
