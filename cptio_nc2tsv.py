#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Instalar CPT IO, no pacote do anaconda seguindo a instrução
To install this package run one of the following:conda install -c iri-nextgen cptio

Abrir ipython primeiro
"""

import cptio as cio
import xarray as xr

var_name = 'tmx'
input_file = '/mnt/c/Predictors_CPT/Predictors_Sept21/cru_ts4.07.1901.2022.tmx_MJJ.nc'
output_file = input_file.replace('.nc', '.tsv')

# Lendo o ficheiro netCDF da fonte CRU data
xdset = xr.open_dataset(input_file)

xdset = xdset.rename({'time': 'T', 'lon': 'X', 'lat': 'Y'})
xdset[var_name] = xdset[var_name].where(~xdset[var_name].isnull(), -9999.0)

xdset[var_name].attrs = {
    'field': var_name,
    'zlev': '0.0 meters',
    'nrow': str(xdset[var_name].shape[1]),
    'ncol': str(xdset[var_name].shape[2]),
    'row': 'Y',
    'col': 'X',
    'units': xdset[var_name].attrs['units'],
    'missing': '-9999.'
}

# Ultimo passo escrevendo e convertendo o ficheiro tsv
cio.to_cptv10(xdset[var_name], output_file)
