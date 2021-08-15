# Malaya-Graph, Knowledge Graph Toolkit for Bahasa Malaysia
#
# Copyright (C) 2021 Malaya Project
# Licensed under the MIT License
# Author: huseinzol05 <husein.zol05@gmail.com>
# URL: <https://malaya-graph.readthedocs.io/>
# For license information, see https://github.com/huseinzol05/malaya-graph/blob/master/LICENSE

from malaya_boilerplate.utils import get_home

version = '0.1'
bump_version = '0.1'
__version__ = bump_version

package = 'malaya-graph'
url = 'https://f000.backblazeb2.com/file/malaya-graph-model/'

__home__, _ = get_home(package=package, package_version=version)
