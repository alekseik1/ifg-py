import matplotlib.pyplot as plt
import numpy as np

from ifg import IfgCalculator

# temps = np.logspace(-2, 4, num=100)
thetas = np.linspace(0.5, 10.0, 1000)
vols = [0.1, 1, 100]
t = (
    IfgCalculator()
    .with_volumes(vols, in_si=False)
    .with_theta(thetas)
    .with_output_in_si(False)
)
asymp = np.ones_like(thetas) * 5 / 3

plt.plot(thetas, t.C_P[:, 0] / t.C_V[:, 0], "k-", label=r"$v = 0.1$")
# NOTE: does not depend on volume
# plt.plot(thetas, t.C_P[:, 0] / t.C_V[:, 1], "k--", label=r"$v = 1$")
# plt.plot(thetas, t.C_P[:, 0] / t.C_V[:, 2], "k-.", label=r"$v = 10$")
plt.plot(thetas, asymp, "r--", label=r"High-$T$ asymp.")

plt.xscale("log")
plt.xlabel(r"$T$, Ha")
plt.ylabel(r"$C_P / C_V$")
# plt.xlim(1e-2, 1e4)
# plt.ylim(0, 2)
plt.legend()
plt.text(200, 1.7, r"$C_P/C_V = 5/3$")
plt.savefig("cp_by_cv.pdf", bbox_inches="tight")
plt.show()
