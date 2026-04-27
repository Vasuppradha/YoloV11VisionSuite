import streamlit as st

# Page configuration
st.set_page_config(
    page_title="YOLOv11 Vision Suite",
    layout="wide"
)

# Custom CSS (Compact Cards)
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 45px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        font-size: 16px;
        color: #b0b0b0;
        margin-bottom: 20px;
    }
    .card {
        background: #111827;
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        height: 170px;
        box-shadow: 0 0 15px rgba(0,0,0,0.4);
        transition: 0.25s;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 25px rgba(99,102,241,0.5);
    }
    .card h3 {
        margin-bottom: 6px;
        font-size: 25px;
    }
    .card p {
        font-size: 14px;
        color: #c7c7c7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Session state
if "current_app" not in st.session_state:
    st.session_state.current_app = None

# HOME DASHBOARD (NO SCROLL)
if st.session_state.current_app is None:

    st.markdown("<div class='title'>🚀 YOLOv11 Vision Suite</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Real-time AI Computer Vision Applications</div>",
        unsafe_allow_html=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    # -------- Row 1 (3 Cards) --------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>⚽ Football Analysis System</h3>
                <p>Player, ball & team tracking</p>
            </div>
            """,
            unsafe_allow_html=True
        ) 
        if st.button("Launch ⚽", key="football"):
            st.session_state.current_app = "football"
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🌿 Plant Classification</h3>
                <p>Object Classification</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch 🌿", key="plant"):
            st.session_state.current_app = "classification"
            st.rerun()

    with col3:
        st.markdown(
            """
            <div class="card">
                <h3>🚗 Car Parts Segmentation</h3>
                <p>Segmentation</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch 🚗", key="segmentation"):
            st.session_state.current_app = "segmentation"
            st.rerun()

    st.write("")

    # -------- Row 2 (3 Cards) --------
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(
            """
            <div class="card">
                <h3>🧍 Human Pose Estimation</h3>
                <p>Pose Estimation</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch 🧍", key="pose"):
            st.session_state.current_app = "pose"
            st.rerun()

    with col5:
        st.markdown(
            """
            <div class="card">
                <h3>🦁 Wildlife Detection</h3>
                <p>Object Detection</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch 🦁", key="wildlife"):
            st.session_state.current_app = "detection"
            st.rerun()

    with col6:
        st.markdown(
            """
            <div class="card">
                <h3>🚘 Motion Tracking</h3>
                <p>Object Tracking</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch 🚘", key="tracking"):
            st.session_state.current_app = "tracking"
            st.rerun()


# ROUTER (UNCHANGED)
else:
    app = st.session_state.current_app 

    if app == "pose":
        from Modules.Pose_Estimation.app import run
        run()

    elif app == "detection":
        from Modules.Object_Detection.app import run
        run()

    elif app == "tracking":
        from Modules.Object_Tracking.app import run
        run()

    elif app == "classification":
        from Modules.Classification.app import run
        run()

    elif app == "segmentation":
        from Modules.Segmentation.app import run
        run()

    elif app == "football":
        from Modules.FootballAnalysisSystem.app import run
        run()




