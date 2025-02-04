"""
Copyright 2018 Grid Singularity
This file is part of Grid Singularity Exchange.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import unittest

from gsy_e.gsy_e_core.util import IntervalType
from gsy_e.gsy_e_core.util import d3a_path
from gsy_framework.constants_limits import ConstSettings
from gsy_e.gsy_e_core.util import read_settings_from_file
from gsy_e.gsy_e_core.util import update_advanced_settings
from gsy_e.models.config import SimulationConfig


class SampleTest(unittest.TestCase):
    def test_parse_settings_file(self):
        simulation_settings, advanced_settings = read_settings_from_file(
            os.path.join(d3a_path, "setup", "gsy_e_settings.json"))
        update_advanced_settings(advanced_settings)
        simulation_config = SimulationConfig(**simulation_settings)

        assert simulation_config.__getattribute__("sim_duration") == IntervalType('H:M')("24h")
        try:
            for setting in advanced_settings.keys():
                getattr(ConstSettings, setting)
        except AttributeError:
            self.fail("The settings file is not consistent with the selection of variables in "
                      "const.py")
