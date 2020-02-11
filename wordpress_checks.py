#!/usr/bin/env python
import os
import re
from datetime import date, timedelta

# Define the day of interest in the Apache common log format.
try:
    # daysAgo = int(sys.argv[1])
    daysAgo = 1
except:
    daysAgo = 1
theDay = date.today() - timedelta(daysAgo)
apacheDay = theDay.strftime('[%d/%b/%Y:')

path = "/home/username/Desktop/domlogs"
logs_path = os.listdir(path)
stats_output = open(os.getcwd() + '/stats.txt', "w")

# Initialize dictionaries for hit count tallys
wp_login_dict = {}
wp_cron_dict = {}
wp_xmlrpc_dict = {}
wp_admin_ajax_dict = {}

for log in logs_path:
    file = os.path.join(path, log)
    text = open(file, "r")
    wp_login_hit_count = 0
    wp_cron_hit_count = 0
    wp_xmlrpc_hit_count = 0
    wp_admin_ajax_hit_count = 0
    for line in text:
        if re.match("(.*)(wp-login.php)(.*)", line):
            wp_login_hit_count = wp_login_hit_count + 1
        if re.match("(.*)(wp-cron.php)(.*)", line):
            wp_cron_hit_count = wp_cron_hit_count + 1
        if re.match("(.*)(xmlrpc.php)(.*)", line):
            wp_xmlrpc_hit_count = wp_xmlrpc_hit_count + 1
        if re.match("(.*)(admin-ajax.php)(.*)", line):
            wp_admin_ajax_hit_count = wp_admin_ajax_hit_count + 1
            # print >> stats_output, log + "|" + line,
            # print(log + "|" + line, end="", file=stats_output)

    log = log.replace('.access_log', '', 1)

    wp_login_dict[log] = str(wp_login_hit_count)
    wp_cron_dict[log] = str(wp_cron_hit_count)
    wp_xmlrpc_dict[log] = str(wp_xmlrpc_hit_count)
    wp_admin_ajax_dict[log] = str(wp_admin_ajax_hit_count)

    print(log)
    print("Wordpress Logins => " + str(wp_login_hit_count))
    print("Wordpress wp-cron => " + str(wp_cron_hit_count))
    print("Wordpress xmlrpc => " + str(wp_xmlrpc_hit_count))
    print("Wordpress admin-ajax => " + str(wp_admin_ajax_hit_count))
    print("===============================================================")
    text.close()

print(wp_login_dict.mostcommon(10))
print(wp_cron_dict.mostcommon(10))
print(wp_xmlrpc_dict.mostcommon(10))
print(wp_admin_ajax_dict.mostcommon(10))
