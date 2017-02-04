=============================
Django-Data-Approvals
=============================

.. image:: https://badge.fury.io/py/django-data-approvals.svg
    :target: https://badge.fury.io/py/django-data-approvals

.. image:: https://travis-ci.org/normic/django-data-approvals.svg?branch=master
    :target: https://travis-ci.org/normic/django-data-approvals

.. image:: https://codecov.io/gh/normic/django-data-approvals/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/normic/django-data-approvals

A Django app which makes changes of users approvable, before writing to the production database.

Documentation
-------------

The full documentation is at https://django-data-approvals.readthedocs.io.

Quickstart
----------

Install Django-Data-Approvals::

    pip install django-data-approvals

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'approvals.apps.ApprovalsConfig',
        ...
    )

Add Django-Data-Approvals's URL patterns:

.. code-block:: python

    from approvals import urls as approvals_urls


    urlpatterns = [
        ...
        url(r'^', include(approvals_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
