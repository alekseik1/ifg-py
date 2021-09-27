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
vols = [0.1, 1, 10]
t = IfgCalculator(
    temperatures=temps, volumes=vols, input_in_si=False, output_in_si=False
)
asymp = np.zeros(len(temps))
asymp.fill(5.0 / 3.0)

plt.plot(temps, t.C_P[:, 0] / t.C_V[:, 0], "k-", label=r"$v = 0.1$")
plt.plot(temps, t.C_P[:, 0] / t.C_V[:, 1], "k--", label=r"$v = 1$")
plt.plot(temps, t.C_P[:, 0] / t.C_V[:, 2], "k-.", label=r"$v = 10$")
plt.plot(temps, asymp, "r--", label=r"High-$T$ asymp.")

plt.xscale("log")
plt.xlabel(r"\LARGE $T$, Ha")
plt.ylabel(r"\LARGE $C_P / C_V$")
plt.xlim(1e-2, 1e4)
plt.ylim(0, 2)
plt.legend()
plt.text(200, 1.7, r"$C_P/C_V = 5/3$")
plt.savefig("cp_by_cv.pdf", bbox_inches="tight")
plt.show()
