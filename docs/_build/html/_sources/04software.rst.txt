.. _software:

Software y módulos adicionales
==============================

.. _software-anaconda:

Módulo de ambiente Anaconda
---------------------------

Anaconda es una plataforma de desarrollo centrada en aplicaciones de Machine Learning,
la cual puede instalarse y correrse en cualquier sistema operativo. Esta plataforma
emplea Python y R como herramientas básicas para que los usuarios puedan desarrollar
sus algoritmos con bastante facilidad. Para descargarlo se puede partir del siguiente
`enlace <https://www.anaconda.com/download/#linux>`_.

Anaconda 2
~~~~~~~~~~

Para instalarlo deberemos descargar el software desde la página mencionada anteriormente.
Una vez descargado, ejecutamos el instalador con permisos administrativos si deseamos
instalarlo en una ruta por defecto del PATH del sistema, o como usuario normal si
deseamos manejar el software desde nuestro home. En nuestro caso particular lo que
haremos es crear un módulo de ambiente en /opt/python/anaconda2-5.2.0 por lo que
requerimos permisos administrativos.

.. code-block:: bash

  sudo bash Anaconda2-5.2.0-Linux-x86_64.sh

En este paso basta con aceptar el acuerdo de licencia y proveer una ruta de instalación,
en este caso /opt/python/anaconda2-5.2.0 y luego le indicaremos que no agregue al
.bashrc la exportación de la variable de entorno PATH. Si lo deseamos, podemos instalar
Visual Studio Code, el cual es un editor de texto desarrollado por Microsoft.

.. code-block:: bash

  Welcome to Anaconda2 5.2.0

  In order to continue the installation process, please review the license
  agreement.
  Please, press ENTER to continue
  >>>
  ===================================
  Anaconda End User License Agreement
  ===================================

  Copyright 2015, Anaconda, Inc.

  All rights reserved under the 3-clause BSD License:

  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * Neither the name of Anaconda, Inc. ("Anaconda, Inc.") nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTI
  CULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ANACONDA, INC. BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITU
  TE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) AR
  ISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

  Notice of Third Party Software Licenses
  =======================================

  Anaconda Distribution contains open source software packages from third parties. These are available on an "as is" basis and subject to their individual license agreements. These licenses are available in Anacon
  da Distribution or at http://docs.anaconda.com/anaconda/pkg-docs. Any binary packages of these third party tools you obtain via Anaconda Distribution are subject to their individual licenses as well as the Anaco
  nda license. Anaconda, Inc. reserves the right to change which third party tools are provided in Anaconda Distribution.

  In particular, Anaconda Distribution contains re-distributable, run-time, shared-library files from the Intel(TM) Math Kernel Library ("MKL binaries"). You are specifically authorized to use the MKL binaries wit
  h your installation of Anaconda Distribution. You are also authorized to redistribute the MKL binaries with Anaconda Distribution or in the conda package that contains them. Use and redistribution of the MKL bin
  aries are subject to the licensing terms located at https://software.intel.com/en-us/license/intel-simplified-software-license. If needed, instructions for removing the MKL binaries after installation of Anacond
  a Distribution are available at http://www.anaconda.com.

  Anaconda Distribution also contains cuDNN software binaries from NVIDIA Corporation ("cuDNN binaries"). You are specifically authorized to use the cuDNN binaries with your installation of Anaconda Distribution.
  You are also authorized to redistribute the cuDNN binaries with an Anaconda Distribution package that contains them. If needed, instructions for removing the cuDNN binaries after installation of Anaconda Distrib
  ution are available at http://www.anaconda.com.


  Anaconda Distribution also contains Visual Studio Code software binaries from Microsoft Corporation ("VS Code"). You are specifically authorized to use VS Code with your installation of Anaconda Distribution. Us
  e of VS Code is subject to the licensing terms located at https://code.visualstudio.com/License.

  Cryptography Notice
  ===================

  This distribution includes cryptographic software. The country in which you currently reside may have restrictions on the import, possession, use, and/or re-export to another country, of encryption software. BEF
  ORE using any encryption software, please check your country's laws, regulations and policies concerning the import, possession, or use, and re-export of encryption software, to see if this is permitted. See the
   Wassenaar Arrangement http://www.wassenaar.org/ for more information.

  Anaconda, Inc. has self-classified this software as Export Commodity Control Number (ECCN) 5D992b, which includes mass market information security software using or performing cryptographic functions with asymme
  tric algorithms. No license is required for export of this software to non-embargoed countries. In addition, the Intel(TM) Math Kernel Library contained in Anaconda, Inc.'s software is classified by Intel(TM) as
   ECCN 5D992b with no license required for export to non-embargoed countries and Microsoft's Visual Studio Code software is classified by Microsoft as ECCN 5D992.c with no license required for export to non-embar
  goed countries.

  The following packages are included in this distribution that relate to cryptography:

  Do you accept the license terms? [yes|no]
  [no] >>> yes

  Anaconda2 will now be installed into this location:
  /home/wivill/anaconda2

    - Press ENTER to confirm the location
    - Press CTRL-C to abort the installation
    - Or specify a different location below

  [/home/wivill/anaconda2] >>> /opt/python/anaconda2-5.2.0
  PREFIX=/opt/python/anaconda2-5.2.0
  installing: python-2.7.15-h1571d57_0 ...
  Python 2.7.15 :: Anaconda, Inc.
  .
  .
  .
  installing: anaconda-5.2.0-py27_3 ...
  installation finished.
  Do you wish the installer to prepend the Anaconda2 install location
  to PATH in your /home/wivill/.bashrc ? [yes|no]
  [no] >>> no

  You may wish to edit your .bashrc to prepend the Anaconda2 install location to PATH:

  export PATH=/home/wivill/anaconda2/bin:$PATH

  Thank you for installing Anaconda2!

  ===========================================================================

  Anaconda is partnered with Microsoft! Microsoft VSCode is a streamlined
  code editor with support for development operations like debugging, task
  running and version control.

  To install Visual Studio Code, you will need:
    - Administrator Privileges
    - Internet connectivity

  Visual Studio Code License: https://code.visualstudio.com/license

  Do you wish to proceed with the installation of Microsoft VSCode? [yes|no]
  >>> no

De manera resumida, para crear el módulo de ambiente, podemos utilizar el siguiente
script.

.. code-block:: bash

  #!/bin/bash

  soft=anaconda2
  version=5.2.0
  install=/opt/python
  src=/opt/src
  module_path=${install}/modulefiles/${soft}
  prefix=${install}/${soft}-${version}
  mkdir -p ${module_path}

  /bin/cat <<"#EOF#" > ${module_path}/${version}
  #%Module#####################################################################
  ## anaconda2
  set version 5.2.0
  proc ModulesHelp { } {
  puts stderr "This module enables Anaconda 2"
  puts stderr " "
  }
  module-whatis "Anaconda 2"

  set prefix /opt/python/anaconda2-${version}
  prepend-path PATH ${prefix}/bin
  prepend-path CPATH ${prefix}/include
  prepend-path LIBRARY_PATH ${prefix}/lib
  prepend-path LD_LIBRARY_PATH ${prefix}/lib
  prepend-path MANPATH ${prefix}/share/man
  #EOF#


Anaconda 3
~~~~~~~~~~

Para el caso de Anaconda 3, los pasos son similares a los de Anaconda 2. En este
caso la ruta sugerida de instalación es /opt/python/anaconda3-5.2.0.

.. code-block:: bash

  sudo bash Anaconda3-5.2.0-Linux-x86_64.sh

Para crear el módulo de ambiente, ejecutamos el siguiente script.

.. code-block:: bash

  #!/bin/bash

  soft=anaconda3
  version=5.2.0
  install=/opt/python
  src=/opt/src
  module_path=${install}/modulefiles/${soft}
  prefix=${install}/${soft}-${version}
  mkdir -p ${module_path}

  /bin/cat <<"#EOF#" > ${module_path}/${version}
  #%Module#####################################################################
  ## anaconda3
  set version 5.2.0
  proc ModulesHelp { } {
  puts stderr "This module enables Anaconda 3"
  puts stderr " "
  }
  module-whatis "Anaconda 3"

  set prefix /opt/python/anaconda3-${version}
  prepend-path PATH ${prefix}/bin
  prepend-path CPATH ${prefix}/include
  prepend-path LIBRARY_PATH ${prefix}/lib
  prepend-path LD_LIBRARY_PATH ${prefix}/lib
  prepend-path MANPATH ${prefix}/share/man
  #EOF#


.. _software-intelpython:

Módulo de ambiente Intel Python
-------------------------------

Intel Python es una distribución optimizada para ejecutarse en equipos con procesadores
Intel, ya sea utilizando bibliotecas compiladas directamente usando el compilador
desarrollado por la empresa, o usando bibliotecas optimizadas para la arquitectura.
Para descargarlo se debe ingresar la información solicitada en el siguiente
`enlace <https://software.seek.intel.com/python-distribution>`_.

Intel Python 2
~~~~~~~~~~~~~~

Para instalarlo deberemos descargar el software desde la plataforma de Intel.

Una vez descargado, descomprimimos el paquete con el programa tar y accedemos al
directorio generado.

.. code-block:: bash

  tar -xvzf l_python2_pu3_2018.3.039.tgz
  cd l_python2_pu3_2018.3.039

Una vez dentro, ejecutamos con permisos administrativos (sea con sudo o como root)
el instalador.

.. code-block:: bash

  bash install.sh

Esto ejecutará el instalador, en el cual simplemente deberemos seguir los pasos
indicados según se detalla a continuación.


.. code-block:: bash

  --------------------------------------------------------------------------------
  Initializing, please wait...
  --------------------------------------------------------------------------------

  Step 1 of 5 | Welcome
  --------------------------------------------------------------------------------
  Welcome to the Intel(R) Distribution for Python* 2.7 2018 Update 3 for Linux* OS setup program.
  --------------------------------------------------------------------------------


  You will complete the steps below during setup process:
  Step 1 : Welcome
  Step 2 : License agreement
  Step 3 : Options
  Step 4 : Installation
  Step 5 : Complete

  --------------------------------------------------------------------------------
  Press "Enter" key to continue or "q" to quit:



  Step 2 of 5 | License agreement
  --------------------------------------------------------------------------------
  To continue with the installation of this product you are required to accept
  the terms and conditions of the End User License Agreement (EULA). The EULA
  is displayed using the 'more' utility. Press the spacebar to advance to the
  next page or enter 'q' to skip to the end. After reading the EULA, you must
  enter 'accept' to continue the installation or 'decline' to return to the
  previous menu.
  --------------------------------------------------------------------------------
  Intel Simplified Software License for Intel(R) Math Kernel Library,
  Intel(R) Integrated Performance Primitives' Library,
  Intel(R) Machine Learning Scaling Library, and
  Intel(R) Distribution for Python* (version January 2017)

  Copyright (c) [2017] Intel Corporation.

  Use and Redistribution. You may use and redistribute the software (the
  'Software'), without modification, provided the following conditions are met:

  * Redistributions must reproduce the above copyright notice and the following
    terms of use in the Software and in the documentation and/or other materials
    provided with the distribution.
  * Neither the name of Intel nor the names of its suppliers may be used to
    endorse or promote products derived from this Software without specific prior
    written permission.
  * No reverse engineering, decompilation, or disassembly of this Software is
  --------------------------------------------------------------------------------
  Type "accept" to continue or "decline" to go back to the previous menu: accept
  --------------------------------------------------------------------------------
  Checking the prerequisites. It can take several minutes. Please wait...
  --------------------------------------------------------------------------------

  Step 2 of 5 | Prerequisites > Missing Optional Prerequisite(s)
  --------------------------------------------------------------------------------
  There are one or more optional unresolved issues. It is highly recommended to
  resolve them all before you continue. You can fix them without exiting the setup
  program and re-check. Or you can exit the setup program, fix them and run the
  setup program again.
  --------------------------------------------------------------------------------
  Missing optional prerequisites
  -- Unsupported OS
  --------------------------------------------------------------------------------
  1. Skip missing optional prerequisites [default]
  2. Show the detailed info about issue(s)
  3. Re-check the prerequisites

  h. Help
  b. Back to the previous menu
  q. Quit
  --------------------------------------------------------------------------------
  Please type a selection or press "Enter" to accept default choice [1]: 1


  Step 3 of 5 | Options > Pre-install Summary
  --------------------------------------------------------------------------------
  Install location:
      /opt/intel/intelpython2


  Install space required:  111MB

  --------------------------------------------------------------------------------
  1. Start installation Now [default]
  2. Customize installation

  h. Help
  b. Back to the previous menu
  q. Quit
  --------------------------------------------------------------------------------
  Please type a selection or press "Enter" to accept default choice [1]:
  --------------------------------------------------------------------------------
  Checking the prerequisites. It can take several minutes. Please wait...
  --------------------------------------------------------------------------------


  Step 4 of 5 | Installation
  --------------------------------------------------------------------------------
  Each component will be installed individually. If you cancel the installation,
  some components might remain on your system. This installation may take several
  minutes, depending on your system and the options you selected.
  --------------------------------------------------------------------------------
  Installing Intel(R) Distribution for Python* 2.7 2018 Update 3 component... done
  --------------------------------------------------------------------------------
  Finalizing product configuration...
  --------------------------------------------------------------------------------
  Press "Enter" key to continue


  Step 5 of 5 | Complete
  --------------------------------------------------------------------------------
  Thank you for installing and for using Intel(R) Distribution for Python* 2.7
  2018 Update 3 for Linux* OS.

  If you have not done so already, please register your product with Intel
  Registration Center https://registrationcenter.intel.com to create your support
  account and take full advantage of your product purchase.

  Your support account gives you access to free product updates and upgrades as
  well as Priority Customer support at the Online Service Center
  https://supporttickets.intel.com.

  --------------------------------------------------------------------------------
  Press "Enter" key to quit:

Una vez instalado, creamos el módulo de ambiente correspondiente.

.. code-block:: bash

  #!/bin/bash

  soft=intelpython2
  version=2.7.14
  install=/opt/intel
  src=/opt/src
  module_path=${install}/modulefiles/${soft}
  prefix=${install}/${soft}-${version}
  mkdir -p ${module_path}

  /bin/cat <<"#EOF#" > ${module_path}/${version}
  #%Module#####################################################################
  ## intelpython2
  set version 2
  proc ModulesHelp { } {
  puts stderr "This module enables Intel Python 2"
  puts stderr " "
  }
  module-whatis "Intel Python 2"

  set prefix /opt/intel/intelpython${version}
  prepend-path PATH ${prefix}/bin
  prepend-path CPATH ${prefix}/include
  prepend-path LIBRARY_PATH ${prefix}/lib
  prepend-path LD_LIBRARY_PATH ${prefix}/lib
  prepend-path MANPATH ${prefix}/share/man
  #EOF#

Intel Python 3
~~~~~~~~~~~~~~

Para instalarlo deberemos descargar el software desde la plataforma de Intel.

Una vez descargado, descomprimimos el paquete con el programa tar y accedemos al
directorio generado.

.. code-block:: bash

  tar -xvzf l_python3_pu3_2018.3.039.tgz
  cd l_python3_pu3_2018.3.039

Una vez dentro, ejecutamos con permisos administrativos (sea con sudo o como root)
el instalador.

.. code-block:: bash

  bash install.sh

Esto ejecutará el instalador, en el cual simplemente deberemos seguir los pasos
indicados. Es en general el mismo proceso que para Intel Python 2. Para generar
el módulo de ambiente, ejecutamos el siguiente script.

.. code-block:: bash

  #!/bin/bash

  soft=intelpython3
  version=3.6.3
  install=/opt/intel
  src=/opt/src
  module_path=${install}/modulefiles/${soft}
  prefix=${install}/${soft}-${version}
  mkdir -p ${module_path}

  /bin/cat <<"#EOF#" > ${module_path}/${version}
  #%Module#####################################################################
  ## intelpython3
  set version 3
  proc ModulesHelp { } {
  puts stderr "This module enables Intel Python 3"
  puts stderr " "
  }
  module-whatis "Intel Python 3"

  set prefix /opt/intel/intelpython${version}
  prepend-path PATH ${prefix}/bin
  prepend-path CPATH ${prefix}/include
  prepend-path LIBRARY_PATH ${prefix}/lib
  prepend-path LD_LIBRARY_PATH ${prefix}/lib
  prepend-path MANPATH ${prefix}/share/man
  #EOF#

.. _software-qgis_compile:

Módulo de ambiente QGIS 3.0
---------------------------

QGIS es la plataforma sobre la cual estaremos trabajando principalmente, y dado
Anaconda no provee aún la versión 3.0 debidamente empaquetada y soportada, nos
corresponde compilarlar para poder tener acceso si queremos manejarlo de manera
aislada del resto del sistema como módulo de ambiente.

Lo primero que corresponde en este caso es instalar las dependencias para poder compilar
y usar QGIS.

.. code-block:: bash

  sudo apt install libqt5xmlpatterns5-dev libgsl-dev libqscintilla2-qt5-dev ccache qt5-default libqt5svg5-dev libqt5serialport5-dev libqt5positioning5 libqt5positioning5-plugins libqt5webkit5-dev libqwt-dev libqwt-qt5-dev qttools5-dev qtdeclarative5-dev qca-qt5-2-utils libqca-qt5-2-dev qtpositioning5-dev python3-sip-dev pyqt5-dev-tools  sip-dev flex bison libgeos-dev libgdal-dev libzip-dev

Posterior a esto podemos descargar el código fuente desde el repostitorio git y
compilarlo.
