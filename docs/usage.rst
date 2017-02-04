=====
Usage
=====

To use Django-Data-Approvals in a project, add it to your `INSTALLED_APPS`:

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
