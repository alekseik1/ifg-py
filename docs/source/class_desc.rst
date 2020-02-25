Calculating properties using class
===================================
All calculations are performed by a single simple class.
*The class solves all unit conversion problems*.

Currently, it is impossible to reuse same class object for calculating
another gas. You need to create *another* class instance instead.

========
Examples
========

.. code-block:: python

    from ifg_py import IfgCalculator, get_metal_specific_volume
    import numpy as np

    # see `get_metal_specific_volume` reference for details
    v_al = get_metal_specific_volume(density_sgs=2.70, molar_mass_sgs=26.98, num_electrons=3)
    T_range = np.array([1, 10, 100, 1000])

    calculator = IfgCalculator(temperatures=T_range, specific_volumes=v_al, input_in_si=True, output_in_si=True)

    calculator.mu
    # array([[9.82775992e+16], [9.82775987e+16], [9.82775550e+16], [9.82731832e+16]])
    calculator.p
    # array([[1.56068519e-16], [1.56068523e-16], [1.56068870e-16], [1.56103577e-16]])


=============
API Reference
=============

.. autoclass:: ifg_py.ifg.IfgCalculator
    :members:
