
# Simple function to seprate light curve in known transit(s) and out trasit
# single known transit

import numpy as np


####


def split_transit_LC(time,flux, flux_err, transit_time,\
 transit_duration, transit_peiod, mode='out_transit'):
	"""
	In : 
	time: array
	flux: array
	flux: array
	transit_time: float, known first transit time
	transit_duration: float, [hour]
	transit_peiod: float, [day]
	mode: 'transit' or 'out_transit' 

	Out:

	time, flux, flux_err : array : in or out of transit depends the selected mode
	"""

	final_index = []
	all_index = np.arange(0,len(time))
	transit_duration_h = transit_duration/(2.0*24) # half transit du in h
	tran, i = transit_time , 0
	while tran < max(time):
		transi_index = np.where((time > transit_time+i*transit_peiod-\
			transit_duration_h)&(time < transit_time+i*transit_peiod+\
			transit_duration_h))
		tran = transit_time+i*transit_peiod
		i += 1
		final_index.append(transi_index[0])
	index_transits = np.concatenate((final_index[0:-1]), axis=None)
	final_no_transit_index = [x for x in all_index.tolist() if x not in index_transits]
	if mode == 'transit':
		return time[index_transits],flux[index_transits], flux_err[index_transits]
	elif mode == 'out_transit':
		return time[final_no_transit_index],flux[final_no_transit_index], flux_err[final_no_transit_index]
