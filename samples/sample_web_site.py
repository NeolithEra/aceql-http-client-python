# -*- coding: utf-8 -*-
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

import aceql
from contextlib import closing

server = "http://localhost:9090/aceql"
database = "kawansoft_example"
username = "MyUsername"
password = "MySecret"

# Attempt to establish a connection to the remote SQL database:
connection = aceql.connect(server, database, username, password)
print("Successfully connected to database " + database)

cursor = connection.cursor()

sql = "delete from customer where customer_id >= ?"
params = (0,)
cursor.execute(sql, params)

sql = "insert into customer values (1, 'Sir', 'John', 'Doe', '1 Madison Ave', 'New York', 'NY 10010', NULL)"
cursor.execute(sql)
print("Rows updated: " + str(cursor.rowcount))

with closing(connection.cursor()) as cursor:
    sql = "select customer_id, customer_title, lname from customer where customer_id = 1"
    cursor.execute(sql)

    rows = cursor.fetchall()

    for row in rows:
        print("customer_id   : " + str(row[0]))
        print("customer_title: " + row[1])
        print("lname         : " + row[2])


cursor = connection.cursor()
sql = "update customer set fname = ? where customer_id = ?"
params = ("Jim", 1)
cursor.execute(sql, params)
print("Rows updated: " + str(cursor.rowcount))

