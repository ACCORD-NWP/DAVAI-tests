# -*- coding: utf-8 -*-
"""
PP_geo = PGD+Prep on a range of LAM geometries
"""
from __future__ import print_function, absolute_import, unicode_literals, division

import vortex
from vortex import toolbox
from vortex.layout.nodes import Driver, Family, LoopFamily

from tasks.surfex.pgd import PGD
from tasks.surfex.prep import Prep


def setup(t, **kw):
    return Driver(tag='drv', ticket=t, options=kw, nodes=[
        Family(tag='arome', ticket=t, nodes=[
            Family(tag='arome_physiography', ticket=t, nodes=[
                LoopFamily(tag='lam_geometries', ticket=t,
                    loopconf='geometrys',
                    loopsuffix='-{0.tag}',
                    nodes=[PGD(tag='pgd-arome', ticket=t, **kw),
                           Prep(tag='prep-arome', ticket=t, **kw),
                    ], **kw),
                ], **kw),
            ], **kw),
        Family(tag='arpege', ticket=t, nodes=[
            Family(tag='arpege_physiography', ticket=t, nodes=[
                LoopFamily(tag='gauss_grids', ticket=t,
                    loopconf='geometrys',
                    loopsuffix='-{0.tag}',
                    nodes=[PGD(tag='pgd-arpege', ticket=t, **kw),
                           Prep(tag='prep-arpege', ticket=t, **kw),
                    ], **kw),
                ], **kw),
            ], **kw),
        ],
    )

