from django.db import connection
#db_name = connection.settings_dict['NAME']
# Or alternatively
db_name = connection.get_connection_params()['db']