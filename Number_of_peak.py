
# A function to derive number of peaks in the periodogram of a lightcurve, 
# more detail about number of the peaks in the periodogram of a LC see ?? et al 
# @Saeed Hojjatpanah


def Number_peaks(time,flux,flux_err, visual=True):

	"""
	Input: 

	time: epoch in LC (numpy array)

	flux: LC flux (numpy array)

	flux_err: LC flux error (numpy array)

	Output:

	Number of significant peak in the periodogram (float number)
	
	if visual == True: plot the periodogram and see the significant peak(s)

	"""
	teresh = 10 # 10 % to define the significant peak, see ?? et al 
	model = LombScargleFast().fit(time, flux, flux_err)
	periods, power = model.periodogram_auto(nyquist_factor=100)
	max_t = max(time)-min(time)
	periods, power = zip(*((x, y) for x, y in zip(periods, power) if x > 0.2))
	periods, power = zip(*((x, y) for x, y in zip(periods, power) if x < max_t))
	peaks = peakdetect(power,periods,2)
	max_peaks , min_peaks = peaks[0] , peaks[1] 
	max_peaks_list, min_peaks_list = [], [] 
	max_peaks_time_list, min_peaks_time_list = [], [] 
	for extrer in max_peaks: 
		max_peaks_list.append(extrer[1]) 
		max_peaks_time_list.append(extrer[0]) 
	fig, ax = plt.subplots()
	try:
		max_peaks_time_list, max_peaks_list = zip(*((x, y) for x, y in zip(max_peaks_time_list, max_peaks_list) if y > max(power)*teresh/100))
		Number_of_peaks = len(max_peaks_list)
		if visual == True:
			plt.plot(periods, power,'--')
			plt.plot(max_peaks_time_list,max_peaks_list,'o')
	except:
		Number_of_peaks = 0
		plt.plot(periods, power,'--')
		print("no significant peak found")
		# plt.plot(max_peaks_time_list,max_peaks_list,'o')
	if visual == True:
		plt.axhline(y=max(power)*10/100, color='r')
		plt.title(f'Number of peaks: {Number_of_peaks}')
		plt.xlabel('Period [days]')
		plt.ylabel('Lomb-Scargle Power')
		plt.savefig(f'./lc_perio_number_peaks.png')
		plt.close()
	return Number_of_peaks