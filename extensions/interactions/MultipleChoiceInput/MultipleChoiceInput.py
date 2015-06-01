# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from extensions.answer_summarizers import calculations
from extensions.interactions import base


class MultipleChoiceInput(base.BaseInteraction):
    """Interaction for multiple choice input."""

    name = 'Multiple Choice'
    description = (
        'Allows learners to select one of a list of multiple-choice options.')
    display_mode = base.DISPLAY_MODE_INLINE
    _dependency_ids = []
    _handlers = [{
        'name': 'submit', 'obj_type': 'NonnegativeInt'
    }]

    _customization_arg_specs = [{
        'name': 'choices',
        'description': 'Multiple Choice options',
        'schema': {
            'type': 'list',
            'validators': [{
                'id': 'has_length_at_least',
                'min_value': 1,
            }],
            'items': {
                'type': 'html',
                'ui_config': {
                    'hide_complex_extensions': True,
                },
            },
            'ui_config': {
                'add_element_text': 'Add multiple choice option',
            }
        },
        'default_value': ['Sample multiple-choice answer'],
    }]

    # Registered answer visualizations. 'data_source' entries will
    # be used to determine which calculations need to be done.
    answer_visualizations = []

    # Bar chart with answer counts.
    answer_visualizations.append(
        {'visualization_id': 'BarChart',
         'visualization_customization_args': {
             'x_axis_label': 'Answer',
             'y_axis_label': 'Count',
             },
         'data_source': {
              'calculation_id': calculations.AnswerCounts.calculation_id,
              }})

    # Table with answer counts.
    answer_visualizations.append(
        {'visualization_id': 'Table',
         'visualization_customization_args': {
             'column_labels': ['Answer', 'Count'],
             },
         'data_source': {
              'calculation_id': calculations.AnswerCounts.calculation_id,
              }})
