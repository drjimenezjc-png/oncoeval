# 🩺 OncoEval Pro: Sistema de Valoración Oncológica

Aplicación clínica basada en Python (Streamlit) para estandarizar la evaluación de candidatos a tratamiento oncoespecífico, integrando variables funcionales, moleculares y de seguridad farmacológica.

## 🎯 Objetivo Clínico
Automatizar y estructurar el juicio clínico oncológico generando un informe estandarizado que evalúa el riesgo/beneficio de administrar terapias citotóxicas, inmunoterapia o terapias dirigidas, facilitando la toma de decisiones en el Comité de Tumores.

## 🧬 Fases de Valoración Integradas

| Fase | Herramienta/Criterio | Objetivo Clínico |
| :--- | :--- | :--- |
| **I. Funcional** | ECOG Performance Status | Determinar elegibilidad para terapias citotóxicas. |
| **II. Molecular** | NGS (Panel Sólido/Mieloide) | Identificar dianas terapéuticas (Targetable mutations). |
| **III. Inmunológica** | PD-L1, MSI, TMB | Estratificación para I/O (Checkpoint inhibitors). |
| **IV. Dinámica** | Criterios iRECIST | Diferenciar pseudoprogresión de progresión verdadera. |
| **V. Calidad de Vida**| EORTC QLQ-C30 | Integrar la perspectiva del paciente (PROs). |

## 🚀 Instalación y Despliegue (Web/App)

Este proyecto está diseñado para desplegarse como una **PWA (Progressive Web App)** a través de Streamlit Cloud, permitiendo a los facultativos usarlo desde cualquier dispositivo sin instalar software local.

1. Haz un fork o clona este repositorio.
2. Vincula el repositorio en [Streamlit Community Cloud](https://share.streamlit.io).
3. Selecciona el archivo `app.py` como punto de entrada.
4. Despliega la aplicación.

**Librerías requeridas:**
Ver archivo `requirements.txt`. Principalmente requiere `streamlit` y `pandas`.

## 📋 Estructura del Informe Generado

El sistema genera una plantilla lista para copiar a la Historia Clínica Electrónica con los siguientes apartados:
1. Resumen Clínico (Edad, Diagnóstico, Motivo, Perfil Molecular)
2. Juicio de Fragilidad (ECOG)
3. Análisis de Seguridad (Hepática, Renal, Hematológica)
4. Recomendación Basada en Evidencia (Apto, Ajuste de Dosis, Cuidados Paliativos)
5. Plan de Seguimiento

---
*Aviso Legal: Esta herramienta es un apoyo a la decisión clínica y no sustituye el criterio médico del especialista.*
