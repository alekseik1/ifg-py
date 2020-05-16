import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from ifg import IfgCalculator
from matplotlib import rc


matplotlib.rcParams['text.usetex'] = True
params = {'text.usetex': True,
          'font.size': 16,
          'font.family': 'lmodern',
          }
plt.rcParams.update(params)
rc('text', usetex=True)

temps = np.logspace(-2, 4, num=100)
temps_high = np.logspace(-1.3, 4, num=100)
temps_low = np.logspace(-2, 0.3, num=100)

vg = 10.
g = 2.
A = 3. / 5. * np.power(3. * np.square(np.pi) / np.sqrt(2.) / g, 2./3.)
beta = np.power(g * np.pi / 6., 2./3.)
asymp_low = 2. * A / 3. * np.power(vg, -5./3.) + \
            beta / 3. * np.square(temps_low) * np.power(vg, -1./3.)
asymp_high = temps_high / vg + np.power(np.pi, 1.5) / 2. / np.sqrt(temps_high) / g / np.square(vg)
vols = [0.1, 1, 10]
t = IfgCalculator(specific_volumes=vols, temperatures=temps, input_in_si=False, output_in_si=False)

plt.plot(temps, t.p[:, 0], 'k-', linewidth=2, label=r'$v = 0.1$')
plt.plot(temps, t.p[:, 1], 'k--', linewidth=2, label=r'$v = 1$')
plt.plot(temps, t.p[:, 2], 'k-.', linewidth=2, label=r'$v = 10$')
plt.plot(temps_low, asymp_low, 'b-', linewidth=1, label=r'low-$T$ asymp.')
plt.plot(temps_high, asymp_high, 'r-', linewidth=1, label=r'high-$T$ asymp.')

plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'\LARGE $T$, Ha')
plt.ylabel(r'\LARGE $P$, atomic units')
plt.xlim(1e-2, 1e4)
plt.ylim(1e-2, 1e4)
plt.legend(loc='lower right')
plt.savefig('p.pdf', bbox_inches='tight')
plt.show()
