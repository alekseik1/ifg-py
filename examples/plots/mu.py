import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from ifg import IfgCalculator


matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['mathtext.fontset'] = 'cm'
params = {'text.usetex': True,
          'font.size': 16,
          'font.family': 'lmodern',
          }
plt.rcParams.update(params)

g = 2
temps = np.logspace(-2, 4, num=100)
temps10_high = np.logspace(-2, 2, num=100)
temps10_low = np.logspace(-2, 0.7)

vols = [0.1, 1, 10]
t = IfgCalculator(specific_volumes=vols, temperatures=temps, input_in_si=False, output_in_si=False)

vg = 10.
e_fermi = np.power(3. * np.square(np.pi) / np.sqrt(2.) / g / vg, 2./3.)
asymp1_low = e_fermi * (1. - np.pi * np.pi / 12. * np.square(temps10_low / e_fermi))
mu_b = temps10_high * np.log(1. / g / vg * np.power(2. * np.pi / temps10_high, 1.5))
asymp1_high = mu_b + temps10_high * np.power(np.pi, 1.5) / g / vg / np.power(temps10_high, 1.5)

plt.plot(temps, t.mu[:, 0], 'k-', label=r'{$v = 0.1$}', linewidth=2)
plt.plot(temps, t.mu[:, 1], 'k--', label=r'{$v = 1$}', linewidth=2)
plt.plot(temps, t.mu[:, 2], 'k-.', label=r'{$v = 10$}', linewidth=2)
plt.plot(temps10_low, asymp1_low, 'b-', linewidth=1, label=r'low-$T$ asymp.')
plt.plot(temps10_high, asymp1_high, 'r-', linewidth=1, label=r'high-$T$ asymp.')

plt.xscale('log')
plt.xlabel(r'{\LARGE $T$, Ha}')
plt.ylabel(r'{\LARGE $\mu$')
plt.xlim(1e-2, 1e2)
plt.ylim(-30, 30)
plt.legend(loc='lower left')
plt.savefig('mu.pdf', bbox_inches='tight')
plt.show()
