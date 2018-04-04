#!/usr/bin/python

from distutils.core import setup
import os
import os.path as osp
import pathlib
import sys

import py2app  # NOQA


base_dir = str(pathlib.Path(os.getcwd()).parent)
sys.argv.append('py2app')
setup(
    app=['labelme_app.py'],
    options=dict(
        py2app=dict(
            argv_emulation=True,
            iconfile='labelme/icons/icon.icns',
            bdist_base=osp.join(base_dir, 'build'),
            dist_dir=osp.join(base_dir, 'dist'),
        ),
    ),
)
