import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

from ifg import IfgCalculator

matplotlib.rcParams["text.usetex"] = True
params = {
    "text.usetex": True,
    "font.size": 16,
    "font.family": "lmodern",
}
plt.rcParams.update(params)
rc("text", usetex=True)

temps = np.logspace(-2, 4, num=100)
temps1 = np.logspace(-2, 4, num=100)
vols = [0.1, 1, 10]

t = IfgCalculator(
    volumes=vols, temperatures=temps, input_in_si=False, output_in_si=False
)
vg = 10.0
g = 2.0
A = 3.0 / 5.0 * np.power(3.0 * np.square(np.pi) / np.sqrt(2.0) / g, 2.0 / 3.0)
beta = np.power(g * np.pi / 6.0, 2.0 / 3.0)
temps_high = np.logspace(-1, 4, num=100)
temps_low = np.logspace(-2.0, -0.1, num=100)
asymp_low = np.sqrt(
    10.0 * A / 9.0 * np.power(vg, -2.0 / 3.0)
    + 5.0 * beta / 9.0 * np.square(temps_low) * np.power(vg, 2.0 / 3.0)
)
asymp_high = np.sqrt(
    5.0 * temps_high / 3.0
    + 5.0 * np.power(np.pi, 1.5) / 6.0 / np.sqrt(temps_high) / g / vg
)

plt.plot(temps, t.C_S[:, 0], "k-", linewidth=2, label=r"{$v = 0.1$}")
plt.plot(temps, t.C_S[:, 1], "k--", linewidth=2, label=r"{$v = 1$}")
plt.plot(temps, t.C_S[:, 2], "k-.", linewidth=2, label=r"{$v = 10$}")
plt.plot(temps_low, asymp_low, "r-", linewidth=1, label=r"{low-$T$ asymp.}")
plt.plot(temps_high, asymp_high, "b-", linewidth=1, label=r"{high-$T$ asymp.}")

plt.text(2, 7.5, r"$C_S = \sqrt{(5/3)T}$")

plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"{\LARGE $T$, Ha}")
plt.ylabel(r"{\LARGE $C_S$, atomic units}")
plt.xlim(1e-2, 2e2)
plt.ylim(5e-1, 10)
plt.legend(loc="lower right")
plt.savefig("cs.pdf", bbox_inches="tight")
plt.show()
