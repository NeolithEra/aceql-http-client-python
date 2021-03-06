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

from aceql.cursor import *


class Connection(object):
    """Allows to create a database connection to a remote server."""

    def __init__(self, server_url, database, username, password, proxies=None, auth=None):
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
        proxies : str
            The proxy to use, can  be an authenticated proxy.
        auth:   : ProxyAuth
            aceql.ProxyAuth instance with proxy (username, password)

        Returns
        -------
        Connection
            A connection to the remote database.

        """

        if server_url is None:
            raise TypeError("server_url is null!")
        if database is None:
            raise TypeError("database is null!")
        if username is None:
            raise TypeError("username is null!")
        if password is None:
            raise TypeError("password is null!")

        self.__aceQLHttpApi = AceQLHttpApi(server_url, database, username, password, proxies=proxies, auth=auth)

    def cursor(self):
        """Instantiates and returns a cursor."""
        cursor = Cursor(self, self.__aceQLHttpApi)
        return cursor

    def is_stateless():
        """Says if session is stateless."""
        return AceQLHttpApi.is_stateless()

    is_stateless = staticmethod(is_stateless)

    def set_stateless(stateless):
        """Sets the session mode. if true, the session will be stateless, else stateful."""
        if stateless is None:
            raise TypeError("stateless is null!")
        if str(stateless) == "True":
            AceQLHttpApi.set_stateless(True)
        else:
            AceQLHttpApi.set_stateless(False)

    set_stateless = staticmethod(set_stateless)

    def set_timeout(timeout):
        """ Sets the HTTP connection timeout in seconds.
        0 means not timeout is used (default value)."""

        if timeout is None:
            raise TypeError("timeout is null!")

        AceQLHttpApi.set_timeout(timeout)

    set_timeout = staticmethod(set_timeout)

    def set_progress_indicator(self, progress_indicator):
        """ Allows to set a progress indicator."""
        self.__aceQLHttpApi.set_progress_indicator(progress_indicator)

    def get_progress_indicator(self):
        """Returns the progress indicator in use."""
        return self.__aceQLHttpApi.get_progress_indicator()

    def set_auto_commit(self, auto_commit):
        """Sets this connection's auto-commit mode to the given state."""
        self.__aceQLHttpApi.set_auto_commit(auto_commit)

    def get_auto_commit(self):
        """Retrieves the current auto-commit mode."""
        return self.__aceQLHttpApi.get_auto_commit()

    def commit(self):
        """Commit current transaction."""
        self.__aceQLHttpApi.commit()

    def rollback(self):
        """Rollback current transaction."""
        self.__aceQLHttpApi.rollback()

    def _trace(self):
        """Print empty line on trace."""
        self.__aceQLHttpApi.trace()

    def trace(self, s):
        """Prints the string on trace."""
        self.__aceQLHttpApi.trace(s)

    def _is_trace_on():
        """Says if trace is on."""
        return AceQLHttpApi.is_trace_on()

    _is_trace_on = staticmethod(_is_trace_on)

    def _set_trace_on(trace_on):
        """Sets the trace on/off."""
        AceQLHttpApi.set_trace_on(trace_on)

    _set_trace_on = staticmethod(_set_trace_on)

    def is_gzip_result(self):
        """Says if the query result is returned compressed with the GZIP file format."""
        return self.__aceQLHttpApi.is_gzip_result()

    def set_gzip_result(self, gzip_result):
        """Define if result sets are compressed before download. Defaults to true."""
        self.__aceQLHttpApi.set_gzip_result(gzip_result)

    def get_server_version(self):
        """Gets the server version of AceQL HTTP."""
        return self.__aceQLHttpApi.get_server_version()

    def get_client_version(self):
        """Gets the SDK version."""
        return self.__aceQLHttpApi.get_client_version()

    def close(self):
        """Closes the connection to the remote database but keeps the HTTP session."""
        self.__aceQLHttpApi.close()

    def logout(self):
        """Closes all the connection to the remote database and closes the HTTP session."""
        self.__aceQLHttpApi.logout()

    def get_transaction_isolation(self):
        """Returns the current transaction isolation level."

           Will be one of the following constants:
                transaction_read_uncommitted,
                transaction_read_committed,
                transaction_repeatable_read,
                transaction_serializable, or
                transaction_none.
        """
        return self.__aceQLHttpApi.get_transaction_isolation()

    def set_transaction_isolation(self, level):
        """Sets the transaction isolation level."""
        self.__aceQLHttpApi.set_transaction_isolation(level)

    def get_holdability(self):
        """Returns the holdability.
         One of hold_cursors_over_commit or close_cursors_at_commit.
        """
        return self.__aceQLHttpApi.get_holdability()

    def set_holdability(self, holdability):
        """Sets the holdability."""
        self.__aceQLHttpApi.set_holdability(holdability)

    def is_read_only(self):
        """Says if Connection is read-only."""
        return self.__aceQLHttpApi.is_read_only()

    def set_read_only(self, read_only):
        """Allows to put Connection read-only mode."""
        self.__aceQLHttpApi.set_read_only(read_only)
