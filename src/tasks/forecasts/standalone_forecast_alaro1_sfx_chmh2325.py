# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, unicode_literals, division

from footprints import FPDict

import vortex
from vortex import toolbox
from vortex.layout.nodes import Task, Family, Driver, LoopFamily
from common.util.hooks import update_namelist
import davai

from .standalone.ifs import StandaloneIFSForecast
from .standalone.arpege import StandaloneArpegeForecast
from .standalone.arome import StandaloneAromeForecast
from .standalone.alaro import StandaloneAlaroForecast


def setup(t, **kw):
    return Driver(tag='drv', ticket=t, options=kw, nodes=[
        LoopFamily(tag='gmkpack', ticket=t,
            loopconf='compilation_flavours',
            loopsuffix='.{}',
            nodes=[
                Family(tag='alaro', ticket=t, on_error='delayed_fail', nodes=[
                    # FIXME 49T2:
                    #Family(tag='chmh2325', ticket=t, nodes=[
                    #    StandaloneAlaroForecast(tag='forecast-alaro1_sfx-chmh2325', ticket=t, **kw),
                    #    ], **kw),
                    ], **kw),
                ], **kw),
        ],
    )

