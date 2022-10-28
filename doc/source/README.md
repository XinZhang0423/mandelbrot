# README

## Introduction
Mandelbrot est un projet based on Python. Il est un projet pour TP final d'option AI a Ecole Centrale Nantes. Ce module peindre des figures de suite Mandelbrot et aussi de suite Julia. Currently available version is v1.0.0. Si vous voulez obtenir le Demo, cliquez [Demo]()

## Environnement
- python_requires = >= 3.6
- install_requires =
     numpy
     matplotlib

## Installation
- inatallationgit
`pip install setup.py`

## Usage et Resultats
```bash
$ MandelbrotPlot -o mandelbrot.png
$ JuliaPlot -o julia.png
```
![Mandelbrot par default](https://cdn.staticaly.com/gh/nililili7876/blog_pic@main/20221028/截图-2022-10-28-15-34-27.webp)
```bash
CPU times: user 3.4 s, sys: 931 ms, total: 4.33 s
Wall time: 4.37 s
```

![Julia par default](https://cdn.staticaly.com/gh/nililili7876/blog_pic@main/20221028/截图-2022-10-28-15-37-57.webp)
```bash
CPU times: user 10 s, sys: 3.52 s, total: 13.5 s
Wall time: 13.5 s
```

```bash
$ MandelbrotPlot --zmin=-0.7440+0.1305j\
                --zmax=-0.7425+0.1320j \
                --pixel_size=5e-7\
                --max-iter=50\
                -o "Mandelbrot_tentacle_lowiter.png" 
```
![Mandelbrot avec args](https://cdn.staticaly.com/gh/nililili7876/blog_pic@main/20221028/截图-2022-10-28-15-39-26.webp)
```bash
CPU times: user 6.34 s, sys: 2.07 s, total: 8.41 s
Wall time: 8.41 s
```

```bash
$ JuliaPlot -c=-0.8j\
            --pixel_size=1e-3\
            --max-iter=50\
            -o "thunder-julia.png" 
```
![Julia avec args](https://cdn.staticaly.com/gh/nililili7876/blog_pic@main/20221028/截图-2022-10-28-15-40-28.webp)

```bash
CPU times: user 9.63 s, sys: 3.73 s, total: 13.4 s
Wall time: 13.4 s
```

## Structure

Mandelbrot
├── LICENSE   
├── README.md
├── mandelbrot
│   ├── __init__.py
│   ├── __main__.py     # Appel en ligne de commande pour générer l'image voulue
│   ├── affichage.py     # Générer des visualisations des ensembles de Mandelbrot et Julia
│   └── mand_calcule.py     # Déterminer si un point du plan complexe appartient à l'ensemble de Mandelbrot.
├── pyproject.toml
├── setup.cfg
└── setup.py


## Maintainers
@LiNI, @AnranSHEN, @XinZHANG

## License
Licence = MIT