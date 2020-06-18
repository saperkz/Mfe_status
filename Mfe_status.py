import subprocess
import smtplib

p = subprocess.Popen(["hostname"], stdout=subprocess.PIPE)
host_output, err = p.communicate()

service1 = "mfeespd"

p =  subprocess.Popen(["systemctl", "is-active",  service1], stdout=subprocess.PIPE)
mfeespd_output, err = p.communicate()

service2 = "mfetpd"

p =  subprocess.Popen(["systemctl", "is-active",  service2], stdout=subprocess.PIPE)
mfetpd_output, err = p.communicate()



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
smtpObj.sendmail('o.omarov@kazatomprom.kz', 'o.omarov@kaptechnology.kazatomprom.kz', '\n %s' % summary)
smtpObj.quit()
