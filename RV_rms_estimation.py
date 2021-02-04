

import numpy as np
from uncertainties import ufloat, umath

LC_peak_to_peak = 4.16 # ppt

def RV_jitter(x=LC_peak_to_peak):
	"""
	input: TESS peak to peak light kurve variability [ppt]

	Out : RV jitter [m/s]
	"""
	x0, y0, k1, k2 = 0.813, 0.548, 0.273, 1.381

	x0_up, y0_up, k1_up, k2_up = ufloat(0.813,0.484), ufloat(0.548, 0.437), \
	 ufloat(0.273,0.306), ufloat(1.381, 1,305)
	x0_down, y0_down, k1_down, k2_down = ufloat(0.813, 0.792), ufloat(0.548, 0.366), \
	 ufloat(0.273, 0.268), ufloat(1.381, 0.735)

	if np.log10(x) > 2 or np.log(x) < 0:
		print('Photometric variability is out of the range !')
		y, y_up, y_down = None, None, None
	elif np.log10(x) < x0:
		y = np.round(10**(k1*np.log10(x) + y0 - k1*x0),2)
		y_up = 10**(k1_up*np.log10(x) + y0_up - k1_up*x0_up)
		y_down = 10**(k1_down*np.log10(x) + y0_down - k1_down*x0_down)
	else:
		y = np.round(10**(k2*np.log10(x) + y0 - k2*x0),2)
		y_up = 10**(k2_up*np.log10(x) + y0_up - k2_up*x0_up)
		y_down = 10**(k2_down*np.log10(x) + y0_down - k2_down*x0_down)
	if y:
		y = np.array([y_up, y_down]).mean()
	else:
		y = None
	return y, y_up, y_down

y, y_up, y_down = RV_jitter(LC_peak_to_peak)

print(f'RV jitter = {y} m/s')