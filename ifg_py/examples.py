from ifg_py import SiAtomicConverter, get_metal_specific_volume
import numpy as np

from ifg_py.ifg import get_all_properties

if __name__ == '__main__':

    v_range = dict(
        small=1.0,
        Al=get_metal_specific_volume(density_sgs=2.70, molar_mass_sgs=26.98, num_electrons=3),
        huge=500.0
    )

    print(v_range)
    v_array = np.array([float(x) for x in v_range.values()])
    converter = SiAtomicConverter(from_si=True)
    T_range = np.hstack((
        np.arange(10**0, 10**4, 10),
        np.arange(10**4, 10**8, 1000),
    ))
    T_range = converter.convert_temperature(T_range)
    high_properties = get_all_properties(v_array, T_range, csv_dir='data/all_temperatures')
