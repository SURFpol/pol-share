Project Open Leermaterialen Share
=================================

This repo is a proof of technology that it is possible for teachers 
to export their learning materials from a LMS to a repository (ShareKit in principle). 


Requirements
------------

This project assumes that you have Docker and docker-compose installed and SSL enabled for a domain.


Installation
------------

```bash
docker-compose up
```

Now find the running container id with

```bash
docker ps
```

And add your own Django superuser with

```bash
docker exec -it <container-id> bash
./manage.py createsuperuser
```

Usage
-----

When the containers are running an administration interface is available at ```https://example.com/admin/```.
Under the *IMS* section of the admin you first need to add a LTIApp with the following values:
* slug => share
* view => share:common-cartridge-fetch
* title => Share (but can be anything)
* description => An LTI app to share Common Cartridges (but can be anything)
* privacy_level => public

Then you need to add at least one tenant. One example tenant:
* app => (select the app you made above)
* organization => SURFnet
* slug => surfnet (gets autocompleted)
* lms => canvas
* api_key => a canvas API key
* api_secret => the API secret belonging to the API key

When saving use the "save" button and note down the 
```consumer_key```, ```shared_secret``` and ```config_url``` from the overview.

Now in your Canvas instance you can add the LTI and use the "by URL" option.
You can fill out the ```consumer_key```, ```shared_secret```, ```config_url``` values here.
After you fill out the form the LTI app and LMS should configure themselves and the LTI app should become available.

After you've used the LTI app to share a course the course content will be available as a IMSArchive instance.
