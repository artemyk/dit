"""
Tests for dit.pid.immi.
"""

import pytest

from dit.pid.immi import PID_MMI
from dit.pid.distributions import bivariates, trivariates


def test_pid_mmi1():
    """
    Test immi on a generic distribution.
    """
    d = bivariates['prob. 1']
    pid = PID_MMI(d, ((0,), (1,)), (2,))
    assert pid[((0,), (1,))] == pytest.approx(0.019973094021974794)
    assert pid[((0,),)] == pytest.approx(0.15097750043269376)
    assert pid[((1,),)] == pytest.approx(0.0)
    assert pid[((0, 1),)] == pytest.approx(0.0)


def test_pid_mmi2():
    """
    Test immi on another generic distribution.
    """
    d = trivariates['sum']
    pid = PID_MMI(d, [[0], [1], [2]], [3])
    for atom in pid._lattice:
        if atom == ((0,), (1,), (2,)):
            assert pid[atom] == pytest.approx(0.31127812445913294)
        elif atom == ((0, 1), (0, 2), (1, 2)):
            assert pid[atom] == pytest.approx(0.5)
        elif atom == ((0, 1, 2),):
            assert pid[atom] == pytest.approx(1.0)
        else:
            assert pid[atom] == pytest.approx(0.0)
