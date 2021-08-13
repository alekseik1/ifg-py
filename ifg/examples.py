import numpy as np

from ifg import IfgCalculator, get_metal_specific_volume

if __name__ == "__main__":

    v_range = dict(
        small=get_metal_specific_volume(
            density_sgs=100, molar_mass_sgs=26.98, num_electrons=3
        ),
        Al=get_metal_specific_volume(
            density_sgs=2.70, molar_mass_sgs=26.98, num_electrons=3
        ),
        huge=get_metal_specific_volume(
            density_sgs=0.01, molar_mass_sgs=26.98, num_electrons=3
        ),
    )

    print(v_range)
    v_array = np.array([float(x) for x in v_range.values()])
    T_range = np.hstack(
        (
            np.arange(10 ** 0, 10 ** 4, 10),
            np.arange(10 ** 4, 10 ** 8, 1000),
        )
    )
    calculator = (
        IfgCalculator()
        .with_volumes(v_array, in_si=True)
        .with_temperatures(T_range, in_si=True)
        .with_output_in_si()
    )
    calculator.get_all_properties("data/all_temperatures")
    calculator.get_all_properties()
