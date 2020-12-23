Welcome to ifg-py's documentation!
==================================
.. toctree::
    :maxdepth: 2

    conversion
    class_desc

Summary
=======
Numerical calculation of ideal Fermi gas (IFG) properties.

Currently supports temperatures in range [1e-49..1e+49] and
specific volumes in range [1e-30..1e+20].
Others are not tested.


Installation
============
Easily install via ``pip``
(note, however, that ``numpy`` should be installed first, see *Installation* on https://pypi.org/project/fdint/)::

    pip install numpy
    pip install ifg


Usage
=====

.. code-block:: python
    import numpy as np
    from ifg import IfgCalculator
    from ifg import get_metal_specific_volume

    # Aluminium
    v_array = np.array([get_metal_specific_volume(density_sgs=2.70, molar_mass_sgs=26.98, num_electrons=3)])

    T_range = np.hstack((
        np.arange(10**0, 10**4, 10),
        np.arange(10**4, 10**8, 1000),
    ))
    calculator = IfgCalculator(specific_volumes=v_array, temperatures=T_range, input_in_si=True, output_in_si=True)
    # Pressure
    print(calculator.P)
    # Entropy
    print(calculator.S)
    # Isobaric heat capacity
    print(calculator.C_P)

More examples are available in `ifg/examples.py` folder.

Support
=======

Feel free to open an issue on Github_ if you have any questions.
You can also contact me (email_, telegram_)

.. _Github: http://github.com/alekseik1/ifg-py
.. _email: mailto:1alekseik1@gmail.com
.. _telegram: https://t.me/alekseik1

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
