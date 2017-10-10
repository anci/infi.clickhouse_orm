#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


if __name__ == '__main__':
    SETUP_INFO = dict(
        name='infi.clickhouse_orm',
        version='0.9.7.2',
        install_requires=[
            'pytz',
	        'requests',
	        'setuptools',
	        'six'
	    ],
        namespace_packages=['infi'],
        package_dir={'': 'src'},
        #package_data={'': []},
        include_package_data=True,
        zip_safe=False,
        entry_points = dict(
            console_scripts=[],
            gui_scripts=[],
        ),
    )
    SETUP_INFO['packages'] = find_packages('src')
    setup(**SETUP_INFO)
