def ex7():
    plot_sky(quasar_table['RA']*u.deg,quasar_table['DEC']*u.deg,nside=32, healpy=False)
