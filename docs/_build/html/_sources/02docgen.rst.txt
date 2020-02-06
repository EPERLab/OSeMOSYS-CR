.. _docgen:

Generación de documentación en Sphinx
=====================================

Sphinx es una herramienta para generación de documentación originalmente pensada
para proyectos en Python, pero que en su implementación permite trabajar en otros
lenguajes y documentar toda clase de proyectos en general. Es una alternativa que
genera un html el cual puede ser montado en una página web, y que además puede ser
exportado a Látex y a otros formatos. Es adicionalmente compatible con Doxygen.
Sphinx utiliza RST como formato para la generación de documentos, y cuenta con una
sintaxis bastante amigable en general.

Para la generación de la documentación se requiere de una serie de paquetes y plugins
los cuales se mencionan en :ref:`linuxsteps-install_packs`.

.. _docgen-quickstart:

Creación del archivo base conf.py
---------------------------------

Luego de instalar los paquetes requeridos, procedemos a crear en el directorio
del proyecto a documentar (generalmente llamado docs). Ingresamos a este directorio
y ejecutamos el comando sphinx-quickstart.

.. code-block:: bash

  cd ruta/del/proyecto
  mkdir docs
  sphinx-quickstart

Este comando genera una serie de preguntas las cuales deben responderse para
autogenerar la documentación de forma rápida y sencilla. En este caso particular
se respondieron de la siguiente forma:

.. code-block:: bash

  Welcome to the Sphinx 1.7.6 quickstart utility.

  Please enter values for the following settings (just press Enter to
  accept a default value, if one is given in brackets).

  Selected root path: .

  You have two options for placing the build directory for Sphinx output.
  Either, you use a directory "_build" within the root path, or you separate
  "source" and "build" directories within the root path.
  > Separate source and build directories (y/n) [n]: n

  Inside the root directory, two more directories will be created; "_templates"
  for custom HTML templates and "_static" for custom stylesheets and other static
  files. You can enter another prefix (such as ".") to replace the underscore.
  > Name prefix for templates and static dir [_]: _

  The project name will occur in several places in the built documentation.
  > Project name: eperdoc
  > Author name(s): Willy Villalobos
  > Project release []: 1.0.0

  If the documents are to be written in a language other than English,
  you can select a language here by its language code. Sphinx will then
  translate text that it generates into that language.

  For a list of supported codes, see
  http://sphinx-doc.org/config.html#confval-language.
  > Project language [en]: es

  The file name suffix for source files. Commonly, this is either ".txt"
  or ".rst".  Only files with this suffix are considered documents.
  > Source file suffix [.rst]: .rst

  One document is special in that it is considered the top node of the
  "contents tree", that is, it is the root of the hierarchical structure
  of the documents. Normally, this is "index", but if your "index"
  document is a custom template, you can also set this to another filename.
  > Name of your master document (without suffix) [index]: index

  Sphinx can also add configuration for epub output:
  > Do you want to use the epub builder (y/n) [n]: n
  Indicate which of the following Sphinx extensions should be enabled:
  > autodoc: automatically insert docstrings from modules (y/n) [n]: y
  > doctest: automatically test code snippets in doctest blocks (y/n) [n]: n
  > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
  > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
  > coverage: checks for documentation coverage (y/n) [n]: n
  > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: y
  > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: n
  > ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
  > viewcode: include links to the source code of documented Python objects (y/n) [n]: n
  > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n

  A Makefile and a Windows command file can be generated for you so that you
  only have to run e.g. `make html' instead of invoking sphinx-build
  directly.
  > Create Makefile? (y/n) [y]: y
  > Create Windows command file? (y/n) [y]: y

  Creating file ./conf.py.
  Creating file ./index.rst.
  Creating file ./Makefile.
  Creating file ./make.bat.

  Finished: An initial directory structure has been created.

  You should now populate your master file ./index.rst and create other documentation
  source files. Use the Makefile to build the docs, like so:
   make builder
  where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

Esto genera un archivo base llamado conf.py donde se indican los ajustes a tomar
en cuenta para la generación de documentación. En nuestro caso particular, se han
hecho ajustes adicionales para tener un formato más acorde a lo que se necesita.
Con esto en consideración, tenemos el siguiente archivo conf.py.

.. code-block:: python

  # -*- coding: utf-8 -*-
  #
  # eperdoc documentation build configuration file, created by
  # sphinx-quickstart on Wed Aug  1 11:44:55 2018.
  #
  # This file is execfile()d with the current directory set to its
  # containing dir.
  #
  # Note that not all possible configuration values are present in this
  # autogenerated file.
  #
  # All configuration values have a default; values that are commented out
  # serve to show the default.

  # If extensions (or modules to document with autodoc) are in another directory,
  # add these directories to sys.path here. If the directory is relative to the
  # documentation root, use os.path.abspath to make it absolute, like shown here.
  #
  import os
  import sys
  #Estaba comentado
  sys.path.insert(0, os.path.abspath('.'))
  #Agregado por prevención
  sys.path.insert(0, os.path.abspath('../'))

  # -- General configuration ------------------------------------------------

  # If your documentation needs a minimal Sphinx version, state it here.
  #
  # needs_sphinx = '1.0'

  # Add any Sphinx extension module names here, as strings. They can be
  # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
  # ones.
  extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinxcontrib.bibtex'] # Agregado napoleon extension

  #Agregado
  napoleon_google_docstring = False
  napoleon_use_param = False
  napoleon_use_ivar = True

  # Add any paths that contain templates here, relative to this directory.
  templates_path = ['_templates']

  # The suffix(es) of source filenames.
  # You can specify multiple suffix as a list of string:
  #
  # source_suffix = ['.rst', '.md']
  source_suffix = '.rst'

  # The master toctree document.
  master_doc = 'index'

  # General information about the project.
  project = u'eperdoc'
  copyright = u'2018, Willy Villalobos'
  author = u'Willy Villalobos'

  # The version info for the project you're documenting, acts as replacement for
  # |version| and |release|, also used in various other places throughout the
  # built documents.
  #
  # The short X.Y version.
  version = u'1.0'
  # The full version, including alpha/beta/rc tags.
  release = u'1.0.a'

  # The language for content autogenerated by Sphinx. Refer to documentation
  # for a list of supported languages.
  #
  # This is also used if you do content translation via gettext catalogs.
  # Usually you set "language" from the command line for these cases.
  language = 'es'

  # List of patterns, relative to source directory, that match files and
  # directories to ignore when looking for source files.
  # This patterns also effect to html_static_path and html_extra_path
  exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

  # The name of the Pygments (syntax highlighting) style to use.
  pygments_style = 'sphinx'

  # If true, `todo` and `todoList` produce output, else they produce nothing.
  todo_include_todos = True


  # -- Options for HTML output ----------------------------------------------

  # The theme to use for HTML and HTML Help pages.  See the documentation for
  # a list of builtin themes.
  #
  # html_theme = 'alabaster'
  html_theme = 'sphinx_rtd_theme'

  # Theme options are theme-specific and customize the look and feel of a theme
  # further.  For a list of options available for each theme, see the
  # documentation.
  #
  # html_theme_options = {}

  # Add any paths that contain custom static files (such as style sheets) here,
  # relative to this directory. They are copied after the builtin static files,
  # so a file named "default.css" will overwrite the builtin "default.css".
  html_static_path = ['_static']

  # Custom sidebar templates, must be a dictionary that maps document names
  # to template names.
  #
  # This is required for the alabaster theme
  # refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
  html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
  }


  # -- Options for HTMLHelp output ------------------------------------------

  # Output file base name for HTML help builder.
  htmlhelp_basename = 'eperdocdoc'


  # -- Options for LaTeX output ---------------------------------------------

  latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
  }

  # Grouping the document tree into LaTeX files. List of tuples
  # (source start file, target name, title,
  #  author, documentclass [howto, manual, or own class]).
  latex_documents = [
    (master_doc, 'eperdoc.tex', u'eperdoc Documentation',
     u'Willy Villalobos', 'manual'),
  ]


  # -- Options for manual page output ---------------------------------------

  # One entry per manual page. List of tuples
  # (source start file, name, description, authors, manual section).
  man_pages = [
    (master_doc, 'eperdoc', u'eperdoc Documentation',
     [author], 1)
  ]


  # -- Options for Texinfo output -------------------------------------------

  # Grouping the document tree into Texinfo files. List of tuples
  # (source start file, target name, title, author,
  #  dir menu entry, description, category)
  texinfo_documents = [
    (master_doc, 'eperdoc', u'eperdoc Documentation',
     author, 'eperdoc', 'One line description of project.',
     'Miscellaneous'),
  ]


  # Example configuration for intersphinx: refer to the Python standard library.
  intersphinx_mapping = {'https://docs.python.org/': None}

  def setup(app):
    app.add_stylesheet('theme_overrides.css')

La última definición es un ajuste que se hace al tema para facilitar su visualización
en otrs dispositivos y resoluciones. Dicho archivo se crea en el directorio _static,
y contiene lo siguiente:

.. code-block:: css

  /* override table width restrictions as found on https://github.com/getpelican/pelican/issues/1311 */
  .wy-table-responsive table td, .wy-table-responsive table th {
    /* !important prevents the common CSS stylesheets from
       overriding this as on RTD they are loaded after this stylesheet */
    white-space: normal !important;
  }

  .wy-table-responsive {
    overflow: visible !important;
  }

.. _docgen-syntax:

Sintaxis básica de archivos rst
-------------------------------

Para empezar a generar la documentación como tal, debemos escribir el contenido
en archivos de extensión .rst los cuales sphinx interpreta para generar el documento
en el formato deseado. Lo primero que debemos considerar son los títulos, secciones,
y subsecciones, así como la generación de cuadros y listas. Presentamos un pequeño
ejemplo y el respectivo resultado :cite:`rstsyntax`.

.. code-block:: rst

  .. _ejemplo:

  *******
  Ejemplo
  *******

  subtitle
  ########

  subsubtitle
  ***********

  .. _docgen-etiqueta:

  section
  =======

  subsection
  ----------

  subsubsection
  ^^^^^^^^^^^^^

  subsubsection
  ~~~~~~~~~~~~~

  Texto normal estilo loren ipsum y una referencia a sintaxis :cite:`rstsyntax`

  Ahora una imagen con una etiqueta para referenciarla :ref:`docgen-fig00` y de
  igual forma una referencia a una sección :ref:`docgen-etiqueta`.

  .. _docgen-fig00

  .. figure:: img/linuxsteps/ssh_gitlab.png
    :align: center
    :width: 100 px
    :alt: Imagen de ejemplo.

    Imagen de ejemplo.

  Listas
  ------

  * This is a bulleted list.
  * It has two items, the second
    item uses two lines. (note the indentation)

  1. This is a numbered list.
  2. It has two items too.

  #. This is a numbered list.
  #. It has two items too.

  Cuadro simple
  -------------

  +---------+---------+-----------+
  | 1       |  2      |  3        |
  +---------+---------+-----------+

  Cuadro más elaborado
  --------------------

  +------------+------------+-----------+
  | Header 1   | Header 2   | Header 3  |
  +============+============+===========+
  | body row 1 | column 2   | column 3  |
  +------------+------------+-----------+
  | body row 2 | Cells may span columns.|
  +------------+------------+-----------+
  | body row 3 | Cells may  | - Cells   |
  +------------+ span rows. | - contain |
  | body row 4 |            | - blocks. |
  +------------+------------+-----------+

  Cuadro alternativo
  ------------------

  =====  =====  ======
     Inputs     Output
  ------------  ------
    A      B    A or B
  =====  =====  ======
  False  False  False
  True   False  True
  =====  =====  ======

  Cuadro estilo Látex
  -------------------

  .. tabularcolumns:: |l|c|p{5cm}|

  +--------------+---+-----------+
  |  simple text | 2 | 3         |
  +--------------+---+-----------+

El código anterior puede apreciarse en la sección :ref:`ejemplo`.

.. _docgen-compile:

Compilación y estructura básica de la documentación
---------------------------------------------------

El comando sphinx-quickstart genera una serie de directorios, un Makefile y un
archivo index.rst que sirve como base para agregar archivos adicionales. Este
archivo index.rst tiene el siguiente aspecto básico:

.. code-block:: rst

  .. eperdoc documentation master file, created by
     sphinx-quickstart on Wed Aug  1 11:44:55 2018.
     You can adapt this file completely to your liking, but it should at least
     contain the root `toctree` directive.

  Documentación Proyecto Eléctrico EPER
  =====================================

  .. toctree::
     :maxdepth: 2
     :caption: Contenidos

     linuxsteps
     docgen
     envmodules
     ejemplo
     refs

  Índices y cuadros
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

Como se puede observar, basta con agregar los nombres sin extensión de los archivos
para que estos se agreguen a la documentación. De esta forma es posible trabajar
de forma modularizada.

A la hora de compilar tenemos varias opciones, incluyendo la posibilidad de generar
código en Látex. los de interés en nuestro caso serán los siguientes:

.. code-block:: bash

  make html # Genera la documentación normal en html.
  make latexpdf # Genera el código en Látex y un pdf.

Otros formatos y opciones se pueden visualizar con el comando make help.
