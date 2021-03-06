#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer - The distributed application framework
# ==============================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from isomer.schemata.extends import DefaultExtension

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""
Schema: Taskgrid
=================

Contains
--------

Taskgrid: Taskgrid config to store gridster settings


"""

from isomer.schemata.defaultform import *
from isomer.schemata.base import base_object, uuid_object

TaskGridConfigSchema = base_object('taskgridconfig', all_roles='crew')

TaskGridConfigSchema['properties'].update({
    'locked': {
        'type': 'boolean', 'title': 'Locked Taskgrid',
        'description': 'Determines whether the Taskgrid should '
                       'be locked against changes.'
    },
    'shared': {
        'type': 'boolean', 'title': 'Shared Taskgrid',
        'description': 'Share Taskgrid with the crew'
    },
    'description': {
        'type': 'string', 'format': 'html',
        'title': 'Taskgrid description',
        'description': 'Taskgrid description'
    },
    'cards': {
        'type': 'array',
        'default': [],
        'items': {
            'type': 'object',
            'id': '#Card',
            'name': 'TaskGridCard',
            'properties': {
                'taskgroup': uuid_object('Associated Unique Task Group ID'),
                'position': {
                    'type': 'object',
                    'properties': {
                        'x': {'type': 'number'},
                        'y': {'type': 'number'}
                    }
                },
                'size': {
                    'type': 'object',
                    'properties': {
                        'width': {'type': 'number'},
                        'height': {'type': 'number'}
                    }
                },
            }
        }
    }
})

TaskGridConfigForm = [
    {
        'type': 'section',
        'htmlClass': 'row',
        'items': [
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'name'
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'shared', 'locked'
                ]
            },
        ]
    },
    {
        'key': 'cards',
        'add': "Add Task Group",
        'startEmpty': True,
        'style': {
            'add': "btn-success"
        },
        'items': [
            {
                'key': 'cards[].taskgroup',
                'type': 'strapselect',
                'placeholder': 'Select a Task Group',
                'options': {
                    "type": "taskgroup",
                    "asyncCallback": "$ctrl.getFormData",
                    "map": {
                        'valueProperty': "uuid",
                        'nameProperty': 'name'
                    }
                }
            }
        ]
    },
    'description',
    editbuttons
]

TaskGridConfigExtends = DefaultExtension(
    {'taskgriduuid': uuid_object('Default Taskgrid')},
    lookup_field('modules.taskgriduuid', 'taskgridconfig')
)

TaskGridConfig = {'schema': TaskGridConfigSchema, 'form': TaskGridConfigForm, 'extends': TaskGridConfigExtends}
