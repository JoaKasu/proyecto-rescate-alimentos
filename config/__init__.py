import pymysql
pymysql.install_as_MySQLdb()

# 1. Parche MariaDB para XAMPP
from django.db.backends.base.base import BaseDatabaseWrapper
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# 2. Parche integral para Python 3.14 (compatibilidad con copy en Context y RequestContext)
from django.template import context

def _patched_context_copy(self):
    duplicate = copy_obj = object.__new__(self.__class__)
    duplicate.__dict__.update(self.__dict__)
    duplicate.dicts = self.dicts[:]
    return duplicate

context.BaseContext.__copy__ = _patched_context_copy
context.Context.__copy__ = _patched_context_copy