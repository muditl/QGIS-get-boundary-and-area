# -*- coding: utf-8 -*-
"""
/***************************************************************************
 get_boundary_and_area
                                 A QGIS plugin
 This plugin is used to get the information about the area of the shape file. It gets area, boundary box and perimeter
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-04-19
        copyright            : (C) 2023 by Map Makers
        email                : muditlodha@jklu.edu.in
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load get_boundary_and_area class from file get_boundary_and_area.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .get_boundary_and_area import get_boundary_and_area
    return get_boundary_and_area(iface)
