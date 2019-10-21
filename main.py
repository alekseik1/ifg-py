from scipy.constants import electron_mass, hbar, pi, k, N_A
import matplotlib.pyplot as plt
from scipy.special import gamma
from fdint import fdk, ifd1h
import numpy as np
import pandas as pd


class PropertiesCalculator:

    def __init__(self):
        super().__init__()
        self.result = pd.DataFrame(columns=['n', 'T', 'mu', 'E/V'], dtype=np.float)

    def calculate_for(self, n_array, T_array, g=2, m=electron_mass):
        for n in n_array:
            for T in T_array:
                # T в Кельвинах
                T *= k
                F_right = n*(np.sqrt(2)*pi**2*hbar**3/(g*m**(3/2)))/(T**(3/2)*gamma(3/2))
                mu_div_T = ifd1h(F_right)
                mu = mu_div_T*T
                E_div_V = g*m**(3/2)/(np.sqrt(2) * pi**2 * hbar**3) * T**(5/2)*gamma(5/2)*fdk(k=1.5, phi=mu/T)
                self.result = self.result.append({'n': n, 'T': T/k, 'mu': mu, 'E/V': E_div_V}, ignore_index=True)
        return self.result

    def _get_E_div_V_asymp(self, n):
        return 3/2*self._get_P_asymp(n)

    def _get_P_asymp(self, n):
        return (3 * pi ** 2) ** (2 / 3) / 5 * hbar ** 2 / electron_mass * n ** (5 / 3)

    def _get_mu_asymp(self, n):
        return (3*pi**2)**(2/3)*hbar**2/(2*electron_mass)*n**(2/3)

    def get_asymp_for(self, n_array):
        return pd.DataFrame([{
            'n': n,
            'mu': self._get_mu_asymp(n),
            'E/V': self._get_E_div_V_asymp(n)
        } for n in n_array])


def rho_to_n(rho, molar_mass, free_electrons):
    """
    :param rho: в г/см^3
    :param molar_mass: в г/моль
    :return:
    """
    return rho/molar_mass*10**6*N_A*free_electrons


if __name__ == '__main__':
    n_array = np.array([
        # Алюминий
        rho_to_n(rho=2.7, molar_mass=27, free_electrons=3),
        # Медь
        rho_to_n(rho=8.92, molar_mass=63.5, free_electrons=2),
    ])
    T_array = np.array([10**i for i in range(-5, 5)])
    calculator = PropertiesCalculator()
    result_df = calculator.calculate_for(n_array, T_array)
    asymp_df = calculator.get_asymp_for(n_array)


    def plot_data(x_data, y_data, xlabel, ylabel, title):
        plt.scatter(x_data, y_data)
        plt.title(title)
        plt.grid()
        plt.ylim(min(y_data), max(y_data))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    data = result_df[result_df['n'] == result_df['n'][0]]
    plot_data(x_data=data['T'], y_data=data['mu'], xlabel='T', ylabel='$\mu$', title='$\mu(T)$')
    plot_data(x_data=data['T'], y_data=data['E/V'], xlabel='T', ylabel='$E/V$', title='$(E/V)(T)$')
