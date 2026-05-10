import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="OncoEval Pro", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; height: 50px; font-weight: bold; background-color: #2e7b32; color: white; }
    .report-box { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7b32; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# PANEL LATERAL: FASES DE VALORACIÓN (Referencia Clínica)
# ==========================================
with st.sidebar:
    st.header("📚 Fases de Valoración")
    st.markdown("Criterios integrados en el sistema:")
    
    fases_data = {
        "Fase": ["I. Funcional", "II. Molecular", "III. Inmunológica", "IV. Dinámica", "V. Calidad de Vida"],
        "Criterio": ["ECOG", "NGS", "PD-L1, MSI, TMB", "iRECIST", "EORTC QLQ-C30"],
        "Objetivo": ["Elegibilidad citotóxica", "Dianas terapéuticas", "Estratificación I/O", "Diferenciar pseudoprogresión", "Integrar PROs"]
    }
    st.dataframe(pd.DataFrame(fases_data), hide_index=True)

# ==========================================
# INTERFAZ PRINCIPAL DE ENTRADA
# ==========================================
st.title("🩺 OncoEval Pro")
st.markdown("**Sistema de Valoración de Candidatos a Tratamiento Oncoespecífico**")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    edad = st.number_input("Edad", min_value=18, max_value=120, value=65)
    motivo = st.text_input("Motivo de ingreso", value="Progresión tumoral / Deterioro")
with col2:
    diagnostico = st.text_input("Diagnóstico", value="Cáncer de Pulmón No Microcítico")
    biomarcadores = st.text_input("Biomarcadores (NGS/Inmuno)", value="EGFR mutado, PD-L1 <1%")

st.markdown("### Juicio de Fragilidad")
ecog = st.slider("Escala ECOG", 0, 4, 1)

st.markdown("### Análisis de Seguridad")
col3, col4, col5 = st.columns(3)
with col3:
    seg_hema = st.selectbox("Seguridad Hematológica", ["Apto", "No Apto"])
with col4:
    seg_renal_hep = st.selectbox("Seguridad Renal/Hepática", ["Apto", "Ajustar dosis", "Contraindicado"])
with col5:
    complicaciones = st.selectbox("Complicaciones agudas", ["Resueltas", "En curso"])

st.markdown("### Evidencia y Seguimiento")
col6, col7 = st.columns(2)
with col6:
    guias = st.selectbox("Guía de referencia", ["ESMO", "NCCN", "ASCO", "SEOM"])
    hr_esperado = st.text_input("Beneficio esperado (Ej: HR 0.75 para OS)", value="HR: 0.80")
with col7:
    plan_seguimiento = st.text_input("Plan de Seguimiento", value="Reevaluar en 48h")

st.markdown("---")

# ==========================================
# LÓGICA Y GENERACIÓN DEL INFORME
# ==========================================
if st.button("Generar Informe Clínico Completo"):
    
    # 1. Lógica de Fragilidad
    texto_fragilidad = f"El paciente presenta un ECOG {ecog}."
    if ecog > 2:
        texto_fragilidad += " Se considera situación de alta fragilidad que limita el uso de quimioterapia citotóxica estándar."

    # 2. Lógica de Candidatura Automática
    candidato_plenas = "[ ]"
    candidato_rest = "[ ]"
    no_candidato = "[ ]"
    
    if ecog > 2 or seg_hema == "No Apto" or seg_renal_hep == "Contraindicado" or complicaciones == "En curso":
        no_candidato = "[X]"
    elif seg_renal_hep == "Ajustar dosis":
        candidato_rest = "[X]"
    else:
        candidato_plenas = "[X]"

    # 3. Construcción de la Plantilla
    informe = f"""
<div class="report-box">
<b>1. Resumen Clínico:</b> Paciente de {edad} años con {diagnostico} ingresado por {motivo}. Presenta un perfil molecular: {biomarcadores}.<br><br>

<b>2. Juicio de Fragilidad:</b> {texto_fragilidad}<br><br>

<b>3. Análisis de Seguridad:</b><br>
&nbsp;&nbsp;&nbsp;• Hematológica: {seg_hema}<br>
&nbsp;&nbsp;&nbsp;• Renal/Hepática: {seg_renal_hep}<br>
&nbsp;&nbsp;&nbsp;• Complicaciones agudas: {complicaciones}<br><br>

<b>4. Recomendación Basada en Evidencia:</b> Según guías {guias}, y considerando el beneficio clínico esperado ({hr_esperado}), el paciente:<br><br>
&nbsp;&nbsp;{candidato_plenas} ES CANDIDATO a tratamiento a dosis plenas.<br>
&nbsp;&nbsp;{candidato_rest} ES CANDIDATO CON RESTRICCIONES (Reducción de dosis al 25-50% o monoterapia).<br>
&nbsp;&nbsp;{no_candidato} NO ES CANDIDATO ACTUALMENTE: Priorizar Mejor Tratamiento de Soporte (BSC) y reevaluar tras mejoría.<br><br>

<b>5. Plan de Seguimiento:</b> {plan_seguimiento}
</div>
    """
    
    st.markdown("## 📋 Informe Generado")
    st.markdown(informe, unsafe_allow_html=True)
    st.info("💡 Consejo: Puedes copiar este texto directamente a la historia clínica electrónica del paciente.")
