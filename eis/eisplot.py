#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def plot_eis(frequencies, impedance, title=None, cmap='tab10'):
    """ Creates a single figure w/ both Bode and Nyquist plots of a single EIS spectrum.
    Plots the results of a simulated circuit as well if provided

    Args:
        frequency (np.ndarray): numpy array of frequency values. Real, positive numbers
        impedance (np.ndarray): numpy array of impedance values. Imaginary numbers
        title (str): A figure title. Defaults to None.
        cmap (str): name of a matplotlib colormap for coloring multiple lines
    """
    fig, ax = plt.subplots(1, 3, figsize=(12,4))

    cmap = plt.get_cmap(cmap)
    if impedance.shape != frequencies.shape:
        colors = cmap(np.linspace(0,1,impedance.size))
        colors = colors[:,0:3]
        ax[0].set_prop_cycle(color=colors)
        ax[1].set_prop_cycle(color=colors)
        ax[2].set_prop_cycle(color=colors)
    else:
        colors = cmap(0)
    
    if impedance.shape != frequencies.shape:
        # plot multiple lines
        frequencies = np.repeat(frequencies, impedance.size).reshape((frequencies.size, impedance.size))
        impedance = np.vstack(impedance).transpose()
    
    # Bode Plot (1)
    ax[0].semilogx(frequencies, np.abs(impedance), "o")
    ax[0].set_title("Bode, |Z| vs. frequency")
    ax[0].set_xlabel("Freq [Hz]")
    ax[0].set_ylabel(r"|Z| [$\Omega$]", color="k")
    # Bode Plot (2)
    ax[1].semilogx(frequencies, np.angle(impedance, deg=True), "o")
    ax[1].set_title(r"Bode, $\angle$Z vs. frequency")
    ax[1].set_xlabel("Freq [Hz]")
    ax[1].set_ylabel(r"$\angle$Z [$^\circ$]", color="k")
    # Nyquist Plot
    ax[2].plot(np.real(impedance), -np.imag(impedance), "o")
    ax[2].set_aspect("equal")
    ax[2].invert_yaxis()
    ax[2].set_title("Nyquist")
    ax[2].set_xlabel(r"Re(Z) [$\Omega$]", color="k")
    ax[2].set_ylabel(r"Im(Z) [$\Omega$]", color="k")

    if title is not None:
        fig.suptitle(title)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    ...
