import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

from ifg import IfgCalculator

matplotlib.rcParams["text.usetex"] = True
params = {
    "text.usetex": True,
    "font.size": 11,
    "font.family": "lmodern",
}
plt.rcParams.update(params)
rc("text", usetex=True)

temps = np.logspace(-2, 4, num=100)
temps1 = np.logspace(-2, 4, num=100)
temps_cv_high = np.logspace(0.7, 4, num=100)
temps_cp_high = np.logspace(0.7, 4, num=100)
asymp1 = temps1 * (math.pow(np.pi / 3.0, 2.0 / 3.0)) * math.pow(0.1, 2.0 / 3.0)
asymp2 = temps1 * (math.pow(np.pi / 3.0, 2.0 / 3.0)) * math.pow(1, 2.0 / 3.0)
asymp3 = temps1 * (math.pow(np.pi / 3.0, 2.0 / 3.0)) * math.pow(10, 2.0 / 3.0)
vtmp = 0.1
asymp_cv_high = (
    1.5 - 3 * math.pow(np.pi, 1.5) / 8.0 / np.power(temps_cv_high, 1.5) / 2.0 / vtmp
)
asymp_cp_high = (
    1.5
    - 3 * math.pow(np.pi, 1.5) / 8.0 / np.power(temps_cp_high, 1.5) / 2.0 / vtmp
    + np.square(4.0 * np.power(temps_cp_high, 1.5) * 2 * vtmp - math.pow(np.pi, 1.5))
    / 16.0
    / np.power(temps_cp_high, 1.5)
    / 2.0
    / vtmp
    / (np.power(temps_cp_high, 1.5) * 2.0 * vtmp + np.power(np.pi, 1.5))
)


vols = [0.1, 1, 10]
t = IfgCalculator(
    volumes=vols, temperatures=temps, input_in_si=False, output_in_si=False
)

plt.plot(temps, t.C_V[:, 0], "k-", linewidth=2, label=r"{$C_V$: $v = 0.1$}")
plt.plot(temps, t.C_V[:, 1], "k--", linewidth=2, label=r"{$C_V$: $v = 1$}")
plt.plot(temps, t.C_V[:, 2], "k-.", linewidth=2, label=r"{$C_V$: $v = 10$}")
plt.plot(temps, t.C_P[:, 0], "r-", linewidth=2, label=r"{$C_P$: $v = 0.1$}")
plt.plot(temps, t.C_P[:, 1], "r--", linewidth=2, label=r"{$C_P$: $v = 1$}")
plt.plot(temps, t.C_P[:, 2], "r-.", linewidth=2, label=r"{$C_P$: $v = 10$}")
plt.plot(temps1, asymp1, "b-", linewidth=1, label=r"$C_V$: low-$T$ asymp.")
plt.plot(
    temps_cp_high,
    asymp_cp_high,
    "-",
    color="tab:orange",
    linewidth=1,
    label=r"$C_V$: high-$T$ asymp.",
)
plt.plot(
    temps_cv_high, asymp_cv_high, "m-", linewidth=1, label=r"$C_P$: high-$T$ asymp."
)
plt.text(200, 1.6, r"$C_V = 3/2$")
plt.text(200, 2.7, r"$C_P = 5/2$")
plt.text(2.5, 5.72, r"$C_V = \beta v^{2/3} T$")

plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"{\LARGE $T$, Ha}")
plt.ylabel(r"{\LARGE $C_V$, $C_P$}, atomic units")
plt.xlim(1e-2, 5e3)
plt.ylim(1e-1, 10)
plt.legend(loc="lower right")
plt.savefig("cv_cp.pdf", bbox_inches="tight")
plt.show()
