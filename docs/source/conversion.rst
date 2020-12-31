Conversion between SI and atomic
================================

Conversion is done using ``SiAtomicConverter`` class.
Currently, only SI and atomic units are supported.


Note that energy, heat capacity and entropy are specific (i.e. J/m^3 for energy).

========
Examples
========

.. code-block:: python

    from ifg_py import SiAtomicConverter

    # From SI to atomic
    converter = SiAtomicConverter(from_si=True)
    converter.convert_energy(1)
    # 2.2937123163853187e+17
    converter.convert_sound_speed(1)
    # 4.5710289062645205e-07

    # From atomic to SI
    converter = SiAtomicConverter(from_si=False)
    converter.convert_energy(1)
    # 4.35974465e-18
    converter.convert_sound_speed(1)
    # 2187691.2627472477

=============
API Reference
=============

.. autoclass:: ifg_py.units_converter.SiAtomicConverter
    :members:
