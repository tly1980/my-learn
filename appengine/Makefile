run:
	dev_appserver.py hello_app

uat:
	appcfg.py --version uat --noauth_local_webserver -A hot-zones update hello_app/

prod:
	appcfg.py --version uat --noauth_local_webserver -A hot-zones update hello_app/