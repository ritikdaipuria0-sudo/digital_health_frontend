import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

# ==========================================
# 1. LIVE CYBER-CLINICAL BRANDING & THEME
# ==========================================
st.set_page_config(
    page_title="NHMS Kerala - Live Influx Surveillance",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Out-of-the-box Neon Teal Healthcare Command Center CSS Theme
st.markdown("""
    <style>
    /* Main App Background Customization */
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    
    /* Unique Headers */
    .main-title { font-size:2.4rem !important; color: #2dd4bf; font-weight: 900; letter-spacing: -0.5px; text-transform: uppercase; text-shadow: 0 0 10px rgba(45, 212, 191, 0.2); }
    .sub-title { font-size:1.05rem !important; color: #94a3b8; margin-bottom: 2rem; font-weight: 400; }
    
    /* Futuristic UI Dashboard Elements */
    .dashboard-card { background: #111827; border: 1px solid #1f2937; padding: 1.5rem; border-radius: 0.75rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); border-top: 4px solid #0d9488; }
    .alert-card { background: #1e1b4b; border: 1px solid #312e81; padding: 1.5rem; border-radius: 0.75rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); border-top: 4px solid #f43f5e; }
    
    /* Unique Treatment History Timeline Node Architecture */
    .prescription-timeline { border-left: 3px dashed #2dd4bf; padding-left: 1.5rem; margin-left: 0.5rem; position: relative; margin-bottom: 1.5rem; }
    .prescription-node { background: #111827; border: 1px solid #1f2937; padding: 1.25rem; border-radius: 0.5rem; box-shadow: 2px 4px 10px rgba(0,0,0,0.4); }
    
    /* Premium Kerala State Authority Emblem Component */
    .kerala-branding-box { background: linear-gradient(135deg, #042f2e 0%, #111827 100%); padding: 1.25rem; border-radius: 0.75rem; text-align: center; border: 1px solid #0f766e; box-shadow: 0 0 15px rgba(15, 118, 110, 0.3); margin-bottom: 2rem; }
    .kerala-emblem-text { font-size: 1.25rem !important; font-weight: 900 !important; color: #2dd4bf !important; letter-spacing: 1.5px; }
    .kerala-emblem-sub { font-size: 0.7rem !important; color: #64748b; font-weight: 700; text-transform: uppercase; margin-top: 0.2rem; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. GENERATIVE MEDICAL DATA ARCHITECTURE
# ==========================================
@st.cache_data
def generate_surveillance_data():
    districts = ['Ernakulam', 'Trivandrum', 'Kozhikode', 'Palakkad', 'Thrissur', 'Malappuram']
    states = ['West Bengal', 'Assam', 'Bihar', 'Odisha', 'Uttar Pradesh', 'Jharkhand']
    diseases = ['None', 'Malaria', 'Dengue', 'Tuberculosis', 'Filariasis', 'Dyspepsia', 'Food Poisoning']
    
    data = []
    for i in range(250):
        screening = random.choice(["Clear", "Under Observation", "High Risk Alert"])
        disease = "None" if screening == "Clear" else random.choice(diseases[1:])
        dist = random.choice(districts)
        
        data.append({
            "National Health ID": f"KER-MIG-2026-{random.randint(1024, 9999)}",
            "Contact Number": f"987654{i+1000:04d}",
            "Full Name": f"Patient Worker #{i+1:03d}",
            "Age": random.randint(18, 60),
            "State of Origin": random.choice(states),
            "Kerala Host District": dist,
            "Local Residential Address": f"Building #{random.randint(10, 200)}, Line Labor Camp, Industrial Growth Center, {dist}, Kerala",
            "Vaccination Status": random.choice(["Fully Immunized", "Partially Immunized", "Unvaccinated"]),
            "Clinical Status": screening,
            "Primary Diagnosis": disease,
            "Last Screening Date": pd.Timestamp('2026-10-20') - pd.Timedelta(days=random.randint(0, 30))
        })
    return pd.DataFrame(data)

df_db = generate_surveillance_data()

@st.cache_data
def get_longitudinal_history():
    return [
        {"Date": "12 March 2024", "Disease": "Vector-borne Malaria Infection", "Facility": "Dr. K. Raghavan (General Medicine - Ernakulam General Hospital)", "Symptoms": "High Fever with Chills, Chronic Splenomegaly, Fatigue"},
        {"Date": "22 July 2025", "Disease": "Acute Syndromic Dengue Screening", "Facility": "Dr. S. Meera (Infectious Diseases Dept - Trivandrum Medical College)", "Symptoms": "Retro-orbital Pain, Diffuse Cutaneous Rashes, Low Thrombocyte Count"},
        {"Date": "05 January 2026", "Disease": "Pulmonary Koch's (Tuberculosis) Observation", "Facility": "Dr. Paul Antony (Pulmonologist - Calicut Chest Hospital)", "Symptoms": "Hemoptysis, Persistent Productive Cough > 3 Weeks, Nocturnal Pyrexia"}
    ]

# ==========================================
# 3. SIDEBAR TECHNICAL DESIGN
# ==========================================
with st.sidebar:
    # Render Out-of-the-box UI Identity Logo Matrix
    st.markdown("""
        <div class="kerala-branding-box">
            <div style="font-size: 2rem; margin-bottom: 0.3rem; filter: drop-shadow(0 0 5px #2dd4bf);">📡</div>
            <div class="kerala-emblem-text">NHMS KERALA</div>
            <div class="kerala-emblem-sub">Syndromic Command Console</div>
        </div>
        """, unsafe_allow_html=True)
    
    ui_mode = st.selectbox("🌐 Interface Localization", ["System English Core", "प्रशासनिक हिंदी विंग", "മലയാളം കൺസോൾ"])
    st.markdown("---")
    
    menu = st.radio(
        "Surveillance Sub-modules:",
        ["🛸 Real-time Influx Analytics", 
         "👨‍⚕️ Clinical Practitioner Portal (Doctor Login)", 
         "🔍 Central Registry Metadata Search", 
         "📝 Secure EHR Registration Node", 
         "🎯 SDG Metric Compliance Tracker"]
    )
    st.markdown("---")
    st.caption("🔒 Status: Secure TLS 1.3 Communication Tunnel Active")
    st.caption("Environment: Production Cloud Web Node")

titles = {
    "System English Core": "Digital Health Record Management System (Kerala Command Portal)",
    "प्रशासनिक हिंदी विंग": "डिजिटल स्वास्थ्य रिकॉर्ड प्रबंधन प्रणाली (केरल सुरक्षा विंग)",
    "മലയാളം കൺസോൾ": "ഡിജിറ്റൽ ഹെൽത്ത് റെക്കോർഡ് മാനേജ്‌മെന്റ് സിസ്റ്റം"
}

st.markdown(f'<div class="main-title">{titles[ui_mode]}</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Advanced Data-Science Framework for Interstate Influx Disease Surveillance and Healthcare Inclusion Analytics.</div>', unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# MODULE 1: INFLUX ANALYTICS (DASHBOARD)
# ==========================================
if menu == "🛸 Real-time Influx Analytics":
    st.markdown("### 📈 Live Syndromic Surveillance Control Panel")
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown(f'<div class="dashboard-card"><h5>Total Screened Registries</h5><h2 style="color:#2dd4bf;">{len(df_db)}</h2><p style="color:#64748b; margin:0; font-size:0.8rem;">Active Influx Profiles</p></div>', unsafe_allow_html=True)
    with col_m2:
        critical = len(df_db[df_db["Clinical Status"] == "High Risk Alert"])
        st.markdown(f'<div class="alert-card"><h5>Active Isolation Alerts</h5><h2 style="color:#f43f5e;">{critical}</h2><p style="color:#94a3b8; margin:0; font-size:0.8rem;">Quarantine Orders Active</p></div>', unsafe_allow_html=True)
    with col_m3:
        vax = (len(df_db[df_db["Vaccination Status"] == "Fully Immunized"]) / len(df_db)) * 100
        st.markdown(f'<div class="dashboard-card" style="border-top-color:#3b82f6;"><h5>Overall Immunization Rate</h5><h2 style="color:#3b82f6;">{vax:.1f}%</h2><p style="color:#64748b; margin:0; font-size:0.8rem;">Herd Immunity Target: 95%</p></div>', unsafe_allow_html=True)
    with col_m4:
        clear = (len(df_db[df_db["Clinical Status"] == "Clear"]) / len(df_db)) * 100
        st.markdown(f'<div class="dashboard-card" style="border-top-color:#10b981;"><h5>EHR Health Clearance</h5><h2 style="color:#10b981;">{clear:.1f}%</h2><p style="color:#64748b; margin:0; font-size:0.8rem;">Asymptomatic Diagnostics</p></div>', unsafe_allow_html=True)
        
    st.markdown("###")
    
    g1, g2 = st.columns(2)
    with g1:
        st.markdown("##### 🗺️ Geographic Outbreak Severity Across Kerala Districts")
        fig1 = px.histogram(df_db, x="Kerala Host District", color="Clinical Status", barmode="group",
                            color_discrete_map={"Clear": "#14b8a6", "Under Observation": "#f59e0b", "High Risk Alert": "#f43f5e"},
                            height=350)
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8",
                           xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="#1f2937"))
        st.plotly_chart(fig1, use_container_width=True)
        
    with g2:
        st.markdown("##### 🦠 Vector Spectrum Classification Chart")
        disease_df = df_db[df_db["Primary Diagnosis"] != "None"]["Primary Diagnosis"].value_counts().reset_index()
        fig2 = px.pie(disease_df, values="count", names="Primary Diagnosis", 
                      color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.4, height=350)
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8")
        st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# MODULE 2: CLINICAL PRACTITIONER PORTAL (DOCTOR LOGIN)
# ==========================================
elif menu == "👨‍⚕️ Clinical Practitioner Portal (Doctor Login)":
    st.markdown("### 👨‍⚕️ Medical Officer Access Interface")
    
    if "doc_auth" not in st.session_state:
        st.session_state.doc_auth = False

    if not st.session_state.doc_auth:
        col_l, col_r = st.columns(2)
        with col_l:
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.info("🔒 Secure Portal Access Restricted to DHS Registered Clinical Practitioners.")
