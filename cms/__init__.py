#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Programming contest management system
# Copyright © 2010-2013 Giovanni Mascellani <mascellani@poisson.phc.unipi.it>
# Copyright © 2010-2012 Stefano Maggiolo <s.maggiolo@gmail.com>
# Copyright © 2010-2012 Matteo Boscariol <boscarim@hotmail.com>
# Copyright © 2013 Luca Wehrstedt <luca.wehrstedt@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

# As this package initialization code is run by all code that imports
# something in cms.* it's the best place to setup the logging handlers.
# By importing the log module we install a handler on stdout. Other
# handlers will be added by services by calling initialize_logging.
import cms.log


# Define what this package will provide.

__all__ = [
    "LANG_C", "LANG_CPP", "LANG_PASCAL", "LANG_PYTHON", "LANG_PHP", "LANG_HASKELL", "LANG_PERL",
    "LANGUAGE_NAMES", "LANGUAGES", "DEFAULT_LANGUAGES",
    "SOURCE_EXT_TO_LANGUAGE_MAP",
    "LANGUAGE_TO_SOURCE_EXT_MAP", "LANGUAGE_TO_HEADER_EXT_MAP",
    # log
    # Nothing intended for external use, no need to advertise anything.
    # util
    "mkdir", "Address", "ServiceCoord", "get_service_address",
    "get_shard_from_addresses", "get_service_shards",
    "default_argument_parser", "find_local_addresses",
    # conf
    "config",
    # plugin
    "plugin_list", "plugin_lookup",
    ]


# Instantiate or import these objects.

# Shorthand codes for all supported languages.
LANG_C = "c"
LANG_CPP = "cpp"
LANG_PASCAL = "pas"
LANG_PYTHON = "py"
LANG_PHP = "php"
LANG_JAVA = "java"
LANG_HASKELL = "hs"
LANG_PERL = "pl"

LANGUAGE_NAMES = {
    LANG_C: "C",
    LANG_CPP: "C++",
    LANG_PASCAL: "Pascal",
    LANG_PYTHON: "Python",
    LANG_PHP: "PHP",
    LANG_JAVA: "Java",
	LANG_HASKELL: "Haskell",
	LANG_PERL: "Perl",
}

LANGUAGES = [LANG_C, LANG_CPP, LANG_PASCAL, LANG_PYTHON, LANG_PHP, LANG_JAVA, LANG_HASKELL, LANG_PERL]
DEFAULT_LANGUAGES = [LANG_C, LANG_CPP, LANG_PASCAL, LANG_PYTHON, LANG_PHP, LANG_JAVA, LANG_HASKELL, LANG_PERL]

# A reference for extension-based automatic language detection.
# (It's more difficult with headers because ".h" is ambiguous.)
SOURCE_EXT_TO_LANGUAGE_MAP = {
    ".c": LANG_C,
    ".cpp": LANG_CPP,
    ".cxx": LANG_CPP,
    ".cc": LANG_CPP,
    ".C": LANG_CPP,
    ".c++": LANG_CPP,
    ".pas": LANG_PASCAL,
    ".py": LANG_PYTHON,
    ".php": LANG_PHP,
    ".java": LANG_JAVA,
	".hs": LANG_HASKELL,
	".pl": LANG_PERL,
}

# Our preferred source file and header file extension for each language.
LANGUAGE_TO_SOURCE_EXT_MAP = {
    LANG_C: ".c",
    LANG_CPP: ".cpp",
    LANG_PASCAL: ".pas",
    LANG_PYTHON: ".py",
    LANG_PHP: ".php",
    LANG_JAVA: ".java",
	LANG_HASKELL: ".hs",
	LANG_PERL: ".pl",
}
LANGUAGE_TO_HEADER_EXT_MAP = {
    LANG_C: ".h",
    LANG_CPP: ".h",
    LANG_PASCAL: "lib.pas",
    LANG_PYTHON: ".py",
    LANG_PHP: ".php",
    LANG_JAVA: ".java",
	LANG_HASKELL: ".hs",
	LANG_PERL: ".pl",
}

from .util import mkdir, Address, ServiceCoord, get_service_address, \
    get_shard_from_addresses, get_service_shards, \
    default_argument_parser, find_local_addresses
from .conf import config
from .plugin import plugin_list, plugin_lookup
