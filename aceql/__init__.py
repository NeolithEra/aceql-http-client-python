#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2017,  KawanSoft SAS
# (http://www.kawansoft.com). All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

"""aceql library. Allows to wrap the AceQL HTTP APIs to access remote SQL databases.

    The library supports Python 2.6 to 2.7 and 3.4 to 3.7.
    It provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
"""

from aceql.connection import *
from aceql.progress_indicator import *
from aceql.sql_null_type import *
from aceql.cursor import *
from aceql.error import *
from aceql.proxy_auth import *
from aceql.proxy_util import *

from aceql.dbapi2 import *

__all__ = ["Connection", "Cursor", "Error", "ProgressIndicator", "ProxyUtil", "ProxyAuth", "SqlNullType"]


def connect(server_url, database, username, password, proxies=None, auth=None):
    """
    Creates a database connection to the remote AceQL HTTP server.

    Parameters
    ----------
    server_url : str
        The URL of the AceQL server. Example: https://www.acme.com:9443/aceql.
    database : str
        The remote database name.
    username : str
        The authentication username.
    password : str
        the authentication password.
    proxies : dict
        The proxy to use, can  be an authenticated proxy.
    auth:   : ProxyAuth
        aceql.ProxyAuth instance with proxy (username, password)

    Returns
    -------
    Connection
        A connection to the remote database.

    """

    the_connection = Connection(server_url, database, username, password, proxies=proxies, auth=auth)
    return the_connection
