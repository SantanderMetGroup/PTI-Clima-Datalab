![Banner PTI Clima](aux/Banner-logos-PTIClima-ProyectoServiciosAEMET.png)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/SantanderMetGroup/PTI-Clima-Datalab?quickstart=1)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SantanderMetGroup/PTI-Clima-Datalab/HEAD?labpath=README.md) [![IFCA](https://img.shields.io/badge/launch-IFCA-orange)](https://hub.climate.ifca.es/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FSantanderMetGroup%2FPTI-Clima-Datalab&urlpath=lab%2Ftree%2FPTI-Clima-Datalab%2Fprimeros_pasos_R.ipynb&branch=main)


# Datalab de la Plataforma Estatal de Servicios Climáticos 
Datalab para acceder, procesar y analizar los datos climatológicos regionalizados provenientes del almacén de datos de los servicios climáticos desarrollados por la PTI-Clima.

Los cuadernos (Jupyter Notebooks) incluidos en este Datalab muestran ejemplos prácticos para utilizar, transformar y visualizar los conjuntos de datos disponibles en el [almacén de datos](https://pti.climate.ifca.es/data) de la Plataforma Estatal de Servicios Climáticos.

Salvo que se indique lo contrario, el contenido de este repositorio se distribuye bajo la [Licencia Creative Commons Atribución 4.0 Internacional](http://creativecommons.org/licenses/by/4.0).
![Licencia de Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)

## Objetivo y Motivación

El Datalab de la Plataforma Estatal de Servicios Climáticos ofrece un entorno interactivo de análisis diseñado para respaldar la **reproducibilidad**, la **transparencia** y la **reutilización** de los datos que sustentan la [Plataforma Estatal de Servicios Climáticos](https://pti-clima.csic.es/servicios-climaticos/).

A través de una colección de **Jupyter Notebooks** y de un entorno de software preparado para trabajar con **Python** y **R**, permite acceder a datos climáticos regionalizados, procesarlos, visualizarlos y adaptar los análisis a nuevas necesidades. Gracias a esta aproximación, los datos, el código y las herramientas de análisis dejan de ser elementos aislados y pasan a formar parte de un flujo de trabajo común, trazable y reutilizable. De este modo, el Datalab de la Plataforma Estatal de Servicios facilita que los resultados del proyecto puedan ser utilizados, revisados y extendidos en beneficio de la sociedad.

## Modo de uso

El Datalab puede utilizarse de distintas formas según las necesidades de cada persona usuaria y los recursos disponibles. Se ofrecen tres modalidades principales de acceso: ejecución en la nube mediante MyBinder, uso de los recursos del IFCA y ejecución local en un equipo propio.

| | Modalidad | Requiere instalación local | Requiere autorización | Uso recomendado |
|---|---|---:|---:|---|
| 1 | MyBinder | No | No | Exploración rápida y uso general |
| 2 | IFCA | No | Sí | Trabajo con recursos computacionales restringidos |
| 3 | Local | Sí | No | Trabajo persistente, desarrollo y adaptación de los análisis |

### 1. Uso libre a través de MyBinder

El Datalab está disponible para el público general a través de **MyBinder**, lo que permite ejecutar los cuadernos directamente desde el navegador sin necesidad de instalar software adicional.

Para utilizar esta opción, basta con pulsar el botón **Binder** disponible al inicio de este README. MyBinder creará un entorno temporal con las dependencias necesarias y abrirá el repositorio en una sesión de JupyterLab.

> **Nota:** las sesiones de MyBinder son temporales. Los cambios realizados durante la sesión pueden perderse al cerrarla, por lo que se recomienda descargar cualquier notebook o resultado que se quiera conservar.

### 2. Uso de los recursos del IFCA

Las personas usuarias con autorización pueden acceder a los **recursos computacionales del Instituto de Física de Cantabria (IFCA, CSIC-UC)**.

Para ello, se puede utilizar el botón **launch IFCA** disponible al inicio de este README. Este enlace redirige al entorno JupyterHub del IFCA y clona automáticamente el repositorio para facilitar el acceso a los cuadernos y materiales del Datalab.

Esta modalidad está pensada para personas o grupos con permisos de acceso al entorno del IFCA y permite trabajar con recursos computacionales más estables.

### 3. Uso local

También es posible ejecutar el Datalab en un equipo propio. Esta opción es recomendable para quienes quieran trabajar de forma persistente, modificar los cuadernos, guardar resultados o adaptar el entorno a sus propias necesidades.

#### Clonar el repositorio

```bash
git clone https://github.com/SantanderMetGroup/PTI-Clima-Datalab.git
cd PTI-Clima-Datalab
```

#### Crear el entorno de trabajo

El entorno del Datalab puede recrearse localmente utilizando el fichero de dependencias incluido en el repositorio:

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
#### Iniciar JupyterLab

```bash
jupyter lab
```

## Entornos de análisis disponibles

<p align="left">
  <img src="https://raw.githubusercontent.com/SantanderMetGroup/climate4R/main/man/figures/climate4R_logo.svg" alt="Logo climate4R" width="100">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Logo Python" width="240">
</p>

Los flujos de trabajo incluidos en los notebooks de este Datalab se basan principalmente en el framework ***climate4R***, un conjunto de librerías desarrolladas en **R** para la carga, el postprocesamiento, el análisis y la visualización de datos climáticos.


Puede encontrarse más información sobre ***climate4R*** en el siguiente repositorio:

[https://github.com/SantanderMetGroup/climate4R](https://github.com/SantanderMetGroup/climate4R)

Para las personas usuarias que prefieran trabajar con **Python**, el Datalab también dispone de un entorno basado en **Python 3**. No obstante, es importante señalar que, en este caso, el software preinstalado es más básico que el disponible en el entorno de R.
