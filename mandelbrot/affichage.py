import numpy as np
import matplotlib.pyplot as plt
from .mand_calcule import is_in_Mandelbrot,is_in_Julia

np.warnings.filterwarnings("ignore")

def plot_mandelbrot(zmin=-2 - 2j,
                    zmax=2 + 2j,
                    pixel_size=0.001,
                    max_iter=50,
                    figname="Mandelbrot.png"):
    """afficher et save la figure de suite Mandelbrot 

    Args:
        zmin (_type_, optional): _description_. Defaults to -2-2j.
        zmax (_type_, optional): _description_. Defaults to 2+2j.
        pixel_size (float, optional): _description_. Defaults to 0.001.
        max_iter (int, optional): _description_. Defaults to 50.
        figname (str, optional): _description_. Defaults to "Mandelbrot.png".
    """
    reals = np.arange(zmin.real, zmax.real, pixel_size)
    imags = np.arange(zmin.imag, zmax.imag, pixel_size)
    x, y = np.meshgrid(reals, imags)
    c = np.array(x + y * 1j, dtype=complex)
    
    plt.figure(figsize=(15, 15))
    plt.imshow(is_in_Mandelbrot(c, max_iter), cmap="binary")
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    plt.savefig(figname)





def plot_julia(c=-0.8 + 0.156j,
               zmin=-2-1j,
               zmax=2+1j,
               pixel_size=5e-4,
               max_iter=100,
               figname="Julia.png"):
    """afficher et save la figure de suite Mandelbrot 

    Args:
        c (_type_, optional): _description_. Defaults to -0.8 + 0.156j.
        zmin (_type_, optional): _description_. Defaults to -2-1j.
        zmax (_type_, optional): _description_. Defaults to 2+1j.
        pixel_size (float, optional): _description_. Defaults to 0.0005.
        max_iter (int, optional): _description_. Defaults to 100.
        figname (str, optional): _description_. Defaults to "Julia.png".
    """
    reals = np.arange(zmin.real, zmax.real, pixel_size)
    imags = np.arange(zmin.imag, zmax.imag, pixel_size)
    x, y = np.meshgrid(reals, imags)
    z = np.array(x + y * 1j, dtype=complex)
    
    plt.figure(figsize=(15, 15))
    plt.imshow(is_in_Julia(z,c, max_iter), cmap="binary",alpha=0.5)
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    plt.savefig(figname)