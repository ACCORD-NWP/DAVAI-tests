# -*- coding: utf-8 -*-
"""
Canonical Forecasts: with the components they usually embark in operational context
(e.g. inline Fullpos, DDH, sometimes IAU...)
"""
from __future__ import print_function, absolute_import, unicode_literals, division

import vortex
from vortex import toolbox
from vortex.layout.nodes import Driver, Family, LoopFamily

from tasks.surfex.pgd import PGD
from tasks.surfex.prep import Prep
from .canonical.arpege import CanonicalArpegeForecast


def setup(t, **kw):
    return Driver(tag='drv', ticket=t, options=kw, nodes=[
        Family(tag='arpege', ticket=t, on_error='delayed_fail', nodes=[
            Family(tag='global798c22', ticket=t, nodes=[
                CanonicalArpegeForecast(tag='forecast-arpege-global798c22', ticket=t, **kw),
                ], **kw),
            ], **kw),
        #Family(tag='arome', ticket=t, on_error='delayed_fail', nodes=[
        #    Forecast(tag='arome_canonical_forecast', ticket=t, **kw),
        #    ], **kw),
        ],
    )

