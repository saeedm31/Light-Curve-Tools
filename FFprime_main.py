

# A function to derive FF' value in light curve, more detail about FF' in Aigrain et al 2012: 
# @Saeed Hojjatpanah


def FFprime(k_delta_V_c, k, time, flux, err, Rstar):

	"""
	Input : 
	k_delta_V_c: constant 
	k: constant
	time: epoch, time array
	flux: LC flux
	err: error in flux
	Rstar: Star's radiues

	Output:
	
	FF' value 

	"""

	s = interp1d(time, flux, fill_value='extrapolate')
	deri = derivative(s,time)
	sprime = interp1d(time, deri,fill_value='extrapolate')
	sigma = np.std(flux)
	Psi_0 = flux.max() + k*sigma  # from Aigrain 2012 eq.13
	print("Psi_0",Psi_0)
	# Psi_0 = phot.max() * 1.014  # value from Haywood 2014
	f = (Psi_0 - flux.min()) / Psi_0   # eq. 14
	Delta_RV_rot = - (deri / Psi_0) * (1 - s(time)/Psi_0) * Rstar / f
	Delta_RV_c =  (1 - s(time)/Psi_0)**2 * (k_delta_V_c*k / f)
	x = Delta_RV_rot + Delta_RV_c
	ffprime = np.sqrt(np.mean(np.square(x)))
	return ffprime


