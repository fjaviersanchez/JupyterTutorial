def ex4():
    masks = [np.logical_and(table['purity']>i/4.,table['purity']<(i+1)/4.) for i in range(0,4)]
    for i in range(0,4):
        label = str(i/4.)+' < purity < '+str((i+1)/4.)
        plt.hist(table['snr_iso'][masks[i]],range=(0,20),bins=40, label=label, alpha=0.5, normed=True)
    plt.legend()
    plt.figure()
    for i in range(0,4):
        label = str(i/4.)+' < purity < '+str((i+1)/4.)
        plt.hist(table['snr_grpf'][masks[i]],range=(0,20),bins=40, label=label, alpha=0.5, normed=True)
    plt.legend()
