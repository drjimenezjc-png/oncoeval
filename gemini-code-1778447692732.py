import streamlit as st

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA (Para móvil)
# ==========================================
st.set_page_config(
    page_title="OncoEval",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo personalizado para parecer más una App
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
        background-color: #2e7b32;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🩺 OncoEval")
st.markdown("---")

# ==========================================
# INTERFAZ DE ENTRADA
# ==========================================
st.subheader("Datos del Paciente")
nombre = st.text_input("Nombre / Iniciales (Por privacidad)")
edad = st.number_input("Edad", min_value=18, max_value=120, value=60, step=1)

st.subheader("Perfil Clínico")
diagnostico = st.text_input("Diagnóstico principal")
estadio = st.selectbox("Estadio", ["I", "II", "III", "IV"])

# Slider para ECOG
st.markdown("**Escala ECOG**")
ecog = st.slider("Nivel de rendimiento (0: Totalmente activo, 4: Encamado)", 0, 4, 0)

# Comorbilidades
opciones_comorbilidades = [
    "Hipertensión Arterial", 
    "Diabetes Mellitus", 
    "EPOC", 
    "Cardiopatía Isquémica", 
    "Insuficiencia Renal", 
    "Hepatopatía"
]
comorbilidades = st.multiselect("Comorbilidades (Selecciona múltiples)", opciones_comorbilidades)

st.markdown("---")

# ==========================================
# LÓGICA Y GENERACIÓN DEL INFORME
# ==========================================
if st.button("Generar Informe de Valoración"):
    if not diagnostico:
        st.warning("⚠️ Por favor, introduce un diagnóstico para continuar.")
    else:
        # Lógica del algoritmo
        apto = False
        justificaciones = []

        if ecog <= 2:
            justificaciones.append("✅ Buen estado funcional (ECOG 0-2). Tolerancia previsible a la toxicidad.")
            aprobado_ecog = True
        else:
            justificaciones.append("❌ Estado funcional deteriorado (ECOG > 2). Alto riesgo de complicaciones severas.")
            aprobado_ecog = False

        if edad >= 75:
            justificaciones.append("⚠️ Edad avanzada (≥75): Se recomienda valoración geriátrica integral simultánea.")
        
        if len(comorbilidades) >= 2:
            justificaciones.append(f"⚠️ Múltiples comorbilidades ({len(comorbilidades)}): Requiere ajuste de dosis y monitoreo estricto.")

        # Decisión final
        if aprobado_ecog:
            apto = True
            estado_final = "CANDIDATO VIABLE"
            color_alerta = "success"
            recomendacion = "APTO para inicio o valoración de tratamiento oncoespecífico activo."
        else:
            estado_final = "NO CANDIDATO (Soporte)"
            color_alerta = "error"
            recomendacion = "Se recomienda priorizar tratamiento de soporte (Best Supportive Care) / Cuidados Paliativos."

        # Mostrar Resultados (La "Pantalla" de Informe)
        st.markdown("## 📋 Informe de Valoración")
        
        if color_alerta == "success":
            st.success(f"**{estado_final}**: {recomendacion}")
        else:
            st.error(f"**{estado_final}**: {recomendacion}")

        st.markdown("### Justificación Clínica:")
        for just in justificaciones:
            st.markdown(f"- {just}")
            
        st.markdown("### Resumen de Datos:")
        st.text(f"Paciente: {nombre if nombre else 'Anónimo'} ({edad} años)\n"
                f"Diagnóstico: {diagnostico} (Estadio {estadio})\n"
                f"ECOG: {ecog}\n"
                f"Antecedentes: {', '.join(comorbilidades) if comorbilidades else 'Ninguno destacado'}")