.. _getting-started:

Getting Started
===============

Installing
----------

Molduck is made up of two components: a webserver and a CLI. Please, take a look
at the documentation of the component you want to install.

.. toctree::
   :maxdepth: 1
   :includehidden:

   ../usage/webserver
   ../usage/cli


Contribute
----------

Contributions are welcome and appreciated.
This section serves as a helper to get you started on contributing.

Prerequisites
~~~~~~~~~~~~~

- `Git`_: version control.
- `Rye`_: python dependencies and virtual environment manager.

Start development server
~~~~~~~~~~~~~~~~~~~~~~~~

#. First, you need to clone the repository:

   .. code-block:: console
    
      $ git clone git@github.com:themagiulio/molduck.git

#. The project uses Rye to manage dependencies and virtual environment. Run the following command to get started:

   .. code-block:: console
      
      $ rye sync


#. Create database:

   .. code-block:: console
     
      $ python ./projects/webserver/manage.py migrate

#. Start dev server:

   .. code-block:: console

      $ python ./projects/webserver/manage.py runserver


.. _`Git`: https://git-scm.com/
.. _`Rye`: https://rye.astral.sh/
