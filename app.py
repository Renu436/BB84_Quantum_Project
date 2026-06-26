import streamlit as st
import matplotlib.pyplot as plt
from core.bb84_qiskit import run_bb84
from core.error_analysis import calculate_error_rate
from feature_engineering import extract_features

# Page setup
st.set_page_config(page_title="Quantum Secure System", layout="wide")

# Header
st.markdown(
    "<h1 style='text-align:center;color:#00ADB5;'>🔐 Quantum Cryptography (BB84)</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# Input section
col1, col2 = st.columns(2)

with col1:
    n = st.slider("🔢 Number of Qubits", 50, 200, 200)

with col2:
    attack = st.toggle("⚠️ Simulate Eavesdropping Attack")

# Run button
if st.button("🚀 Run Simulation"):

    # Run BB84
    a, b = run_bb84(n, attack)
    err = calculate_error_rate(a, b)

    st.markdown("## 📊 Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("🔑 Key Length", len(a))
    col2.metric("⚠️ Error Rate", round(err, 4))
    col3.metric("📡 Status", "Secure" if err < 0.1 else "Attack")

    # Status message
    if err < 0.1:
        st.success("🟢 Secure Communication Established (Low Error Rate)")
    else:
        st.error("🔴 Eavesdropping Attack Detected (High Error Rate)")

    st.markdown("---")

    # Feature display
    st.subheader("🧠 Extracted Features")

    features = extract_features(err, len(a))

    st.json({
        "error_rate": round(features[0], 4),
        "key_length": features[1],
        "mismatch": round(features[2], 2),
        "noise": round(features[3], 4),
        "stability": round(features[4], 4)
    })

    st.markdown("---")

    # Visualization
    st.subheader("📈 Key Comparison (Alice vs Bob)")

    fig, ax = plt.subplots()

    ax.plot(a, label="Alice Key", linewidth=2)
    ax.plot(b, label="Bob Key", linestyle="dashed")

    ax.set_xlabel("Bit Index")
    ax.set_ylabel("Bit Value")
    ax.set_title("Quantum Key Distribution Result")

    ax.legend()

    st.pyplot(fig)

    st.markdown("---")

    # Explanation section (helps in viva/demo)
    st.subheader("📘 Interpretation")

    if err < 0.1:
        st.info(
            "Low error rate indicates that no eavesdropping occurred. "
            "The quantum channel is secure."
        )
    else:
        st.warning(
            "High error rate indicates disturbance in quantum states, "
            "likely due to eavesdropping."
        )