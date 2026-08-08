import streamlit as st
import re
from datetime import datetime

# Page config
st.set_page_config(
    page_title="UPI ScamShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Language dictionary
LANGUAGES = {
    "English": {
        "title": "UPI ScamShield",
        "subtitle": "Protect yourself from UPI scams",
        "theme": "Theme",
        "language": "Language",
        "color": "App Color",
        "input_method": "How do you want to check?",
        "paste_text": "Paste Text",
        "upload_image": "Upload Image",
        "enter_text": "Enter suspicious message, link, or details here...",
        "upload_file": "Upload screenshot or QR code image",
        "analyze_btn": "Analyze for Scams",
        "risk_level": "Risk Level",
        "safe": "🟢 Safe-looking",
        "suspicious": "🟡 Suspicious",
        "high_risk": "🔴 High Risk",
        "warning_signs": "Warning Signs Detected",
        "no_warnings": "No obvious warning signs detected",
        "checklist_title": "⚠️ Money Lost? Emergency Checklist",
        "checklist": [
            "📵 Immediately block the sender's number",
            "🔐 Change your UPI PIN and banking passwords",
            "📞 Call your bank's fraud department immediately",
            "📸 Save all screenshots and transaction details",
            "📝 File an FIR or cybercrime complaint",
            "🔗 Report to National Cybercrime Portal",
            "💳 Monitor your bank accounts for unauthorized transactions",
            "📱 Enable transaction alerts on your bank app"
        ],
        "resources": "🆘 Emergency Resources",
        "helpline": "Cybercrime Helpline: 1930",
        "portal": "National Cybercrime Portal: cybercrime.gov.in",
        "no_analysis": "Enter text or upload an image to analyze",
        "history": "Detection History",
        "clear_history": "Clear History"
    },
    "Telugu": {
        "title": "UPI స్కామ్‌షీల్డ్",
        "subtitle": "UPI స్కామ్‌ల నుండి సురక్షితంగా ఉండండి",
        "theme": "థీమ్",
        "language": "భాష",
        "color": "యాప్ రంగు",
        "input_method": "మీరు ఎలా తనిఖీ చేయాలనుకుంటున్నారు?",
        "paste_text": "టెక్స్ట్ అతికించండి",
        "upload_image": "ఇమేజ్ అपోలోడ్ చేయండి",
        "enter_text": "సందేహాస్పద సందేశం, లింక్ లేదా వివరాలను ఇక్కడ నమోదు చేయండి...",
        "upload_file": "స్క్రీన్‌షాట్ లేదా QR కోడ్ ఇమేజ్ అpload చేయండి",
        "analyze_btn": "స్కామ్‌ల కోసం విశ్లేషణ చేయండి",
        "risk_level": "ఝుందు స్థితి",
        "safe": "🟢 సురక్షితమైనది",
        "suspicious": "🟡 సందేహాస్పదమైనది",
        "high_risk": "🔴 అధిక ఖطरా",
        "warning_signs": "హెచ్చరిక సంకేతాలు కనుగొనబడ్డాయి",
        "no_warnings": "స్పష్టమైన హెచ్చరిక సంకేతాలు కనుగొనబడలేదు",
        "checklist_title": "⚠️ డబ్బు కోల్పోయారా? అత్యవసర చెక్‌లిస్ట్",
        "checklist": [
            "📵 వెంటనే పంపిన వ్యక్తి నంబర్‌ను బ్లాక్ చేయండి",
            "🔐 మీ UPI PIN మరియు బ్యాంకింగ్ పాస్‌వర్డ్‌లను మార్చండి",
            "📞 మీ బ్యాంకు యొక్క కోసం మరియు మోసం విభాగానికి కాల్ చేయండి",
            "📸 అన్ని స్క్రీన్‌షాట్‌లు మరియు లెన్‌దేన్ వివరాలను సేవ్ చేయండి",
            "📝 FIR లేదా సైబర్‌క్రైమ్ ఫిర్యాదు దాఖిల చేయండి",
            "🔗 జాతీయ సైబర్‌క్రైమ్ పోర్టల్‌కు నివేదించండి",
            "💳 మీ బ్యాంక్ ఖాతాలను అనుమతి లేని లెన్‌దెన్ కోసం పర్యవేక్షించండి",
            "📱 మీ బ్యాంక్ యాప్‌లో లెన్‌దెన్ అప్‌డేట్‌లను ఎనేబల్ చేయండి"
        ],
        "resources": "🆘 అత్యవసర వనరులు",
        "helpline": "సైబర్‌క్రైమ్ హెల్‌లైన్: 1930",
        "portal": "జాతీయ సైబర్‌క్రైమ్ పోర్టల్: cybercrime.gov.in",
        "no_analysis": "విశ్లేషణ చేయడానికి టెక్స్ట్‌ను నమోదు చేయండి లేదా ఇమేజ్ అpload చేయండి",
        "history": "కనుగొన్న చరిత్ర",
        "clear_history": "చరిత్రను క్లియర్ చేయండి"
    },
    "Hindi": {
        "title": "UPI स्कैमशील्ड",
        "subtitle": "UPI स्कैम से अपने आप को सुरक्षित रखें",
        "theme": "थीम",
        "language": "भाषा",
        "color": "ऐप रंग",
        "input_method": "आप कैसे जांच करना चाहते हैं?",
        "paste_text": "टेक्स्ट पेस्ट करें",
        "upload_image": "इमेज अपलोड करें",
        "enter_text": "संदिग्ध संदेश, लिंक या विवरण यहां दर्ज करें...",
        "upload_file": "स्क्रीनशॉट या QR कोड इमेज अपलोड करें",
        "analyze_btn": "स्कैम के लिए विश्लेषण करें",
        "risk_level": "जोखिम स्तर",
        "safe": "🟢 सुरक्षित दिखता है",
        "suspicious": "🟡 संदिग्ध",
        "high_risk": "🔴 उच्च जोखिम",
        "warning_signs": "चेतावनी के संकेत पाए गए",
        "no_warnings": "कोई स्पष्ट चेतावनी संकेत नहीं पाए गए",
        "checklist_title": "⚠️ पैसा खो गया? आपातकालीन चेकलिस्ट",
        "checklist": [
            "📵 तुरंत भेजने वाले का नंबर ब्लॉक करें",
            "🔐 अपना UPI PIN और बैंकिंग पासवर्ड बदलें",
            "📞 अपने बैंक की धोखाधड़ी विभाग को तुरंत कॉल करें",
            "📸 सभी स्क्रीनशॉट और लेनदेन विवरण सहेजें",
            "📝 FIR या साइबर अपराध शिकायत दर्ज करें",
            "🔗 राष्ट्रीय साइबर अपराध पोर्टल को रिपोर्ट करें",
            "💳 अपने बैंक खातों की अनुमति न दी गई गतिविधि के लिए निगरानी करें",
            "📱 अपने बैंक ऐप पर लेनदेन सतर्कता सक्षम करें"
        ],
        "resources": "🆘 आपातकालीन संसाधन",
        "helpline": "साइबर अपराध हेल्पलाइन: 1930",
        "portal": "राष्ट्रीय साइबर अपराध पोर्टल: cybercrime.gov.in",
        "no_analysis": "विश्लेषण करने के लिए टेक्स्ट दर्ज करें या इमेज अपलोड करें",
        "history": "पता लगाने का इतिहास",
        "clear_history": "इतिहास साफ करें"
    }
}

# Scam detection keywords and patterns
SCAM_PATTERNS = {
    "pay_to_receive": {
        "keywords": ["pay to receive", "payment to get", "pay first", "send money to get"],
        "risk": "high",
        "message": "Asking you to pay to receive money is a classic scam"
    },
    "urgent_threats": {
        "keywords": ["urgent", "immediately", "asap", "quick action", "before it's too late", "limited time"],
        "risk": "high",
        "message": "Urgent language and threats are common scam tactics"
    },
    "upi_pin_request": {
        "keywords": ["upi pin", "enter pin", "confirm pin", "otp", "secret code", "password"],
        "risk": "high",
        "message": "Never share your UPI PIN or OTP with anyone"
    },
    "fake_customer_care": {
        "keywords": ["customer care", "support team", "bank representative", "agent", "verify account", "confirm details"],
        "risk": "medium",
        "message": "Verify numbers and contacts through official bank websites"
    },
    "money_transfer_link": {
        "keywords": ["click here", "pay now", "transfer now", "process payment", "complete transaction"],
        "risk": "medium",
        "message": "Be cautious of unsolicited payment links"
    },
    "reward_lottery": {
        "keywords": ["won", "reward", "lottery", "prize", "congratulations", "claim", "bonus", "free money"],
        "risk": "high",
        "message": "Lottery and reward scams are common fraud schemes"
    },
    "account_verification": {
        "keywords": ["verify", "confirm", "update account", "enable", "disable", "reactivate", "locked"],
        "risk": "medium",
        "message": "Banks don't ask for personal details via messages"
    }
}

def detect_scams(text):
    """Analyze text for scam indicators"""
    if not text or len(text.strip()) == 0:
        return None, []
    
    text_lower = text.lower()
    detected_warnings = []
    risk_score = 0
    
    for pattern_name, pattern_info in SCAM_PATTERNS.items():
        for keyword in pattern_info["keywords"]:
            if keyword.lower() in text_lower:
                detected_warnings.append({
                    "pattern": pattern_name,
                    "message": pattern_info["message"],
                    "risk": pattern_info["risk"]
                })
                if pattern_info["risk"] == "high":
                    risk_score += 3
                else:
                    risk_score += 1
                break
    
    if risk_score >= 6:
        risk_level = "high_risk"
    elif risk_score >= 3:
        risk_level = "suspicious"
    else:
        risk_level = "safe"
    
    return risk_level, detected_warnings

# Sidebar configuration
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    # Language selection
    lang = st.selectbox(
        "Select Language",
        list(LANGUAGES.keys()),
        key="language_select"
    )
    
    strings = LANGUAGES[lang]
    
    # Theme selection
    theme = st.radio(
        strings["theme"],
        ["Light", "Dark", "System"],
        horizontal=True
    )
    
    # Color selection
    color = st.selectbox(
        strings["color"],
        ["Blue", "Green", "Red", "Purple", "Orange"]
    )
    
    st.divider()
    st.markdown("### 📚 About")
    st.info(
        "UPI ScamShield helps you identify and protect against UPI fraud. "
        "Always verify before taking action."
    )

# Apply theme and color
if theme == "Dark":
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
        color: #c9d1d9;
    }
    </style>
    """, unsafe_allow_html=True)

# Color mapping
color_map = {
    "Blue": "#0066cc",
    "Green": "#28a745",
    "Red": "#dc3545",
    "Purple": "#6f42c1",
    "Orange": "#fd7e14"
}

primary_color = color_map.get(color, "#0066cc")

# Main content
st.title(strings["title"])
st.markdown(f"<h3 style='color: {primary_color};'>{strings['subtitle']}</h3>", unsafe_allow_html=True)

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Main tabs
tab1, tab2, tab3 = st.tabs(["🔍 Analyze", "📋 Emergency Guide", "📱 Resources"])

with tab1:
    st.markdown(f"<h3 style='color: {primary_color};'>Enter Details to Check</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_method = st.radio(
            strings["input_method"],
            [strings["paste_text"], strings["upload_image"]],
            horizontal=True
        )
    
    if input_method == strings["paste_text"]:
        user_text = st.text_area(
            strings["enter_text"],
            height=150,
            placeholder="Paste the suspicious message here..."
        )
        
        if st.button(strings["analyze_btn"], use_container_width=True, type="primary"):
            if user_text.strip():
                risk_level, warnings = detect_scams(user_text)
                
                # Add to history
                st.session_state.history.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "text": user_text[:50] + "..." if len(user_text) > 50 else user_text,
                    "risk": risk_level
                })
                
                st.divider()
                
                # Display risk level
                if risk_level == "high_risk":
                    st.error(f"### {strings['risk_level']}: {strings['high_risk']}")
                elif risk_level == "suspicious":
                    st.warning(f"### {strings['risk_level']}: {strings['suspicious']}")
                else:
                    st.success(f"### {strings['risk_level']}: {strings['safe']}")
                
                # Display warnings
                if warnings:
                    st.markdown(f"### {strings['warning_signs']}")
                    for warning in warnings:
                        st.warning(f"⚠️ {warning['message']}")
                else:
                    st.info(strings["no_warnings"])
                
                # Emergency checklist for high risk
                if risk_level == "high_risk":
                    st.divider()
                    st.markdown(f"### {strings['checklist_title']}")
                    for item in strings["checklist"]:
                        st.write(f"{item}")
    
    else:
        uploaded_image = st.file_uploader(
            strings["upload_file"],
            type=["jpg", "jpeg", "png", "gif"]
        )
        
        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            st.info("🔍 Image analysis would be performed here (requires OCR/ML model)")

with tab2:
    st.markdown(f"<h3 style='color: {primary_color};'>{strings['checklist_title']}</h3>", unsafe_allow_html=True)
    
    for item in strings["checklist"]:
        st.write(item)
    
    st.divider()
    st.markdown("### 🛡️ Prevention Tips")
    prevention_tips = {
        "English": [
            "Never share your UPI PIN, OTP, or card details with anyone",
            "Verify payment links before clicking",
            "Use only official banking apps",
            "Enable transaction alerts on your bank account",
            "Be suspicious of unsolicited payment requests",
            "Always verify caller ID before sharing sensitive info"
        ],
        "Telugu": [
            "మీ UPI PIN, OTP లేదా కార్డ్ వివరాలను ఎవరితో పంచుకోవద్దు",
            "చెల్లింపు లिंक్‌లను క్లిక్ చేయడానికి ముందు ధృవీకరించండి",
            "అధికారిక బ్యాంకింగ్ యాప్‌లను మాత్రమే ఉపయోగించండి",
            "మీ బ్యాంక్ ఖాతాపై లెన్‌దెన్ అప్‌డేట్‌లను ఎనేబల్ చేయండి",
            "అనుమతి లేని చెల్లింపు అభ్యర్థనల గురించి సందేహాస్పదంగా ఉండండి",
            "సున్నితమైన సమాచారాన్ని పంచుకోసాగే ముందు కాలర్ ID ధృవీకరించండి"
        ],
        "Hindi": [
            "अपना UPI PIN, OTP या कार्ड विवरण किसी के साथ साझा न करें",
            "भुगतान लिंक पर क्लिक करने से पहले सत्यापित करें",
            "केवल आधिकारिक बैंकिंग ऐप्स का उपयोग करें",
            "अपने बैंक खाते पर लेनदेन सतर्कता सक्षम करें",
            "अनुमति न दी गई भुगतान अनुरोधों के बारे में संदेहास्पद रहें",
            "संवेदनशील जानकारी साझा करने से पहले कॉलर ID सत्यापित करें"
        ]
    }
    
    for tip in prevention_tips.get(lang, prevention_tips["English"]):
        st.write(f"✓ {tip}")

with tab3:
    st.markdown(f"<h3 style='color: {primary_color};'>{strings['resources']}</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📞 Cybercrime Helpline")
        st.metric("Helpline Number", "1930")
        st.write("Available 24/7 for cybercrime complaints")
    
    with col2:
        st.markdown("### 🌐 Cybercrime Portal")
        st.markdown("[National Cybercrime Reporting Portal](https://cybercrime.gov.in/)")
        st.write("File complaints online")
    
    st.divider()
    
    st.markdown("### 📞 Bank Contact Numbers")
    st.info(
        "Keep your bank's fraud helpline number saved:\n\n"
        "- **HDFC Bank**: 1860-419-0888\n"
        "- **ICICI Bank**: 1860-102-4332\n"
        "- **SBI**: 1800-112-211\n"
        "- **Axis Bank**: 1800-209-5959\n\n"
        "*Note: These are example numbers. Always verify from official bank website.*"
    )

# History section
if st.session_state.history:
    st.divider()
    with st.expander(f"📋 {strings['history']} ({len(st.session_state.history)})"):
        for idx, record in enumerate(reversed(st.session_state.history[-10:]), 1):
            risk_emoji = "🟢" if record["risk"] == "safe" else "🟡" if record["risk"] == "suspicious" else "🔴"
            st.write(f"{idx}. {record['timestamp']} | {risk_emoji} {record['text']}")
        
        if st.button(strings["clear_history"]):
            st.session_state.history = []
            st.rerun()

# Footer
st.divider()
st.markdown(
    "<p style='text-align: center; color: #888;'>"
    "UPI ScamShield - Your Personal Fraud Protection Assistant | "
    "Use responsibly and always verify information independently"
    "</p>",
    unsafe_allow_html=True
)