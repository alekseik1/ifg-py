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
temps_high = np.logspace(-1.3, 4, num=100)
temps_low = np.logspace(-2, 0.3, num=100)

vg = 10.0
g = 2.0
A = 3.0 / 5.0 * np.power(3.0 * np.square(np.pi) / np.sqrt(2.0) / g, 2.0 / 3.0)
beta = np.power(g * np.pi / 6.0, 2.0 / 3.0)
asymp_low = 2.0 * A / 3.0 * np.power(vg, -5.0 / 3.0) + beta / 3.0 * np.square(
    temps_low
) * np.power(vg, -1.0 / 3.0)
asymp_high = temps_high / vg + np.power(np.pi, 1.5) / 2.0 / np.sqrt(
    temps_high
) / g / np.square(vg)
vols = [0.1, 1, 10]
# t = IfgCalculator(volumes=vols, temperatures=temps, input_in_si=False, output_in_si=False)
t = IfgCalculator(
    temperatures=temps, volumes=vols, input_in_si=False, output_in_si=False
)

plt.plot(temps, t.P[:, 0], "k-", linewidth=2, label=r"$v = 0.1$")
plt.plot(temps, t.P[:, 1], "k--", linewidth=2, label=r"$v = 1$")
plt.plot(temps, t.P[:, 2], "k-.", linewidth=2, label=r"$v = 10$")
plt.plot(temps_low, asymp_low, "b-", linewidth=1, label=r"low-$T$ asymp.")
plt.plot(temps_high, asymp_high, "r-", linewidth=1, label=r"high-$T$ asymp.")

plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"\LARGE $T$, Ha")
plt.ylabel(r"\LARGE $P$, atomic units")
plt.xlim(1e-2, 1e4)
plt.ylim(1e-2, 1e4)
plt.legend(loc="lower right")
plt.savefig("p.pdf", bbox_inches="tight")
plt.show()
