![Banner PTI Clima](aux/Banner-logos-PTIClima-ProyectoServiciosAEMET.png)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SantanderMetGroup/PTI-Clima-Datalab/HEAD?labpath=README.md) [![IFCA](https://img.shields.io/badge/launch-IFCA-orange)](https://hub.climate.ifca.es/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FSantanderMetGroup%2FPTI-Clima-Datalab&urlpath=lab%2Ftree%2FPTI-Clima-Datalab%2Fprimeros_pasos_R.ipynb&branch=main)

# DataLab de la Plataforma Estatal de Servicios Climáticos 

El Datalab de la Plataforma Estatal de Servicios Climáticos ([https://plataforma-clima.aemet.es](https://plataforma-clima.aemet.es)) complementa el **[almacén de datos](https://pti.climate.ifca.es/almacen-datos) de la Plataforma** proporcionando un entorno abierto para el procesamiento y análisis transparente de datos climáticos. Basado en **Jupyter Notebooks** y con soporte para R y Python, promueve la ciencia abierta, la reproducibilidad y la reutilización de datos y software, facilitando que los resultados del proyecto puedan ser utilizados, revisados y ampliados por la comunidad. 

Los notebooks disponibles pueden consultarse en la sección de **[Notebooks del repositorio](https://github.com/SantanderMetGroup/PTI-Clima-Datalab/tree/main/Notebooks/R)**. Estos proporcionan ejemplos reproducibles para generar algunos de los productos de la Plataforma, incluyendo el cálculo de índices climáticos (véase, por ejemplo, el notebook para el cálculo del [índice SPEI-3](https://github.com/SantanderMetGroup/PTI-Clima-Datalab/blob/main/Notebooks/R/calculo_indices_SPEI-3_R.ipynb)).


El DataLab se alinea con desarrollos previous realizados en iniciativas como el [IPCC Atlas DataLab](https://doi.org/10.1371/journal.pclm.0000644) y su contenido se distribuye bajo la licencia abierta [CC BY 4.0](http://creativecommons.org/licenses/by/4.0) que permite reutilizar toda la información.

![Licencia de Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)

## Infraestructura Disponible y Modos de Uso

Existen distintos modos de uso del DataLab dependiendo del grado de experiencia y del acceso a recursos: 
- Ejecución en la nube mediante MyBinder, utilizando la infraestructura proporcionada por la inicitiva [MyBinder](https://mybinder.org) que proporcina de forma gratuita recursos limitados. Este modo permite explorar el DataLab y realizar cálculos sencillos que no requieran muchos recursos.
- Ejecución en la nube en recursos de la Plataforma, utilizando recursos limitados que ofrece la Plataforma a través del CSIC. Este modo ofrece recursos más avanzados pero requiere solicitud de acceso.
- Ejecución local en un equipo propio, para usuarios avanzados, permitiendo instalar el entorno el local con acceso remoto a los datos.

| | Modalidad | Requiere instalación local | Requiere autorización | Uso recomendado |
|---|---|---:|---:|---|
| 1 | MyBinder | No | No | Exploración rápida y uso general |
| 2 | Plataforma-CSIC | No | Sí | Trabajo con recursos computacionales restringidos |
| 3 | Local | Sí | No | Trabajo persistente, desarrollo y adaptación de los análisis |

### 1. Uso libre a través de MyBinder

El DataLab está disponible para el público general a través de **MyBinder**, lo que permite ejecutar los notebooks directamente desde el navegador sin necesidad de instalar software adicional. Para utilizar esta opción, basta con pulsar el botón **launch binder** disponible al inicio de este README. MyBinder creará un entorno temporal con las dependencias necesarias y abrirá el repositorio en una sesión de JupyterLab (la inicialización del servicio puede llevar unos minutos).

> **Nota:** las sesiones de MyBinder son temporales. Los cambios realizados durante la sesión pueden perderse al cerrarla, por lo que se recomienda descargar cualquier notebook o resultado que se quiera conservar.

### 2. Uso de los recursos de la Plataforma-CSIC, bajo solicitud de acceso

De forma análoga al caso anterior, el DataLab se puede ejecutar directamente desde un navegador sin necesidad de instalar software adicional a través de los recursos proporcionados por la Plataforma (a través del Instituto de Física de Cantabria, IFCA-CSIC). Estos recursos son limitados y es neceario solicitar acceso en _buzonplataformaclima@aemet.es_, indicando la motivación de uso. El acceso se prioriza en función de los objetivos, priorizando el soporte a proyectos de investigación y actividades de Ciencia Abierta. 

Una vez obtenida la autorizacion se puede utilizar el botón **launch IFCA** disponible al inicio de este README. Este enlace redirige al entorno JupyterHub del IFCA y clona automáticamente el repositorio para facilitar el acceso a los cuadernos y materiales del Datalab.

### 3. Uso local en un equipo propio

También es posible ejecutar el DataLab en un equipo propio. Esta opción requiere un conocimiento técnico avanzado con experiencia en entornos de desarrollo y es recomendable para quienes quieran trabajar de forma persistente, modificar los notebooks, guardar resultados o adaptar el entorno a sus propias necesidades. Los pasos a seguir para instalar el DataLab en local se detallan a continuación.

#### Clonar el repositorio

```bash
git clone https://github.com/SantanderMetGroup/PTI-Clima-Datalab.git
cd PTI-Clima-Datalab
```

#### Crear el entorno de trabajo

El entorno del DataLab puede recrearse localmente utilizando el fichero de dependencias incluido en el repositorio:

```bash
.binder/environment.yml
```

Se recomienda el uso de [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) para instalar las dependencias:

```bash
mamba env create -n datalab -f .binder/environment.yml
```

#### Activar el entorno

```bash
mamba activate datalab
```

#### Instalar e iniciar JupyterLab en el entorno creado

```bash
mamba install -c conda-forge jupyterlab
jupyter lab
```

Usuarios avanzados que utilicen GitHub Codespace también pueden lanzar el DataLab en este entorno:
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/SantanderMetGroup/PTI-Clima-Datalab?quickstart=1)

## Entornos de Análisis Disponibles

<p align="left">
  <img src="https://raw.githubusercontent.com/SantanderMetGroup/climate4R/main/man/figures/climate4R_logo.svg" alt="Logo climate4R" width="100">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Logo Python" width="240">
</p>

Los flujos de trabajo incluidos en los notebooks de este Datalab se basan principalmente en el entorno de programación [climate4R](https://github.com/SantanderMetGroup/climate4R), un conjunto de librerías desarrolladas en **R** para la carga, el postprocesamiento, el análisis y la visualización de datos climáticos.


Para las personas usuarias que prefieran trabajar con **Python**, el Datalab también dispone de un entorno basado en **Python 3**. No obstante, es importante señalar que, en este caso, el software preinstalado es más básico que el disponible en el entorno de R.
