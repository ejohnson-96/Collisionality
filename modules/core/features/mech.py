import numpy as np

from modules.core.vars.num_man import valid_num, positive, dim, valid_vec

c = 299792458
g = -1 * 9.81


def rel_check(
        v,
        limit=0.1,
):
    valid_num(v)
    limit = dim(limit, 0, 1)
    if (v / c) > limit:
        raise ValueError(
            f"Argument {v} is to large and will cause relativistic "
            f"effects. Ratio of {v / c} is given and a ratio of less"
            f" than {limit} is required."
        )
    else:
        return v


def vat(
        a,
        t,
        v0=0,
):
    valid_num(a, v0)
    v0 = rel_check(v0)
    positive(t)
    return a * t + v0


def rat(
        t,
        a=g,
        r0=0,
        v0=0,
):
    valid_num(a, r0, v0)
    positive(t)
    rel_check(v0)
    return r0 + v0 * t + 0.5 * a * (t ** 2)


def rvt(
        v,
        t,
        r0=0,
        v0=0,
):
    valid_num(v, r0, v0)
    positive(t)
    rel_check(v)
    return r0 + 0.5 * (v + v0) * t


def var(
        a,
        r,
        r0=0,
        v0=0,
):
    valid_num(a, r, r0, v0)
    rel_check(v0)
    return np.sqrt(v0 ** 2 + 2 * a * (r - r0))


def rvta(
        v,
        t,
        a=g,
        r0=0,
):
    valid_num(v, t, a, r0)
    positive(t)
    v = rel_check(v)
    return r0 + v * t - 0.5 * a * (t ** 2)


def frict(
        mu,
        N,
):
    valid_num(mu, N)
    return mu * N


def momentum(
        m,
        v,
):
    valid_num(m, v)
    v = rel_check(v)
    return m * v


def ke(
        m,
        v,
):
    valid_num(m, v)
    v = rel_check(v)
    return 0.5 * m * v ** 2


def gpe(
        m,
        y,
        y0=0,
        a=g,
):
    valid_num(m, y, y0, a)
    return m * a * (y - y0)


def oat(
        alpha,
        t,
        omega0=0,
):
    valid_num(alpha, omega0)
    positive(t)
    return omega0 + alpha * t


def pta(
        t,
        alpha,
        omega0=0,
        phi0=0,
):
    valid_num(alpha, omega0, phi0)
    positive(t)
    return phi0 + omega0 * t + 0.5 * alpha * (t ** 2)


def pot(
        omega,
        t,
        phi0=0,
        omega0=0,
):
    valid_num(omega, phi0, omega0)
    positive(t)
    return phi0 + 0.5 * (omega0 + omega) * t


def oap(
        alpha,
        phi,
        phi0=0,
        omega0=0,
):
    valid_num(alpha, phi, phi0, omega0)
    return np.sqrt(omega0 ** 2 + 2 * alpha * (phi - phi0))


def pota(
        omega,
        t,
        alpha,
        phi0=0,
):
    valid_num(omega, alpha, phi0)
    positive(t)
    return phi0 + omega * t + 0.5 * alpha * (t ** 2)


def lin_3d(
        a,
        t,
        v0=None,
):
    dim = valid_vec(a, dimension=True)
    positive(t)

    if v0 is None:
        if dim == 1:
            v0 = 0
        else:
            v0 = np.zeros(dim)
    else:
        if valid_vec(v0, dimension=True) != dim:
            raise ValueError(
                f"Argument {v0} is of incorrect dimension, dimension "
                f"of {dim} is required. Please try again."
            )

    if dim == 1:
        return vat(a, t, v0)
    else:
        res = np.zeros(dim)
        for i in range(dim):
            res[i] = vat(a[i], t, v0[i])

        return res


t = 10
a = [1,2]


z = lin_3d(a, t,)

print(z)