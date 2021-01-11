"""Thermodynamic properties of ideal Fermi-gas

The module calculate all thermodynamic properties of ideal Fermi-gas,
including second derivatives of thermodynamic potential. The module
uses both atomic and SI systems of units. Brief description of usage:

import ifg
vols = [1./1.e29]      # Array of volumes (in SI units, m^3)
temps = [1.e3, 1.e4]   # Array of temperatures (in SI units, K)
# Initialization, input and output in SI (False means atomic units)
t = ifg.IfgCalculator(vols, temps, input_in_si=True, output_in_si=True)
t.get_all_properties()
# Output: E - energy (J/m^3), S - entropy (J/K/m^3),
# P - pressure (Pa), C_V - isochoric heat capacity (J/K/m^3),
# C_S - adiabatic sound velocity (km/s), ... All properties
# are 2D arrays, first index - temperature, second index - volume
t.E[1, 0]
5343662281313.693
"""

from ifg.calculator import IfgCalculator
from ifg.units_converter import SiAtomicConverter, get_metal_specific_volume

from ifg.metadata import __version__

__all__ = [
    'IfgCalculator', 'SiAtomicConverter',
    'get_metal_specific_volume', '__version__'
]
