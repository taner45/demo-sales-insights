# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""
A page of the application.
Page content is imported from the Predictions.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown, notify
import pandas as pd


dn_holiday = None
dn_result = None

selected_scenario = None
selected_holiday = None
selected_level = 100


def on_submission_change(state, submitable, details):
    if details["submission_status"] == "COMPLETED":
        state.dn_result = state.selected_scenario.result
        notify(state, "success", "Predictions ready!")
        print("Predictions ready!")


def on_change_params(state):
    holiday = pd.read_csv(state.selected_holiday) if state.selected_holiday else None
    state.selected_scenario.level.write(state.selected_level / 100)
    state.selected_scenario.holiday.write(holiday)
    state.dn_holiday = state.selected_scenario.holiday
    notify(state, "success", "Scenario parameters changed!")

    state.refresh("selected_scenario")


def on_change(state, var_name, var_value):
    if var_name == "selected_scenario" and var_value:
        state.selected_level = state.selected_scenario.level.read() * 100
        state.dn_holiday = state.selected_scenario.holiday
        state.dn_result = state.selected_scenario.result


Predictions = Markdown("pages/Predictions/Predictions.md")
