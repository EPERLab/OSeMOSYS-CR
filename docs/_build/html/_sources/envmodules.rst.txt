.. _envmodules:

Creación de módulos de ambiente
===============================

En esta sección se muestra cómo compilar el software para la creación de módulos
de ambiente para el desarrollo y ejecución de programas con requisitos específicos,
sin que exista un conflicto entre estos debido al uso de distintas versiones de
una misma biblioteca o herramienta. De esta manera se puede jugar un poco más en
un entorno estilo caja de arena y hacer pruebas específicas y poder saltar de un
ambiente a otro sin mayor inconveniente, y de manera transparente. Para más información,
se puede consultar el link :cite:`modules,modules2`.

Los módulos de ambiente permiten una gran flexibilidad en el desarrollo del software
al permitir cambiar dinámicamente la versión de las bibliotecas y herramientas,
todo esto según las necesidades del software o del algoritmo que se desea implementar.
Para este caso se compilará desde el código fuente y se dejará en funcionamiento
en el directorio /opt, donde además se manejarán los module files y el código fuente
de lo que se desee implementar como módulo de ambiente :cite:`moduleinstall`.

Primero creamos los directorios donde vamos a manejar el software que se vaya a
compilar y manejar como módulo de ambiente, además de desinstalar la versión de
repositorio de los módulos de ambiente.

.. code-block:: bash

  mkdir -p /opt/src/modulefiles
  mkdir -p /opt/libs/modulefiles
  mkdir -p /opt/tools/modulefiles
  mkdir -p /opt/compilers/modulefiles
  mkdir -p /opt/debug/modulefiles
  mkdir -p /opt/python/modulefiles
  sudo apt purge environment-modules

Es posible que lo anterior desinstale otros programas y herramientas, como es el
caso de mpich y openmpi, pues al instalarlos desde los repositorios, estos se instalan
como si fuesen módulos de ambiente empleando la configuración provista por la versión
de los repositorios. Lo anterior implica que debemos crear estos módulos de ambiente
después de terminar de configurar la versión compilada  de este software.

Clonamos en el directorio /opt/src el repositorio del software de módulos de ambiente
y procedemos a compilarlo.

.. code-block:: bash

  cd /opt/src
  git clone git@github.com:cea-hpc/modules.git # git clone https://github.com/cea-hpc/modules.git
  cd modules
  mkdir /opt/tools/modules-4.0.0
  ./configure --with-module-path=/opt/modules --prefix=/opt/tools/modules-4.0.0
  make
  make install

Con esto ahora procedemos a crear y llenar los archivos de configuración necesarios
para la correcta creación y funcionamiento de los módulos. Primero creamos el archivo
/etc/profile.d/modules.sh el cual define y exporta los directorios, así como los
distintos tipos de shell que se puede tener instalado en el sistema.

.. code-block:: bash

  ln -s /opt/tools/modules-4.0.0 /opt/modules/default
  touch /etc/profile.d/modules.sh
  nano /etc/profile.d/modules.sh

En este archivo agregamos lo siguiente:

.. code-block:: bash

  trap "" 1 2 3

  MID=/opt/modules/default/init

  case "$0" in
          -bash|bash|*/bash) test -f $MID/bash && . $MID/bash ;;
             -ksh|ksh|*/ksh) test -f $MID/ksh && . $MID/ksh ;;
                -sh|sh|*/sh) test -f $MID/sh && . $MID/sh ;;
                          *) test -f $MID/sh && . $MID/sh ;;

  #default for scripts
  esac

  MODULERCFILE=/opt/modulerc
  export MODULERCFILE
  module add null

  trap - 1 2 3

Ahora creamos el archivo modulerc donde se definen los directorios de los
modulefiles para que el archivo modules.sh funcione correctamente.

.. code-block:: bash

  #%Module
  append-path MODULEPATH /opt/libs/modulefiles
  append-path MODULEPATH /opt/tools/modulefiles
  append-path MODULEPATH /opt/compilers/modulefiles
  append-path MODULEPATH /opt/python/modulefiles
  append-path MODULEPATH /opt/debug/modulefiles

  # system-wide pre-loaded standard modules:
  set defmodules {}
  foreach m $defmodules {
    if {! [ is-loaded $m ] } {
      module load $m
      }
  }

En caso de tener disponible tcsh, creamos además el archivo /etc/profile.d/modules.csh
y lo editamos con nano o vim. Agregamos lo siguiente:

.. code-block:: bash

  if ($?tcsh) then
  	set modules_shell="tcsh"
  else
  	set modules_shell="csh"
  endif

  if ( -f /opt/modules/default/init/${modules_shell} ) then
     source /opt/modules/default/init/${modules_shell}
  endif

  setenv MODULERCFILE /opt/modulerc
  module add null

  unset modules_shell

Finalmente recargamos los archivos de configuración mediante el comando source.

.. code-block:: bash

  source /etc/profile.d/modules.sh

Adicionalmente al procedimiento anterior, se creó un script que automatiza el
procedimiento anterior en caso de que sea necesaria una reinstalación. Se replicará
esta metodología en la creación de los módulos de ambiente para facilitar la
administración de este sistema.

.. code-block:: bash

  #!/bin/bash


  soft=modules
  version=4.0.0
  src=/opt/src
  install=/opt/tools
  mod_path=${install}/modulefiles/${soft}
  prefix=${install}/${soft}-${version}
  cd $src
  mkdir -p ${prefix}
  git clone https://github.com/cea-hpc/modules.git
  cd $soft
  ./configure --with-module-path=/opt/modules --prefix=/opt/tools/modules-4.0.0
  make
  make install
  mkdir -p /opt/modules
  ln -s ${prefix} /opt/modules/default

  /bin/cat <<"#EOF#" > /etc/profile.d/modules.sh
  trap "" 1 2 3

  MID=/opt/modules/default/init/

  case "$0" in
        -bash|bash|*/bash) test -f $MID/bash && . $MID/bash ;;
           -ksh|ksh|*/ksh) test -f $MID/ksh && . $MID/ksh ;;
              -sh|sh|*/sh) test -f $MID/sh && . $MID/sh ;;
                        *) test -f $MID/sh && . $MID/sh ;;

  #default for scripts
  esac

  MODULERCFILE=/opt/modulerc
  export MODULERCFILE
  module add null

  trap - 1 2 3

  #EOF#


  /bin/cat <<"#EOF#" > /etc/profile.d/modules.csh
  if ($?tcsh) then
  set modules_shell="tcsh"
  else
  set modules_shell="csh"
  endif

  if ( -f /opt/modules/default/init/${modules_shell} ) then
   source /opt/modules/default/init/${modules_shell}
  endif

  setenv MODULERCFILE /opt/modulerc
  module add null

  unset modules_shell

  #EOF#

  /bin/cat <<"#EOF#" > /opt/modulerc
  #%Module
  append-path MODULEPATH /opt/libs/modulefiles
  append-path MODULEPATH /opt/tools/modulefiles
  append-path MODULEPATH /opt/compilers/modulefiles
  append-path MODULEPATH /opt/python/modulefiles
  append-path MODULEPATH /opt/debug/modulefiles
  append-path MODULEPATH /opt/intel/modulefiles

  # system-wide pre-loaded standard modules:
  set defmodules {}
  foreach m $defmodules {
  if {! [ is-loaded $m ] } {
    module load $m
    }
  }

  #EOF#

.. _envmodules-crear_modulo:

Creación de módulo de ambiente
------------------------------

Una vez instalada la infraestructura para instalar módulos de ambiente, lo que procede
es crear nuestros módulos. Generalmente esto implica descargar los instaladores
o el código fuente y compilar en directorios que no necesariamente están dentro
de las variables de entorno del sistema.
