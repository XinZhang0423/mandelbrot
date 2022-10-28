"""Main call to mandelbrot. Mostly a parser."""
import argparse
from .affichage import plot_mandelbrot,plot_julia

def MandelbrotPlot():
    """Draw la suite Mandelbrot with des arguments suivants"""
    parser = argparse.ArgumentParser(description='Draw mandelbrot')
    parser.add_argument('--zmin',metavar='zmin', type=complex,default=-2-2j,
                        help='input zmin,default:-2-2j')
    parser.add_argument('--zmax',metavar='zmax', type=complex,default=2+2j,
                        help='input zmax,default=2+2j')
    parser.add_argument('--pixel_size',metavar='pixel_size', type=float,default=0.001,
                        help='input pixel_size,default:0.01')
    parser.add_argument('--max_iter',metavar='max-iter', type=int,default=50,
                        help='input max_iter,default:50')
    parser.add_argument('-o',metavar='pathname', type=str,default='mandelbrot.png',
                        help='input pathname')

    args = parser.parse_args()
    plot_mandelbrot(zmin=args.zmin,zmax = args.zmax,
                        pixel_size = args.pixel_size,max_iter=args.max_iter,
                        figname=args.o)

def JuliaPlot():
    """Draw la suite Mandelbrot with des arguments suivants"""
    parser = argparse.ArgumentParser(description='Draw Julia')
    parser.add_argument('-c',metavar='c de Julia', type=complex,default=-0.8+0.156j,
                        help='input c de Julia,default:-0.8+0.156j')
    parser.add_argument('--zmin',metavar='zmin', type=complex,default=-2-1j,
                        help='input zmin,default:-2-1j')
    parser.add_argument('--zmax',metavar='zmax', type=complex,default=2+1j,
                        help='input zmax,default=2+1j')
    parser.add_argument('--pixel_size',metavar='pixel_size', type=float,default=5e-4,
                        help='input pixel_size,default:5e-4')
    parser.add_argument('--max_iter',metavar='max-iter', type=int,default=100,
                        help='input max_iter,default:100')
    parser.add_argument('-o',metavar='pathname', type=str,default='julia.png',
                        help='input pathname')

    args = parser.parse_args()
    plot_julia(c=args.c,zmin=args.zmin,zmax = args.zmax,
                        pixel_size = args.pixel_size,max_iter=args.max_iter,
                        figname=args.o)