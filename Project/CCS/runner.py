"""This file is used to call the first login page,
this was necessary to avoid circular import errors"""

import login_pg
import customer_home_pg
import applyc_pg
import approve_cust_pg

login_pg.call_login_pg()