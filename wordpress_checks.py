#!/usr/bin/env python
import os
import re
from datetime import date, timedelta
from os.path import join, isfile

# Define the day of interest in the Apache common log format.


try:
    # daysago = int(sys.argv[1])
    daysago = 1
except:
    daysago = 1
the_day = date.today() - timedelta(daysago)
apache_day = the_day.strftime('[%d/%b/%Y:')

# Define Output file
stats_output = open(os.getcwd() + '/stats.txt', "w")

# Define log path directory
path = "/home/username/Desktop/domlogs"

# Get list of dir contents
logs_path_contents = os.listdir(path)

# Get list of files only from this directory
logs = filter(lambda f: isfile(join(path, f)), logs_path_contents)

# Initialize dictionaries for hit counters
wp_login_dict = {}
wp_cron_dict = {}
wp_xmlrpc_dict = {}
wp_admin_ajax_dict = {}

for log in logs:
    file = os.path.join(path, log)
    text = open(file, "r")
    wp_login_hit_count = 0
    wp_cron_hit_count = 0
    wp_xmlrpc_hit_count = 0
    wp_admin_ajax_hit_count = 0
    for line in text:
        if apache_day in line:
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

    log = log.replace('-ssl_log', '', 1)
    log = log.replace('.access_log', '', 1)

    wp_login_dict[log] = int(wp_login_hit_count)
    wp_cron_dict[log] = int(wp_cron_hit_count)
    wp_xmlrpc_dict[log] = int(wp_xmlrpc_hit_count)
    wp_admin_ajax_dict[log] = int(wp_admin_ajax_hit_count)

    #    print(log)
    #    print("Wordpress Logins => " + str(wp_login_hit_count))
    #    print("Wordpress wp-cron => " + str(wp_cron_hit_count))
    #    print("Wordpress xmlrpc => " + str(wp_xmlrpc_hit_count))
    #    print("Wordpress admin-ajax => " + str(wp_admin_ajax_hit_count))
    #    print("===============================================================")
    text.close()


# print(wp_login_dict.mostcommon(10))
# print(wp_cron_dict.mostcommon(10))
# print(wp_xmlrpc_dict.mostcommon(10))
# print(wp_admin_ajax_dict.mostcommon(10))

# d = sorted(a.items(),key=lambda x: (x[1], x[0]), reverse=True)  # Value then Key

# wp_logintop = sorted(wp_login_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)  # Value then Key

# wp_crontop = sorted(wp_cron_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)  # Value then Key

# wp_xmlrpctop = sorted(wp_xmlrpc_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)  # Value then Key

# wp_admin_ajaxtop = sorted(wp_admin_ajax_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)  # Value then Key

# print('+++++++++++++++++++++++++++++++++++')
# print('The original Wordpress login dictionary')
# print(wp_login_dict)
# print('+++++++++++++++++++++++++++++++++++')
# print('The sorted Wordpress login dictionary')
# print(wp_logintop)
# print('+++++++++++++++++++++++++++++++++++')
# print('+++++++++++++++++++++++++++++++++++')
# print('The original Wordpress wp-cron dictionary')
# print(wp_cron_dict)
# print('+++++++++++++++++++++++++++++++++++')
# print('The sorted Wordpress cron dictionary')
# print(wp_crontop)
# print('+++++++++++++++++++++++++++++++++++')
# print('+++++++++++++++++++++++++++++++++++')
# print('The original Wordpress wp-xmlrpc dictionary')
# print(wp_xmlrpc_dict)
# print('+++++++++++++++++++++++++++++++++++')
# print('The sorted Wordpress xmlrpc dictionary')
# print(wp_xmlrpctop)
# print('+++++++++++++++++++++++++++++++++++')
# print('+++++++++++++++++++++++++++++++++++')
# print('The original Wordpress wp-admin ajax dictionary')
# print(wp_admin_ajax_dict)
# print('+++++++++++++++++++++++++++++++++++')
# print('The sorted Wordpress admin_ajax dictionary')
# print(wp_admin_ajaxtop)
# print('+++++++++++++++++++++++++++++++++++')
# print('+++++++++++++++++++++++++++++++++++')

# print('sorted_d')
# print(sorted_d)
# print('Sorted reverse')
# print(sortedreverse)

# d = Counter(
# d = Counter(wp_login_dict)
# d.most_common()
# for k, v in d.most_common(10):
#  print('%s: %i' % (k, v))

# create a function which returns the value of a dictionary
def keyfunction(k):
    return d[k]


d = wp_login_dict

print('''
Wordpress Bruteforce Logins for wp-login.php %s''' % the_day.strftime('%b %d, %Y'))
print('============================================')
# sort by dictionary by the values and print top 10 {key, value} pairs
for key in sorted(d, key=keyfunction, reverse=True)[:10]:
    print("%s: %i" % (key, d[key]))
print('============================================')

d = wp_cron_dict

print('''
Wordpress Cron wp-cron.php(virtual cron) checks for %s''' % the_day.strftime('%b %d, %Y'))
print('============================================')
# sort by dictionary by the values and print top 10 {key, value} pairs
for key in sorted(d, key=keyfunction, reverse=True)[:10]:
    print("%s: %i" % (key, d[key]))
print('============================================')

d = wp_xmlrpc_dict

print('''
Wordpress XMLRPC Attacks checks for xmlrpc.php for %s''' % the_day.strftime('%b %d, %Y'))
print('============================================')
# sort by dictionary by the values and print top 10 {key, value} pairs
for key in sorted(d, key=keyfunction, reverse=True)[:10]:
    print("%s: %i" % (key, d[key]))
print('============================================')

d = wp_admin_ajax_dict

print('''
Wordpress Heartbeat API checks for admin-ajax.php for %s''' % the_day.strftime('%b %d, %Y'))
print('============================================')
# sort by dictionary by the values and print top 10 {key, value} pairs
for key in sorted(d, key=keyfunction, reverse=True)[:10]:
    print("%s: %i" % (key, d[key]))
print('============================================')
