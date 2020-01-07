
# A function to derive F8 value in light curve, more detail about F8 value see ??: 
# @Saeed Hojjatpanah


def F8_proxy(time,flux,flux_err):

    """
    Input: 

    time: epoch time in LC (numpy array)

    flux: LC flux (numpy array)

    flux_err: LC flux error (numpy array)
    
    Output:

        mena F8 value (float), median F8 (float) [ppt]

    """

    index = np.where(time > time[-1] - 0.33328) # to figure out how we should devide time series in to 8 houres
    n = len(index[0]) ## n ~ 16 for kepler  
    flux_8h_list = [flux[i * n:(i + 1) * n] for i in range((len(flux) + n - 1) // n )]
    flux__err_8h_list = [flux_err[i * n:(i + 1) * n] for i in range((len(flux_err) + n - 1) // n )]
    list_f8 = [] 
    for i in range(0,len(flux_8h_list)):
        f8 = wrms(flux_8h_list[i],flux__err_8h_list[i])
        list_f8.append(f8)
    mean_F8 = np.mean(list_f8)
    median_F8 = np.median(list_f8)
    return mean_F8*1000, median_F8*1000