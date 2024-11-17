<h3 align="center">Delivery website</h3>
<p align="center">simple delivery website with simple configuration settings</p>

<h4 align="center"> build setup </h4>

```
# clone the repo into your disk

$ git clone https://github.com/hellcard/site-configuration.git

# installing dependencies

$ cd site-configuration
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install django~=4.1

# server startup

(.venv)$ python manage.py runserver
```


<h3 align="center">The following routes are available:</h3>
<p align=center>'delivery/main/' - main page</p>
<p align="center">'delivery/add/' - add page</p>
<p align="center">'delivery/delivery/int:id/' - sorted deliveries</p>

<h3 align="center">admin pannel</h3>
<p align="center">Login: admin</p>
<p align="center">Password: 123</p>
