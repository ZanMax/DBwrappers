#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

class SQLiteDB():
	"""SQLite wrapper"""

	def __init__(self, dbfile):
		self.dbfile = dbfile
	
	def select(self, columns, table_names, condition = ""):
		if not isinstance(table_names, basestring):
			table_names = ", ".join(table_names)

		if not isinstance(columns, basestring):
			columns = ", ".join(columns)

		conn = sqlite3.connect(self.dbfile)

		try:
			cursor = conn.execute("select {0} from {1} {2}".format(columns, table_names, condition))
			return cursor.fetchall()
		except Exception, err:
			return err
		finally:
			conn.close()

	def insert(self, diction, table_name):
		if isinstance(diction, dict):
			keys = ", ".join("{}".format(key) for key in diction)
			values = ", ".join("'{}'".format(diction[key]) for key in diction)
			diction = "({0}) values ({1})".format(keys, values)

		conn = sqlite3.connect(self.dbfile)
		
		try:
			cursor = conn.execute("insert into {0} {1}".format(table_name, diction))
			conn.commit()
			return cursor.lastrowid
		except Exception, err:
			return err
		finally:
			conn.close()

	def update(self, diction, table_names, condition = ""):
		if not isinstance(table_names, basestring):
			table_names = ", ".join(table_names)

		if isinstance(diction, dict):
			diction = ", ".join("{}='{}'".format(k, v) for k, v in diction.items())

		conn = sqlite3.connect(self.dbfile)
		
		try:
			cursor = conn.execute("update {0} set {1} {2}".format(table_names, diction, condition))
			conn.commit()
			return True
		except Exception, err:
			return err
		finally:
			conn.close()

	def delete(self, table_names, condition = ""):
		if not isinstance(table_names, basestring):
			table_names = ", ".join(table_names)

		if isinstance(diction, dict):
			diction = ", ".join("{}='{}'".format(k, v) for k, v in diction.items())

		conn = sqlite3.connect(self.dbfile)
		
		try:
			cursor = conn.execute("delete from {0} where {1}".format(table_names, condition))
			conn.commit()
			return True
		except Exception, err:
			return err
		finally:
			conn.close()