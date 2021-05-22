import numpy as np

objectives_penalizado = [1000000000,0,0]

# ADCS: id nombre costo masa vol confiabilidad potencia
ADCS = np.array([
    [1, "iMTQ_Magnetorquer_Board", 9600, 0.196, 0.17, 0.98, 1.2],
    [2, "IADCS-100", 120000, 0.4, 0.32, 0.98, 1.15],
])

# COM: id nombre costo masa vol confiabilidad potencia
COM = np.array([
    [1, "kit_isis", 11880, 0.164, 0.18, 0.98, 5.8],
    [2, "PULSAR-TMTC", 10823, 0.1, 0.1651, 0.995, 4.25],
    [3, "PULSAR-DATA", 17174, 0.1, 0.1741, 0.995, 5],
])

# EPS: id nombre costo masa vol confiabilidad potencia
EPS = np.array([
    [1, "isis_eps_a", 5520, 0.184, 0.26, 0.98, 32],
    [2, "isis_eps_b", 9600, 0.31, 0.21, 0.98, 64],
    [3, "isis_eps_c", 12000, 0.36, 0.21, 0.98, 64],
    [4, "modular_eps", 23760, 0.4161, 0.54, 0.995, 39],
    [5, "starbuck-nano-photon", 10934, 0.221, 0.162, 0.995, 60],
])

# OBC: id nombre costo masa vol confiabilidad potencia
OBC = np.array([
    [1, "ISIS_On_Board_Computer", 5280, 0.094, 0.124, 0.98, 0.4],
    [2, "KRYTEN-M3", 8624, 0.0619, 0.0551, 0.995, 0.6],
    [3, "SIRIUS_OBC_LEON3FT", 23285, 0.13, 0.0551, 0.995, 1.3],
    [4, "SIRIUS_TMC_LEON3FT", 32340, 0.13, 0.1720, 0.995, 1.3],
])

# STR: id costo U(factor) confiabilidad
STR = np.array([
    [1, 2580, 1, 0.98],
    [2, 3870, 1.5, 0.98],
    [3, 3540, 2, 0.98],
    [4, 3780, 2, 0.98],
    [5, 4380, 3, 0.98],
    [6, 6960, 4, 0.98],
    [7, 8820, 6, 0.98],
    [8, 11400, 8, 0.98],
])

# PL: id nombre costo masa volumen confiabilidad potencia
PL_list = np.array([
    [1, "gecko", 31680, 0.40, 0.65, 0.98, 2.70],
    [2, "chameleon", 224280, 1.60, 2.15, 0.98, 7.00],
    [3, "mantis", 68280, 0.50, 0.65, 0.98, 4.50],
    [4, "piCAM-FM", 3948, 0.1, 0.19, 0.98, 0.297],
    [5, "caiman", 140280, 1.8, 2.65, 0.98, 10],
    [6, "TriScape_100", 48000, 1.1, 1.76, 0.985, 6],
    [7, "HyperScape_100", 182400, 1.2, 1.76, 0.985, 5.5],
    [8, "ThermoVision_A10", 400, 0.12, 0.4826, 0.9, 1.5],
    [9, "Tau_320", 1300, 0.479, 0.2921, 0.9, 1],
    [10, "Vacio", 0, 0, 0, 1, 0],
])

# GSD[LR,MR,HR]
GSD = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
])

# RE[UV,VIS,NIR,SWIR,MWIR,TIR,MW]
RE = np.array([
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
])

# Rentabilidad
RENT = np.array([
    [0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 16, 0, 24, 0],
    [0, 0, 0, 28, 0, 42, 0],
    [12, 20, 8, 8, 0, 0, 10],
    [21.6, 36, 14.4, 14.4, 18, 21.6, 18],
    [36, 60, 14.4, 24, 30, 36, 30],
    [13.2, 0, 8.8, 8, 0, 0, 10],
    [19.2, 0, 16, 12.8, 0, 19.2, 16],
    [42, 0, 16, 28, 0, 42, 35],
    [12, 20, 0, 8, 0, 0, 10],
    [26.4, 44, 0, 17.6, 0, 0, 22],
    [43.2, 72, 0, 28.8, 0, 0, 36],
    [0, 0, 0, 8, 0, 0, 10],
    [0, 0, 0, 19.2, 0, 0, 24],
    [0, 0, 0, 28.8, 0, 0, 36],
    [0, 0, 12.8, 0, 0, 0, 10],
    [0, 0, 20, 0, 25, 30, 25],
    [0, 0, 20, 0, 38, 45.6, 38],
    [24, 0, 0, 0, 0, 0, 20],
    [48, 0, 0, 0, 40, 48, 40],
    [72, 0, 0, 0, 60, 72, 60],
])

costo_fijo=8000
