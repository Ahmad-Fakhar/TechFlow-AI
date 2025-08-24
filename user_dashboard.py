import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import json

# Page config
st.set_page_config(
    page_title="TechFlow AI - Voice Commerce Revolution",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with BETTER COLORS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        padding: 0;
        max-width: 100%;
    }
    
    /* Updated color scheme - professional blue/teal */
    .hero-section {
        background: linear-gradient(135deg, #0066CC 0%, #00A8E8 100%);
        color: white;
        padding: 80px 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.2);
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 900;
        margin-bottom: 20px;
        color: white;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 24px;
        opacity: 0.95;
        margin-bottom: 30px;
    }
    
    .stat-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-top: 4px solid #00A8E8;
        transition: transform 0.3s;
        height: 100%;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .big-number {
        font-size: 48px;
        font-weight: 700;
        color: #0066CC;
        margin: 10px 0;
    }
    
    .problem-card {
        background: #FFF5F5;
        border-left: 4px solid #FF4444;
        padding: 40px;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    .solution-card {
        background: #F0FFF4;
        border-left: 4px solid #00C851;
        padding: 40px;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    .tech-card {
        background: #F8F9FA;
        border: 2px solid #0066CC;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        transition: all 0.3s;
    }
    
    .tech-card:hover {
        background: #0066CC;
        color: white;
        transform: scale(1.05);
    }
    
    .demo-section {
        background: #F8F9FA;
        padding: 60px 40px;
        border-radius: 20px;
        margin: 40px 0;
    }
    
    .cta-button {
        background: linear-gradient(135deg, #00C851 0%, #00A8E8 100%);
        color: white;
        padding: 20px 40px;
        border-radius: 50px;
        font-size: 20px;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
        text-decoration: none;
        display: inline-block;
        margin: 20px 10px;
    }
    
    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(0, 168, 232, 0.4);
    }
    
    .timeline-item {
        background: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #00A8E8;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .metric-highlight {
        background: linear-gradient(135deg, #0066CC 0%, #00A8E8 100%);
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        display: inline-block;
        font-weight: 600;
    }
    
    .whatsapp-demo {
        background: #E3F2E6;
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .sidebar .sidebar-content {
        background: #F8F9FA;
    }
    
    .stSidebar {
        background: #F8F9FA;
    }
    
    .section-divider {
        height: 2px;
        background: linear-gradient(to right, transparent, #00A8E8, transparent);
        margin: 60px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("# 🎯 TechFlow AI")
        st.markdown("### Navigation")
        
        sections = {
            "🏠 Home": "home",
            "📊 Problem": "problem", 
            "💡 Solution": "solution",
            "🚀 Live Demo": "demo",
            "🛠️ Tech Stack": "tech",
            "📈 Market": "market",
            "🎯 Impact": "impact",
            "🔮 Future": "future"
        }
        
        # Radio buttons for navigation
        selected = st.radio("Go to section:", list(sections.keys()), label_visibility="collapsed")
        
        st.markdown("---")
        st.markdown("### Quick Stats")
        st.metric("Active Demo", "Live Now 🟢")
        st.metric("Languages", "60+")
        st.metric("Response Time", "1.2s")
        
        st.markdown("---")
        st.markdown("### Contact")
        st.markdown("📧 team@techflow.ai")
        st.markdown("📱 +1 415 523 8886")
    
    # Main content - single page flow
    if selected == "🏠 Home":
        show_home()
    elif selected == "📊 Problem":
        show_problem()
    elif selected == "💡 Solution":
        show_solution()
    elif selected == "🚀 Live Demo":
        show_demo()
    elif selected == "🛠️ Tech Stack":
        show_tech_stack()
    elif selected == "📈 Market":
        show_market()
    elif selected == "🎯 Impact":
        show_impact()
    elif selected == "🔮 Future":
        show_future()

def show_home():
    """Hero landing page"""
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">TechFlow AI</h1>
        <p class="hero-subtitle">Voice Commerce for 2 Billion WhatsApp Users</p>
        <p style="font-size: 20px; margin: 30px 0;">
            Breaking language barriers in e-commerce<br>
            Shop in ANY language using voice messages
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <h3>🌍 Global Reach</h3>
            <div class="big-number">2B+</div>
            <p>WhatsApp Users</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <h3>🗣️ Languages</h3>
            <div class="big-number">60+</div>
            <p>Supported</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <h3>⚡ Speed</h3>
            <div class="big-number">1.2s</div>
            <p>Response Time</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <h3>💰 Market</h3>
            <div class="big-number">$2.8T</div>
            <p>Opportunity</p>
        </div>
        """, unsafe_allow_html=True)

def show_problem():
    """Problem statement"""
    
    st.markdown("# 📊 The $500 Billion Problem")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="problem-card">
            <h2>🚨 The Digital Divide Crisis</h2>
            <ul style="font-size: 18px; line-height: 2;">
                <li><strong>780 million people</strong> can't type efficiently</li>
                <li><strong>65% of emerging markets</strong> prefer voice over text</li>
                <li><strong>87% of small businesses</strong> lose sales due to language barriers</li>
                <li><strong>$500 billion</strong> in lost e-commerce opportunity annually</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Pie chart
        fig = go.Figure(data=[go.Pie(
            labels=['Voice Preferred', 'Text Preferred', 'Mixed'],
            values=[65, 20, 15],
            hole=.7,
            marker_colors=['#FF4444', '#FFA500', '#FFD700']
        )])
        fig.update_layout(
            title="Communication Preference",
            height=300,
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Real stories
    st.markdown("""
    <div class="solution-card">
        <h2>Real People, Real Problems</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div>
                <h4>🇵🇰 Fatima, Karachi</h4>
                <p>"I want to shop online but typing in English is hard. Voice in Urdu would be perfect."</p>
            </div>
            <div>
                <h4>🇧🇩 Rahman, Dhaka</h4>
                <p>"My mother can't type. Voice shopping would change her life."</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_solution():
    """Solution presentation"""
    
    st.markdown("# 💡 Our Solution")
    
    # How it works
    st.markdown("### How It Works - 3 Simple Steps")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card" style="text-align: center;">
            <div style="font-size: 60px;">🎤</div>
            <h3>1. Voice Message</h3>
            <p>Send voice note in ANY language on WhatsApp</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card" style="text-align: center;">
            <div style="font-size: 60px;">🤖</div>
            <h3>2. AI Processing</h3>
            <p>GPT-5 understands and processes instantly</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card" style="text-align: center;">
            <div style="font-size: 60px;">✅</div>
            <h3>3. Order Complete</h3>
            <p>Confirmation in customer's language</p>
        </div>
        """, unsafe_allow_html=True)

def show_demo():
    """Live demo section"""
    
    st.markdown("# 🚀 Live Demo")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="demo-section">
            <h2>Try It Now!</h2>
            <h3 style="color: #0066CC;">WhatsApp: +1 415 523 8886</h3>
            <p>Send: "join quite-putting" to start</p>
            
            <h3>Test Scenarios:</h3>
            <ul>
                <li>🇵🇰 "Mujhe laptop chahiye" (Urdu)</li>
                <li>🇬🇧 "Show phones under $500" (English)</li>
                <li>🇧🇩 "আমি ফোন কিনতে চাই" (Bengali)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # WhatsApp demo placeholder
        st.markdown("""
        <div class="whatsapp-demo">
            <h3>📱 WhatsApp Demo</h3>
            <p>Screenshots will appear here</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Placeholder for WhatsApp screenshots
        st.image("https://via.placeholder.com/360x640/25D366/FFFFFF?text=WhatsApp+Demo+1", caption="Voice message sent")
        st.image("https://via.placeholder.com/360x640/25D366/FFFFFF?text=WhatsApp+Demo+2", caption="AI response")

def show_tech_stack():
    """Technical architecture"""
    
    st.markdown("# 🛠️ Technical Architecture")
    
    st.markdown("### Our Tech Stack")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="tech-card">
            <h3>🎯 Frontend</h3>
            <p><strong>Streamlit</strong></p>
            <p>Dashboard & Analytics</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card">
            <h3>⚡ Backend</h3>
            <p><strong>FastAPI + Flask</strong></p>
            <p>Webhook & Processing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tech-card">
            <h3>🧠 AI Engine</h3>
            <p><strong>GPT-5 + Whisper</strong></p>
            <p>Language & Voice</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="tech-card">
            <h3>💾 Database</h3>
            <p><strong>PostgreSQL</strong></p>
            <p>Neon Cloud</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Architecture diagram
    st.markdown("### System Architecture")
    
    st.markdown("""
    <div class="solution-card">
        <pre style="font-family: monospace; font-size: 14px;">
        Customer (WhatsApp)
              ↓
        Voice Message (Any Language)
              ↓
        Twilio API Gateway
              ↓
        Flask Webhook Server
              ↓
        ┌─────────────────────────┐
        │   TechFlow AI Engine    │
        │  ┌──────────────────┐   │
        │  │ Whisper API      │   │
        │  │ (Transcription)  │   │
        │  └──────────────────┘   │
        │           ↓             │
        │  ┌──────────────────┐   │
        │  │    GPT-5 API     │   │
        │  │  (Understanding) │   │
        │  └──────────────────┘   │
        └─────────────────────────┘
              ↓
        PostgreSQL Database
              ↓
        Response Generation
              ↓
        Customer (WhatsApp Reply)
        </pre>
    </div>
    """, unsafe_allow_html=True)

def show_market():
    """Market analysis"""
    
    st.markdown("# 📈 Market Opportunity")
    
    # TAM SAM SOM
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <h3>TAM</h3>
            <div class="big-number">$2.8T</div>
            <p>Global Mobile Commerce</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <h3>SAM</h3>
            <div class="big-number">$480B</div>
            <p>WhatsApp Commerce</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <h3>SOM</h3>
            <div class="big-number">$12B</div>
            <p>Year 1 Target</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Growth chart
    years = [2024, 2025, 2026, 2027, 2028]
    revenue = [0.5, 2.4, 8.7, 24.3, 52.8]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years, y=revenue,
        mode='lines+markers',
        name='Revenue (Billions USD)',
        line=dict(color='#0066CC', width=4),
        marker=dict(size=12)
    ))
    
    fig.update_layout(
        title='5-Year Revenue Projection',
        height=400,
        yaxis_title='Billions USD'
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_impact():
    """Impact metrics"""
    
    st.markdown("# 🎯 Global Impact")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="solution-card">
            <h2>🌍 Social Impact</h2>
            <ul style="font-size: 18px;">
                <li>780M people gain e-commerce access</li>
                <li>60+ languages preserved</li>
                <li>45% women entrepreneurs empowered</li>
                <li>Rural communities connected</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="problem-card">
            <h2>💰 Economic Impact</h2>
            <ul style="font-size: 18px;">
                <li>$500B new market unlocked</li>
                <li>2.5M jobs created</li>
                <li>150K businesses digitized</li>
                <li>30% rural income increase</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_future():
    """Future roadmap"""
    
    st.markdown("# 🔮 The Future")
    
    # Roadmap
    timeline_data = [
        ("Q1 2025", "🚀 Launch", "10 languages, 3 countries"),
        ("Q2 2025", "🌍 Expand", "30 languages, 10 countries"),
        ("Q3 2025", "🤝 Partner", "Shopify & WooCommerce"),
        ("Q4 2025", "📱 Scale", "1M+ merchants"),
        ("2026", "🎯 Lead", "Market leader position")
    ]
    
    for quarter, phase, desc in timeline_data:
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.markdown(f"### {quarter}")
        with col2:
            st.markdown(f"### {phase}")
        with col3:
            st.markdown(desc)
        st.markdown("---")
    
    # CTA
    st.markdown("""
    <div class="hero-section">
        <h2>Ready to Join the Revolution?</h2>
        <p>Be part of the future where commerce speaks every language</p>
        <div>
            <a href="#" class="cta-button">🚀 Get Early Access</a>
            <a href="#" class="cta-button">🤝 Partner With Us</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()