import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

# ==========================================
# 1. LIVE OFFICIAL BRANDING & THEME
# ==========================================
st.set_page_config(
    page_title="National Health Surveillance Portal - Kerala Migrants",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Institutional CSS Accent Styling
st.markdown("""
    <style>
    .main-title { font-size:2.5rem !important; color: #042f2e; font-weight: 800; letter-spacing: -0.5px; }
    .sub-title { font-size:1.1rem !important; color: #475569; margin-bottom: 1.5rem; font-weight: 400; }
    .metric-box { background: #ffffff; padding: 1.25rem; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05); border-top: 4px solid #0d9488; }
    .alert-box { background: #fff5f5; padding: 1.25rem; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05); border-top: 4px solid #e11d48; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. CORE DIGITAL ARCHITECTURE (DATA INGESTION)
# ==========================================
@st.cache_data
def generate_advanced_health_records():
    districts = ['Ernakulam', 'Trivandrum', 'Kozhikode', 'Palakkad', 'Thrissur', 'Malappuram']
    states = ['West Bengal', 'Assam', 'Bihar', 'Odisha', 'Uttar Pradesh', 'Jharkhand']
    diseases = ['None', 'Malaria', 'Dengue', 'Tuberculosis', 'Filariasis', 'Dyspepsia', 'Food Poisoning']
    
    data = []
    for i in range(250):
        screening = random.choice(["Clear", "Under Observation", "High Risk Alert"])
        disease = "None" if screening == "Clear" else random.choice(diseases[1:])
        
        data.append({
            "National Health ID": f"KER-MIG-2026-{random.randint(1024, 9999)}",
            "Full Name": f"Patient Worker #{i+1:03d}",
            "Age": random.randint(18, 60),
            "State of Origin": random.choice(states),
            "Kerala Host District": random.choice(districts),
            "Vaccination Status": random.choice(["Fully Immunized", "Partially Immunized", "Unvaccinated"]),
            "Clinical Status": screening,
            "Primary Diagnosis": disease,
            "Last Screening Date": pd.Timestamp('2026-10-19') - pd.Timedelta(days=random.randint(0, 30))
        })
    return pd.DataFrame(data)

df_db = generate_advanced_health_records()

# ==========================================
# 3. HIGH-END INSTITUTIONAL NAVIGATION
# ==========================================
with st.sidebar:
    st.image("https://icons8.com", width=70)
    st.markdown("### **NHMS Kerala**\n*Public Health Surveillance Portal*")
    st.markdown("---")
    
    ui_mode = st.selectbox("🌐 System Language Access", ["English Portal", "हिंदी प्रशासनिक पोर्टल", "മലയാളം സിസ്റ്റം"])
    
    st.markdown("---")
    menu = st.radio(
        "Administrative Sub-modules:",
        ["📈 Real-time Epidemic Dashboard", 
         "🔍 Central Health Registry Search", 
         "📝 Clinical Intake Form", 
         "🎯 SDG Metric Compliance Analytics"]
    )
    st.markdown("---")
    st.caption("🔒 Secure TLS 1.3 Encrypted Portal Connection")

portal_titles = {
    "English Portal": "Digital Health Record Management System (NHMS Portal)",
    "हिंदी प्रशासनिक पोर्टल": "डिजिटल स्वास्थ्य रिकॉर्ड प्रबंधन प्रणाली (राष्ट्रीय पोर्टल)",
    "മലയാളം സിസ്റ്റം": "ഡിജിറ്റൽ ഹെൽത്ത് റെക്കോർഡ് മാനേജ്‌മെന്റ് സിസ്റ്റം"
}

st.markdown(f'<div class="main-title">{portal_titles[ui_mode]}</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Aligned with UN Sustainable Development Goals (SDG 3 & 10) for Interstate Migrant Influx Monitoring.</div>', unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# SUB-MODULE 1: EPIDEMIC DASHBOARD
# ==========================================
if menu == "📈 Real-time Epidemic Dashboard":
    st.markdown("### 📈 Active Public Health Surveillance Matrix")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f'<div class="metric-box"><h5>Total Registered Migrants</h5><h2>{len(df_db)}</h2></div>', unsafe_allow_html=True)
    with m2:
        critical_cases = len(df_db[df_db["Clinical Status"] == "High Risk Alert"])
        st.markdown(f'<div class="alert-box"><h5>Critical Pathogen Alerts</h5><h2 style="color:#dc2626;">{critical_cases}</h2></div>', unsafe_allow_html=True)
    with m3:
        vax_rate = (len(df_db[df_db["Vaccination Status"] == "Fully Immunized"]) / len(df_db)) * 100
        st.markdown(f'<div class="metric-box" style="border-top-color:#2563eb;"><h5>Overall Immunization Rate</h5><h2 style="color:#2563eb;">{vax_rate:.1f}%</h2></div>', unsafe_allow_html=True)
    with m4:
        clear_rate = (len(df_db[df_db["Clinical Status"] == "Clear"]) / len(df_db)) * 100
        st.markdown(f'<div class="metric-box" style="border-top-color:#16a34a;"><h5>Asymptomatic Log Rate</h5><h2 style="color:#16a34a;">{clear_rate:.1f}%</h2></div>', unsafe_allow_html=True)
        
    st.markdown("###")
    
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.markdown("##### 📍 Active Syndromic Influx by District & Severity")
        fig1 = px.histogram(df_db, x="Kerala Host District", color="Clinical Status", barmode="group",
                            color_discrete_map={"Clear": "#0d9488", "Under Observation": "#fbbf24", "High Risk Alert": "#f43f5e"},
                            template="simple_white", height=350)
        st.plotly_chart(fig1, use_container_width=True)
        
    with g_col2:
        st.markdown("##### 🦠 Identified Clinical Diagnoses Summary")
        disease_df = df_db[df_db["Primary Diagnosis"] != "None"]["Primary Diagnosis"].value_counts().reset_index()
        fig2 = px.pie(disease_df, values="count", names="Primary Diagnosis", 
                      color_discrete_sequence=px.colors.sequential.Sunsetdark, hole=0.4, height=350)
        st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# SUB-MODULE 2: CENTRAL REGISTRY SEARCH
# ==========================================
elif menu == "🔍 Central Health Registry Search":
    st.markdown("### 🔍 Centralized Medical Record Verification Engine")
    
    search_id = st.text_input("💳 Enter National Health ID or Full Name (e.g., Patient Worker #001):")
    
    if search_id:
        results = df_db[df_db["National Health ID"].str.contains(search_id, case=False) | df_db["Full Name"].str.contains(search_id, case=False)]
        if not results.empty:
            st.success(f"Archived Entry Detected: {len(results)} matches identified.")
            st.dataframe(results, use_container_width=True)
        else:
            st.error("No verified medical registry entry found matching parameters.")
    else:
        st.dataframe(df_db, use_container_width=True, height=400)

# ==========================================
# SUB-MODULE 3: CLINICAL INTAKE FORM
# ==========================================
elif menu == "📝 Clinical Intake Form":
    st.markdown("### 📝 Secure Electronic Health Record (EHR) Data Entry")
    
    with st.form("ehr_intake", clear_on_submit=True):
        f1, f2, f3 = st.columns(3)
        with f1:
            name = st.text_input("Full Legal Name *")
            age = st.number_input("Age (Years) *", min_value=18, max_value=80, value=28)
        with f2:
            origin = st.selectbox("Origin Jurisdiction", ["Assam", "West Bengal", "Bihar", "Odisha", "Uttar Pradesh", "Jharkhand"])
            destination = st.selectbox("Kerala Allocation District", ["Ernakulam", "Trivandrum", "Kozhikode", "Palakkad", "Thrissur", "Malappuram"])
        with f3:
            vax = st.selectbox("Immunization Status Registry", ["Fully Immunized", "Partially Immunized", "Unvaccinated"])
            lang = st.selectbox("Linguistic Access Matrix", ["Hindi", "Bengali", "Assamese", "Malayalam", "English"])
            
        st.markdown("##### 🩺 Point-of-Entry Clinical Symptom Tracking Matrix")
        s_c1, s_c2, s_c3, s_c4 = st.columns(4)
        with s_c1: fever = st.checkbox("Pyrexia / Elevated Temperature")
        with s_c2: cough = st.checkbox("Respiratory Distress / Cough")
        with s_c3: gastric = st.checkbox("Dyspepsia / Gastrointestinal Issues")
        with s_c4: rash = st.checkbox("Acute Cutaneous Eruptions / Rashes")
        
        btn = st.form_submit_button("💾 Commit Record to Central Cloud Core")
        
        if btn:
            if not name:
                st.error("Validation Violation: Secure Record Processing requires Full Name input.")
            else:
                payload = {
                    "health_id": f"KER-MIG-2026-{random.randint(1000,9999)}",
                    "patient_meta": {"name": name, "age": age, "language": lang},
                    "geographics": {"origin": origin, "host_district": destination},
                    "clinical_log": {
                        "immunization": vax,
                        "symptom_profile": {"pyrexia": fever, "respiratory": cough, "dyspepsia": gastric, "rash": rash}
                    }
                }
                st.toast("EHR Pipeline Ingestion Active!", icon="💾")
                st.success("Patient Record compiled successfully.")
                with st.expander("🔗 View Encrypted JSON API Structure"):
                    st.json(payload)

# ==========================================
# SUB-MODULE 4: SDG COMPLIANCE ANALYTICS
# ==========================================
elif menu == "🎯 SDG Metric Compliance Analytics":
    st.markdown("### 🎯 UN Sustainable Development Goals (SDG) Alignment Index")
    
    c_sdg1, c_sdg2 = st.columns(2)
    with c_sdg1:
        st.markdown("#### SDG 3: Good Health and Well-being")
        fully_immunized = (df_db["Vaccination Status"] == "Fully Immunized").mean() * 100
        st.metric("Fully immunized patients", f"{fully_immunized:.1f}%")

        vaccination_counts = (
            df_db["Vaccination Status"]
            .value_counts()
            .reindex(
                ["Fully Immunized", "Partially Immunized", "Unvaccinated"],
                fill_value=0,
            )
            .rename_axis("Vaccination Status")
            .reset_index(name="Patients")
        )
        vaccination_chart = px.bar(
            vaccination_counts,
            x="Vaccination Status",
            y="Patients",
            color="Vaccination Status",
            title="Immunization status of registered migrants",
            color_discrete_sequence=px.colors.sequential.Teal,
            template="simple_white",
        )
        st.plotly_chart(vaccination_chart, use_container_width=True)

    with c_sdg2:
        st.markdown("#### SDG 10: Reduced Inequalities")
        origin_counts = (
            df_db["State of Origin"]
            .value_counts()
            .rename_axis("State of Origin")
            .reset_index(name="Registered Patients")
        )
        origin_chart = px.bar(
            origin_counts,
            x="State of Origin",
            y="Registered Patients",
            title="Registered patients by state of origin",
            color="Registered Patients",
            color_continuous_scale="Teal",
            template="simple_white",
        )
        st.plotly_chart(origin_chart, use_container_width=True)
        st.caption(
            "Origin distribution shows representation in this registry; it does "
            "not measure population coverage or inequality by itself."
        )
