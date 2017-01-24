""" This module contains functions to:
    i) Process UV-Vis data and
    ii) Plot Tramitance vs. Eg data

    Created by: Daniel Casas-Orozco
    Date: 24/01/17
"""

from __future__ import division


def process_data(raw_data, scaling_factors):
    """
    Inputs
    ----------
    raw_data : array_type
        UV-Vis raw data organized in columns. First column contains wavelength
        values (nm) and tramitance values (au.) from second column on .

    scaling_factors : tuple
        Contains numbers in the range 0 - 1 which are intended to multiply
        tramitance values, so all plots are in the same order of magnitude.

    Returns
    --------------
    Eg_values : array_type
        Energy values (eV) obtained from wavelength data.

    scaled_tramitance : array_type
        Tramitance data multiplied by their corresponding scaling factors

    """

    # Extract data
    wavelength = raw_data[:, ::2]
    tramitance = raw_data[:, 1::2]

    # Process data
    planck_ct = 1.23984193e3  # eV*nm

    Eg_values = planck_ct/wavelength  # matrix operation
    scaled_tramitance = tramitance*scaling_factors  # matrix operation

    return Eg_values, scaled_tramitance


def plot_uv_vis(Eg_array, tramitance_array, offset):

    import matplotlib.pyplot as plt
    from matplotlib.ticker import AutoMinorLocator

    fig, axis = plt.subplots()
    number_plots = len(Eg_array.T)

    offset_acum = 0

    # --------------- Iterate to plot all curves

    for ind in range(number_plots):
        axis.plot(Eg_array[:, ind], tramitance_array[:, ind] + offset_acum)

        offset_acum += offset

    # --------------- Edit plots
    # Labels on axes
    axis.set_xlabel('Energy (eV)')
    axis.set_ylabel('Intensity (au)')

    # Put minor ticks
    axis.xaxis.set_minor_locator(AutoMinorLocator(2))
    axis.xaxis.set_ticks_position('bottom')  # xticks only at bottom
    axis.yaxis.set_ticks('left')  # yticks only at left

    return fig, axis
