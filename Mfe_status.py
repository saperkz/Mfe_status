# ***************************
# App: ConverP12
# Description: Converts all certificates in folder with name "AUTH..." and "RSA..." also shows "issued to" and expiration date
# Date: 03.04.2020
# Author: Olzhas Omarov
# Python version: 3.8
# Compatibility: Any
# Email: ooskenesary@gmail.com
# ***************************

import subprocess
import smtplib

#--GET HOSTNAME OF SERVER----------------------------------------------------
p = subprocess.Popen(["hostname"], stdout=subprocess.PIPE)
host_output, err = p.communicate()


#--CHECK MFE SERVICES: mfeespd and mfetpd------------------------------------

service1 = "mfeespd"

p =  subprocess.Popen(["systemctl", "is-active",  service1], stdout=subprocess.PIPE)
mfeespd_output, err = p.communicate()

service2 = "mfetpd"

p =  subprocess.Popen(["systemctl", "is-active",  service2], stdout=subprocess.PIPE)
mfetpd_output, err = p.communicate()


#--CHECK MFE EXCLUSIONS------------------------------------------------------
p = subprocess.Popen(["/opt/McAfee/ens/tp/bin/mfetpcli", "--getoasconfig", "--exclusionlist", "--profile", "standard"], stdout=subprocess.PIPE)
excl_output, err = p.communicate()

summary="======================================================================"+'\n'+"hostname"+'\t'+host_output+service1+'\t'+mfeespd_output+service2+'\t'+mfetpd_output+excl_output


#======optional: save to file===================
# with open("/nfs2/mfe_output.txt", "a") as f:
#     f.write(summary)
# f.close


#==========SMTP(must be "open relay" on smtp server)=================

smtpObj=smtplib.SMTP('IP_or_dns_name_mail_server', 25)
smtpObj.ehlo()
smtpObj.sendmail('recpnt1@domain.com', 'recpnt2@domain.com', '\n %s' % summary)
smtpObj.quit()
