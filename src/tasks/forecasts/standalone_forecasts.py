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
                Family(tag='ifs', ticket=t, on_error='delayed_fail', nodes=[
                    Family(tag='global21', ticket=t, nodes=[
                        StandaloneIFSForecast(tag='forecast-ifs-global21', ticket=t, **kw),
                        ], **kw),
                    ], **kw),
                Family(tag='arpege', ticket=t, on_error='delayed_fail', nodes=[
                    Family(tag='globaltst149c24', ticket=t, nodes=[
                        StandaloneArpegeForecast(tag='forecast-arpege-globaltst149c24', ticket=t, **kw),
                        ], **kw),
                    ], **kw),
                Family(tag='arome', ticket=t, on_error='delayed_fail', nodes=[
                    Family(tag='corsica2500', ticket=t, nodes=[
                        StandaloneAromeForecast(tag='forecast-arome-corsica2500', ticket=t, **kw),
                        ], **kw),
                    ], **kw),
               Family(tag='alaro', ticket=t, on_error='delayed_fail', nodes=[
                    Family(tag='antwrp1300', ticket=t, nodes=[
                        StandaloneAlaroForecast(tag='forecast-alaro-antwrp1300', ticket=t, **kw),
                        ], **kw),
                    Family(tag='cz2300', ticket=t, nodes=[
                        StandaloneAlaroForecast(tag='forecast-alaro-cz2300', ticket=t, **kw),
                        ], **kw),
                    ], **kw),
                ], **kw),
        ],
    )

