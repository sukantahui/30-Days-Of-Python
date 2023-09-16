"""
Compute neutron scattering XS for rare earth isotopes.

Lynn, J.E., Seeger, P.A., 1990.
*Resonance effects in neutron scattering lengths of rare-earth nuclides.*
Atomic Data and Nuclear Data Tables 44, 191–207.
https://doi.org/10.1016/0092-640X(90)90013-A
"""
import numpy as np

import periodictable as pt

class RareEarthIsotope:
    def __init__(
        self, isotope, E0, E_lambda, gamma_lambda_sq, Gamma_lambda,
        A=0j, B=0j, C=0j, Delta_E=0, a=None):
        r"""
        *isotope* is the isotope of interest (e.g., Sm[149])

        *E0* is the chosen pivot energy of the fit $E_0$ (eV)

        *E_lambda* is the formal compound nucleus energy level $E_\lambda$ (eV).

        *gamma_lambda_sq* is the reduced neutron width amplitude
        $\gamma_{\lambda(n)}$ (eV).

        *a* is the atomic radius, estimated as $1.16 A^{1/3} + 0.6$ fm if
        not provided, where $A$ is the atomic mass of the isotope.

        *Gamma_lambda* is the absorption width $\Gamma_{\lambda(a)}$ (eV).

        *Delta_E* is the level shift $\Delta_E$ (eV) that can "usually be
        neglected at the very low neutron energies considered in this paper".

        *A*, *B*, *C* are the fitted real + imaginary constants for the isotope,
        with units 1/eV for B and 1/eV^2 for C.
        """
        self.isotope = isotope
        # Eq. 13: a is the nuclear radius
        self.a = a if a is not None else 1.16*np.cbrt(isotope.mass) + 0.6  # fm
        #print(f"a={self.a}")
        self.E0 = E0
        self.E_lambda = E_lambda
        self.Delta_E = Delta_E
        self.gamma_lambda_sq = gamma_lambda_sq
        self.Gamma_lambda = Gamma_lambda
        self.A, self.B, self.C = A, B, C

    def f(self, E):
        # Eq. 11 & 12
        dE = E - self.E0
        Rex = self.A.real + (self.B.real + self.C.real*dE)*dE
        Sex = self.A.imag + (self.B.imag + self.C.imag*dE)*dE
        # Eq. 1.5
        k = 0.0021968*np.sqrt(E)
        # Eq. 10 is shuffled a bit to allow the following substitutions
        aRt = self.a*(1 - Rex)
        aSt = self.a*Sex
        Et = self.E_lambda - E + self.Delta_E
        Gt = self.Gamma_lambda/2
        agsq = self.a*self.gamma_lambda_sq
        # Eq. 10
        fr = (2*k*aSt-1)*aRt + agsq*(Et + (2*k*Gt)*aRt)/(Et**2 + Gt**2)
        fi = aSt + k*(aRt**2 - aSt**2) + agsq*(Gt - 2*k*Et*aRt)/(Et**2 + Gt**2)
        return fr, fi

    def __str__(self):
        return str(self.isotope)

Sm_nat = RareEarthIsotope(
    pt.Sm, E0=0.025, E_lambda=0.0973,
    gamma_lambda_sq=0.573, Gamma_lambda=0.0656,
    A=0+0.13j, B=0.75+0.j, C=0.441+0.j)

Gd_155 = RareEarthIsotope(
    pt.Gd[155], E0=0.025, E_lambda=0.0281,
    gamma_lambda_sq=0.208, a=6.831, Gamma_lambda=0.105)

Gd_157 = RareEarthIsotope(
    pt.Gd[157], E0=0.025, E_lambda=0.0312,
    gamma_lambda_sq=0.885, a=6.858, Gamma_lambda=0.105,
    A=0.089j)

Dy_164 = RareEarthIsotope(
    pt.Dy[164], E0=None, E_lambda=-3.025,
    gamma_lambda_sq=18.5, a=6.949, Gamma_lambda=None,
)

#Lu_176 = RareEarthIsotope(
#    pt.Lu[176], E0=None, E_lambda=0.1413,
#    gamma_lambda_sq=0.07913, 
#)

def demo():
    from itertools import cycle
    import matplotlib.pyplot as plt
    from . import nsf

    E = np.logspace(-3, 0, 400)
    L = nsf.neutron_wavelength(1000*E)

    isos = Sm_nat, Gd_155, Gd_157
    #isos =

    colors = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    for iso in isos:
        c = next(colors)
        fr, fi = iso.f(E)
        plt.semilogx(L, fr, '-', c=c, label=f"{iso}")
        plt.semilogx(L, fi, '--', c=c, label=None)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    demo()
