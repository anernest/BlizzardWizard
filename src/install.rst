Installing
==========

1. Create the Ionic app

.. code::

    ionic start "BlizzardWizard" tabs --type vue 

#. Initialize Poetry to support python development

.. code::

    cd BlizzardWizard
    poetry init

#. Add Spyce

    poetry add git+https://<github_personal_access_token>@github.com/RATESResearch/Spyce.git#main

#. Install Django and create project

.. code::

    poetry add django
    cd src 
    poetry run django-admin startproject wizard .
