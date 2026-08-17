import streamlit as st
from datetime import datetime

# ============================================================================
# UPI ScamShield - Complete Streamlit App (Streamlit Only, No Dependencies)
# ============================================================================

# Page Configuration
st.set_page_config(
    page_title="UPI ScamShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# LANGUAGE DICTIONARY - Multi-language Support
# ============================================================================

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
        "no_analysis": "Enter text to analyze",
        "history": "Detection History",
        "clear_history": "Clear History",
        "prevention_title": "🛡️ Prevention Tips",
        "prevention_tips": [
            "Never share your UPI PIN, OTP, or card details with anyone",
            "Verify payment links before clicking",
            "Use only official banking apps",
            "Enable transaction alerts on your bank account",
            "Be suspicious of unsolicited payment requests",
            "Always verify caller ID before sharing sensitive info",
            "Check bank website for actual customer care numbers",
            "Look for HTTPS and official branding on payment pages"
        ],
        "bank_title": "📞 Bank Contact Numbers",
        "bank_note": "Keep your bank's fraud helpline number saved:",
        "about": "About",
        "about_text": "UPI ScamShield helps you identify and protect against UPI fraud. Always verify before taking action.",
        "footer": "UPI ScamShield - Your Personal Fraud Protection Assistant | Use responsibly and always verify information independently",
        "settings": "⚙️ Settings",
        "emergency_guide": "Emergency Guide",
        "emergency_resources": "Emergency Resources"
    },
    "Telugu": {
        "title": "UPI స్కామ్‌షీల్డ్",
        "subtitle": "UPI స్కామ్‌ల నుండి సురక్షితంగా ఉండండి",
        "theme": "థీమ్",
        "language": "భాష",
        "color": "యాప్ రంగు",
        "input_method": "మీరు ఎలా తనిఖీ చేయాలనుకుంటున్నారు?",
        "paste_text": "టెక్స్ట్ అతికించండి",
        "upload_image": "ఇమేజ్ అపోలోడ్ చేయండి",
        "enter_text": "సందేహాస్పద సందేశం, లింక్ లేదా వివరాలను ఇక్కడ నమోదు చేయండి...",
        "upload_file": "స్క్రీన్‌షాట్ లేదా QR కోడ్ ఇమేజ్ అपలోడ్ చేయండి",
        "analyze_btn": "స్కామ్‌ల కోసం విశ్లేషణ చేయండి",
        "risk_level": "ఝుందు స్థితి",
        "safe": "🟢 సురక్షితమైనది",
        "suspicious": "🟡 సందేహాస్పదమైనది",
        "high_risk": "🔴 అధిక ఖతరా",
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
        "no_analysis": "విశ్లేషణ చేయడానికి టెక్స్ట్‌ను నమోదు చేయండి",
        "history": "కనుగొన్న చరిత్ర",
        "clear_history": "చరిత్రను క్లియర్ చేయండి",
        "prevention_title": "🛡️ నిరోధక చిట్కాలు",
        "prevention_tips": [
            "మీ UPI PIN, OTP లేదా కార్డ్ వివరాలను ఎవరితో పంచుకోవద్దు",
            "చెల్లింపు లింక్‌లను క్లిక్ చేయడానికి ముందు ధృవీకరించండి",
            "అధికారిక బ్యాంకింగ్ యాప్‌లను మాత్రమే ఉపయోగించండి",
            "మీ బ్యాంక్ ఖాతాపై లెన్‌దెన్ అప్‌డేట్‌లను ఎనేబల్ చేయండి",
            "అనుమతి లేని చెల్లింపు అభ్యర్థనల గురించి సందేహాస్పదంగా ఉండండి",
            "సున్నితమైన సమాచారాన్ని పంచుకోసాగే ముందు కాలర్ ID ధృవీకరించండి",
            "బ్యాంక్ వెబ్‌సైట్ నుండి వాస్తవ కస్టమర్ కేర్ నంబర్‌లను తనిఖీ చేయండి",
            "చెల్లింపు పేజీలలో HTTPS మరియు అధికారిక బ్రాండింగ్‌ను చూడండి"
        ],
        "bank_title": "📞 బ్యాంక్ సంప్రదింపు సంఖ్యలు",
        "bank_note": "మీ బ్యాంకు యొక్క మోసం సహాయరేఖ నంబర్ సేవ్ చేయండి:",
        "about": "గురించి",
        "about_text": "UPI ScamShield UPI మోసం నుండి రక్షణ పొందటానికి సహాయ చేస్తుంది. ఎల్లప్పుడు చర్య తీసుకోవడానికి ముందు ధృవీకరించండి.",
        "footer": "UPI స్కామ్‌షీల్డ్ - మీ వ్యక్తిగత మోసం రక్షణ సహాయకుడు | బాధ్యతపూర్వకంగా ఉపయోగించండి మరియు ఎల్లప్పుడు స్వతంత్రంగా సమాచారాన్ని ధృవీకరించండి",
        "settings": "⚙️ సెట్టింగ్‌లు",
        "emergency_guide": "అత్యవసర గైడ్",
        "emergency_resources": "అత్యవసర వనరులు"
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
        "no_analysis": "विश्लेषण करने के लिए टेक्स्ट दर्ज करें",
        "history": "पता लगाने का इतिहास",
        "clear_history": "इतिहास साफ करें",
        "prevention_title": "🛡️ रोकथाम टिप्स",
        "prevention_tips": [
            "अपना UPI PIN, OTP या कार्ड विवरण किसी के साथ साझा न करें",
            "भुगतान लिंक पर क्लिक करने से पहले सत्यापित करें",
            "केवल आधिकारिक बैंकिंग ऐप्स का उपयोग करें",
            "अपने बैंक खाते पर लेनदेन सतर्कता सक्षम करें",
            "अनुमति न दी गई भुगतान अनुरोधों के बारे में संदेहास्पद रहें",
            "संवेदनशील जानकारी साझा करने से पहले कॉलर ID सत्यापित करें",
            "बैंक की वेबसाइट से वास्तविक कस्टमर केयर नंबर जांचें",
            "भुगतान पृष्ठों पर HTTPS और आधिकारिक ब्रांडिंग देखें"
        ],
        "bank_title": "📞 बैंक संपर्क नंबर",
        "bank_note": "अपने बैंक की धोखाधड़ी हेल्पलाइन नंबर सहेजें:",
        "about": "के बारे में",
        "about_text": "UPI ScamShield आपको UPI धोखाधड़ी की पहचान और सुरक्षा में मदद करता है। कार्रवाई करने से पहले हमेशा सत्यापित करें।",
        "footer": "UPI स्कैमशील्ड - आपके व्यक्तिगत धोखाधड़ी संरक्षण सहायक | जिम्मेदारी से उपयोग करें और हमेशा स्वतंत्र रूप से जानकारी सत्यापित करें",
        "settings": "⚙️ सेटिंग्स",
        "emergency_guide": "आपातकालीन गाइड",
        "emergency_resources": "आपातकालीन संसाधन"
    }
}

# ============================================================================
# SCAM DETECTION PATTERNS
# ============================================================================

# Multi-word phrase patterns with descriptive messages (checked first)
SCAM_PATTERNS = {
    "pay_to_receive": {
        "keywords": ["pay to receive", "payment to get", "pay first", "send money to get", "deposit to receive"],
        "risk": "high",
        "urgency": "high",
        "message": "Asking you to pay to receive money is a classic scam"
    },
    "screen_share": {
        "keywords": ["screen share", "screenshare", "anydesk", "teamviewer", "quick support"],
        "risk": "very_high",
        "urgency": "immediate",
        "message": "Never install screen-sharing apps or grant remote access to your device"
    },
    "qr_code": {
        "keywords": ["qr code", "scan qr", "scan this qr", "qr to receive"],
        "risk": "high",
        "urgency": "immediate",
        "message": "Scanning a QR code can only send money, never receive it - be cautious"
    },
    "digital_arrest": {
        "keywords": ["digital arrest"],
        "risk": "very_high",
        "urgency": "immediate",
        "message": "'Digital arrest' is a well-known scam - no real agency arrests you over a call"
    },
    "begging_for_money": {
        "keywords": [
            "please help me", "please send money", "please lend me", "please transfer",
            "urgently need money", "need money urgently", "in urgent need of money",
            "i am stranded", "i'm stranded", "stuck here", "family emergency",
            "medical emergency", "hospital bill", "hospitalized", "accident happened",
            "please help financially", "need your help urgently", "borrow some money",
            "small favor please", "please i beg you", "life or death", "please save me",
            "desperately need", "only you can help me", "trust me this once"
        ],
        "risk": "high",
        "urgency": "high",
        "message": "Emotional appeals begging for urgent money are a common impersonation scam - verify by calling the person directly on a known number before sending anything"
    },
}

# Points assigned per risk level for scoring
RISK_POINTS = {
    "very_high": 4,
    "high": 3,
    "medium_high": 2,
    "medium": 1
}

# ----------------------------------------------------------------------
# Single-word / short-phrase keyword table: word -> (risk, urgency)
# Consolidated from all provided keyword lists
# ----------------------------------------------------------------------
KEYWORD_TABLE = {
    # Original core terms
    "otp": ("very_high", "immediate"),
    "pin": ("very_high", "immediate"),
    "mpin": ("very_high", "immediate"),
    "kyc": ("high", "immediate"),
    "cashback": ("high", "high"),
    "reward": ("high", "high"),

    # Account / status words
    "account": ("medium", "medium"),
    "bank": ("medium", "medium"),
    "suspended": ("high", "immediate"),
    "deactivated": ("high", "immediate"),
    "frozen": ("high", "immediate"),
    "locked": ("high", "immediate"),
    "expired": ("high", "high"),
    "disconnected": ("high", "high"),
    "terminated": ("high", "immediate"),
    "restricted": ("high", "high"),
    "deletion": ("high", "immediate"),
    "closure": ("high", "immediate"),
    "warning": ("medium", "high"),
    "alert": ("medium", "high"),
    "notice": ("medium", "high"),
    "action": ("medium", "high"),
    "deadline": ("high", "immediate"),
    "today": ("high", "immediate"),
    "tomorrow": ("high", "high"),
    "immediately": ("high", "immediate"),
    "urgent": ("high", "immediate"),
    "final": ("high", "immediate"),
    "last-chance": ("high", "immediate"),
    "hurry": ("high", "immediate"),
    "deadline-today": ("high", "immediate"),
    "confirm": ("medium", "high"),
    "confirmation": ("medium", "high"),
    "authentication": ("high", "high"),
    "validation": ("high", "high"),
    "reactivation": ("high", "immediate"),
    "renewal": ("high", "high"),
    "update": ("medium", "high"),
    "upgrade": ("medium", "high"),
    "registration": ("medium", "high"),
    "activation": ("high", "high"),
    "login": ("high", "high"),
    "sign-in": ("high", "high"),
    "password": ("very_high", "immediate"),
    "passcode": ("very_high", "immediate"),
    "security-code": ("very_high", "immediate"),
    "verification-code": ("very_high", "immediate"),
    "credentials": ("very_high", "immediate"),
    "username": ("high", "high"),
    "secret": ("very_high", "immediate"),
    "recovery": ("high", "high"),
    "reset": ("high", "high"),
    "unlock": ("high", "immediate"),
    "approve": ("very_high", "immediate"),
    "authorize": ("very_high", "immediate"),
    "accept": ("high", "immediate"),
    "decline": ("medium", "medium"),
    "collect": ("very_high", "immediate"),
    "request": ("high", "immediate"),
    "transfer": ("high", "immediate"),
    "payment": ("high", "immediate"),
    "pay": ("high", "immediate"),
    "send": ("high", "immediate"),
    "deposit": ("medium", "high"),
    "withdraw": ("high", "immediate"),
    "debit": ("high", "immediate"),
    "credit": ("medium", "high"),
    "charge": ("high", "high"),
    "invoice": ("high", "high"),
    "bill": ("medium", "high"),
    "outstanding": ("high", "high"),
    "overdue": ("high", "immediate"),
    "fine": ("high", "immediate"),
    "penalty": ("high", "immediate"),
    "tax": ("high", "high"),
    "customs": ("high", "high"),
    "clearance": ("high", "high"),
    "compensation": ("high", "high"),
    "insurance": ("high", "high"),
    "claim": ("high", "high"),
    "settlement": ("high", "high"),
    "commission": ("high", "high"),
    "profit": ("high", "high"),
    "investment": ("high", "high"),
    "loan": ("high", "high"),
    "credit-card": ("high", "high"),
    "lottery": ("very_high", "high"),
    "jackpot": ("very_high", "high"),
    "prize": ("very_high", "high"),
    "winner": ("very_high", "high"),
    "giveaway": ("high", "high"),
    "bonus": ("high", "high"),
    "gift": ("high", "high"),
    "voucher": ("high", "high"),
    "coupon": ("medium", "medium"),
    "offer": ("medium", "medium"),
    "benefit": ("high", "high"),
    "subsidy": ("high", "high"),
    "scholarship": ("high", "high"),
    "pension": ("high", "high"),
    "salary": ("medium", "high"),
    "job": ("high", "high"),
    "interview": ("medium", "medium"),
    "parcel": ("medium", "high"),
    "delivery": ("medium", "high"),
    "courier": ("medium", "high"),
    "shipment": ("medium", "high"),
    "tracking": ("medium", "high"),
    "address": ("high", "high"),
    "reschedule": ("high", "high"),
    "missed-delivery": ("high", "high"),
    "electricity": ("high", "immediate"),
    "disconnection": ("high", "immediate"),
    "sim": ("high", "immediate"),
    "esim": ("high", "immediate"),
    "malware": ("very_high", "immediate"),
    "antivirus": ("high", "high"),
    "download": ("high", "immediate"),
    "install": ("high", "immediate"),
    "remote-access": ("very_high", "immediate"),
    "screen-sharing": ("very_high", "immediate"),
    "link": ("high", "high"),
    "click-here": ("high", "immediate"),
    "attachment": ("high", "high"),
    "apk": ("very_high", "immediate"),
    "app-update": ("high", "immediate"),
    "customer-care": ("high", "high"),
    "support-agent": ("high", "high"),
    "police": ("very_high", "immediate"),
    "court": ("very_high", "immediate"),
    "arrest": ("very_high", "immediate"),
    "legal-action": ("very_high", "immediate"),
    "investigation": ("very_high", "immediate"),
    "complaint": ("high", "high"),
    "case-number": ("high", "high"),

    # Emotional appeal / begging-for-money terms
    "emergency": ("high", "immediate"),
    "hospitalized": ("high", "immediate"),
    "stranded": ("high", "immediate"),
    "beg": ("high", "high"),
    "desperate": ("high", "high"),
    "borrow": ("medium", "high"),
    "favor": ("medium", "medium"),
    "lend": ("medium", "high"),
    "trust-me": ("medium_high", "high"),

    # Payment / transaction mechanics
    "beneficiary": ("medium", "medium"),
    "recipient": ("medium", "medium"),
    "collect-request": ("high", "high"),
    "mandate": ("high", "high"),
    "autopay": ("high", "high"),
    "debit-request": ("high", "immediate"),
    "payee": ("medium", "medium"),
    "vpa": ("medium", "medium"),
    "upi-id": ("medium", "medium"),
    "transaction-id": ("medium", "medium"),
    "reference-number": ("medium", "medium"),

    # Sensitive data requests
    "bank-details": ("high", "high"),
    "card-details": ("very_high", "immediate"),
    "cvv": ("very_high", "immediate"),
    "expiry-date": ("high", "high"),
    "security-question": ("very_high", "immediate"),
    "access-code": ("very_high", "immediate"),
    "verification-link": ("high", "high"),
    "login-link": ("high", "high"),

    # Urgency / pressure phrases
    "act-now": ("high", "immediate"),
    "act-fast": ("high", "immediate"),
    "respond-now": ("high", "immediate"),
    "within-hours": ("high", "immediate"),
    "within-24-hours": ("high", "immediate"),
    "time-sensitive": ("medium", "high"),
    "limited-time": ("medium", "high"),
    "last-warning": ("high", "immediate"),
    "final-warning": ("high", "immediate"),
    "immediate-action": ("high", "immediate"),
    "avoid-loss": ("high", "high"),
    "avoid-closure": ("high", "immediate"),
    "avoid-penalty": ("high", "high"),
    "non-compliance": ("high", "high"),
    "escalation": ("high", "high"),
    "formal-notice": ("medium", "high"),
    "legal-notice": ("high", "immediate"),
    "court-notice": ("very_high", "immediate"),
    "warrant": ("very_high", "immediate"),

    # Fake income / money-for-nothing lures
    "instant-cash": ("high", "high"),
    "easy-money": ("high", "high"),
    "guaranteed-income": ("very_high", "high"),
    "risk-free": ("high", "high"),
    "double-your-money": ("very_high", "high"),
    "earnings": ("medium", "medium"),
    "payout": ("high", "high"),
    "cash-prize": ("very_high", "high"),
    "lucky-draw": ("high", "high"),
    "contest": ("medium", "medium"),
    "free-money": ("very_high", "high"),

    # Upfront "fee" scams
    "processing-fee": ("high", "immediate"),
    "release-fee": ("very_high", "immediate"),
    "activation-fee": ("high", "high"),
    "security-deposit": ("very_high", "immediate"),
    "advance-fee": ("very_high", "immediate"),
    "test-payment": ("high", "immediate"),

    # Impersonated authority
    "officer": ("medium", "high"),
    "agent": ("medium", "medium"),
    "manager": ("medium", "medium"),
    "executive": ("medium", "medium"),
    "government": ("high", "high"),
    "police-officer": ("very_high", "immediate"),
    "cyber-cell": ("very_high", "immediate"),
    "income-tax": ("high", "high"),
    "rbi": ("high", "high"),
    "npci": ("high", "high"),
    "uidai": ("high", "high"),
    "aadhaar": ("high", "high"),
    "pan": ("high", "high"),
    "investigator": ("very_high", "immediate"),
    "authority": ("high", "high"),
    "verification-team": ("high", "high"),

    # Link / domain red flags
    "short-link": ("high", "high"),
    "redirect": ("high", "high"),
    "untrusted-domain": ("high", "high"),
    "domain-mismatch": ("high", "high"),
    "secure-login": ("medium", "high"),
    "mobile-app": ("medium", "medium"),

    # Remote access tools
    "remote-desktop": ("very_high", "immediate"),
    "anydesk": ("very_high", "immediate"),
    "teamviewer": ("very_high", "immediate"),
    "quicksupport": ("very_high", "immediate"),
    "rustdesk": ("very_high", "immediate"),
    "unknown-source": ("high", "high"),
    "unknown-app": ("high", "immediate"),
    "malicious-file": ("very_high", "immediate"),
    "compressed-file": ("high", "high"),
    "zip-file": ("high", "high"),
    "download-now": ("high", "immediate"),
    "open-attachment": ("high", "high"),
    "enable-permission": ("very_high", "immediate"),

    # Isolation / secrecy tactics (classic "digital arrest" / call-center scam signs)
    "confidential": ("medium", "high"),
    "keep-secret": ("high", "immediate"),
    "do-not-tell": ("high", "immediate"),
    "do-not-disconnect": ("high", "immediate"),
    "stay-on-call": ("high", "immediate"),
    "private-line": ("medium", "high"),
    "transfer-now": ("very_high", "immediate"),
    "do-not-contact-bank": ("very_high", "immediate"),
    "do-not-report": ("very_high", "immediate"),
    "delete-message": ("high", "high"),
    "share-location": ("high", "high"),
    "recording": ("medium", "medium"),
    "monitoring": ("high", "high"),
    "surveillance": ("high", "high"),
}

import re as _re

def _to_pattern(word):
    """Convert a hyphenated keyword into a regex allowing hyphen, space, or nothing between parts."""
    parts = word.split("-")
    if len(parts) == 1:
        return r"\b" + _re.escape(word) + r"\b"
    joined = r"[\s-]*".join(_re.escape(p) for p in parts)
    return r"\b" + joined + r"\b"

# ============================================================================
# STRUCTURAL WARNING SIGN DETECTORS (non-keyword pattern checks)
# ============================================================================

# Known URL shorteners commonly abused in scam links
SHORTENER_DOMAINS = [
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "rebrand.ly",
    "cutt.ly", "shorturl.at", "rb.gy", "tiny.cc", "ow.ly", "bit.do"
]

# Legitimate-looking but risky TLDs/file types often used in phishing
SUSPICIOUS_FILE_EXT = [".apk", ".exe", ".scr", ".bat"]

# Action words + sensitive terms that scammers often merge without a space
# (e.g. "sendotp", "sharepin", "clicklink") to slip past spam/keyword filters
COMBINED_ACTIONS = [
    "send", "share", "enter", "confirm", "verify", "give", "tell",
    "reveal", "provide", "submit", "forward", "reply", "type", "input", "click"
]
COMBINED_SENSITIVE = [
    "otp", "pin", "mpin", "cvv", "password", "passcode",
    "link", "qr", "details", "card", "atmpin", "upipin", "creditcard", "info"
]

def _detect_structural_signs(original_text):
    """Detect scam indicators that aren't simple keyword matches."""
    signs = []
    text = original_text
    text_lower = text.lower()

    # 1. Any URL present
    urls = _re.findall(r'(https?://[^\s]+|www\.[^\s]+)', text_lower)
    if urls:
        shortened = [u for u in urls if any(d in u for d in SHORTENER_DOMAINS)]
        if shortened:
            signs.append({
                "pattern": "shortened_link",
                "message": "Shortened/masked link detected - the real destination is hidden",
                "risk": "very_high",
                "urgency": "immediate"
            })
        else:
            signs.append({
                "pattern": "contains_link",
                "message": "Message contains a link - verify the domain before clicking",
                "risk": "medium_high",
                "urgency": "high"
            })
        if any(ext in u for u in urls for ext in SUSPICIOUS_FILE_EXT):
            signs.append({
                "pattern": "app_file_link",
                "message": "Link points to an installable app file (.apk/.exe) - do not download",
                "risk": "very_high",
                "urgency": "immediate"
            })

    # 2. Phone numbers (Indian mobile-style 10-digit, or with +91 / 0 prefix)
    phone_matches = _re.findall(r'(?<!\d)(?:\+?91[\-\s]?)?[6-9]\d{9}(?!\d)', text)
    if phone_matches:
        signs.append({
            "pattern": "phone_number",
            "message": "Contains a phone number - never call back numbers from unsolicited messages; use only numbers from your bank's official website",
            "risk": "medium_high",
            "urgency": "high"
        })

    # 3. Generic greeting instead of personalized name
    if _re.search(r'\bdear (customer|user|sir|madam|valued customer|member)\b', text_lower):
        signs.append({
            "pattern": "generic_greeting",
            "message": "Generic greeting ('Dear Customer') instead of your real name - banks usually address you by name",
            "risk": "medium",
            "urgency": "medium"
        })

    # 4. Money amount mentioned (₹ or Rs figures)
    if _re.search(r'(₹|rs\.?|inr)\s?[\d,]+', text_lower):
        signs.append({
            "pattern": "money_amount",
            "message": "Specific money amount mentioned - be cautious of unexpected transaction claims",
            "risk": "medium",
            "urgency": "medium"
        })

    # 5. Excessive urgency punctuation (multiple ! or ?)
    if _re.search(r'[!?]{2,}', text):
        signs.append({
            "pattern": "excessive_punctuation",
            "message": "Excessive exclamation/question marks - a common pressure tactic",
            "risk": "medium",
            "urgency": "medium"
        })

    # 6. ALL CAPS shouting (3+ consecutive all-caps words, 4+ letters each)
    caps_words = _re.findall(r'\b[A-Z]{4,}\b', text)
    if len(caps_words) >= 3:
        signs.append({
            "pattern": "all_caps",
            "message": "Excessive use of ALL CAPS - often used to create panic or urgency",
            "risk": "medium",
            "urgency": "medium"
        })

    # 7. Suspicious email address (free/generic domain impersonating a bank)
    emails = _re.findall(r'[\w.\-]+@[\w.\-]+\.\w+', text_lower)
    free_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "rediffmail.com"]
    bank_terms = ["bank", "upi", "paytm", "phonepe", "gpay", "sbi", "hdfc", "icici", "axis", "kyc", "rbi"]
    for email in emails:
        domain = email.split("@")[-1]
        local = email.split("@")[0]
        if domain in free_domains and any(term in local for term in bank_terms):
            signs.append({
                "pattern": "spoofed_email",
                "message": "Email claims to be from a bank/UPI service but uses a free public email domain - a strong impersonation signal",
                "risk": "very_high",
                "urgency": "immediate"
            })
            break

    # 8. Very short message with just a link + urgency word (typical smishing)
    if urls and len(text.split()) <= 12 and _re.search(r'\b(urgent|now|today|immediately)\b', text_lower):
        signs.append({
            "pattern": "smishing_pattern",
            "message": "Short message combining a link with urgent language - typical of SMS phishing (smishing)",
            "risk": "high",
            "urgency": "immediate"
        })

    # 9. Combined/joined words with no space (e.g. "sendotp", "sharepin", "clicklink")
    # Scammers often merge an action word + a sensitive term to slip past spam/keyword filters
    combined_pattern = (
        r'\b(?:'
        + '|'.join(COMBINED_ACTIONS)
        + r')(?:'
        + '|'.join(COMBINED_SENSITIVE)
        + r')\b'
    )
    combined_matches = set()
    for m in _re.finditer(combined_pattern, text_lower):
        combined_matches.add(m.group(0))

    for combo in sorted(combined_matches)[:5]:
        signs.append({
            "pattern": f"combined_word_{combo}",
            "message": f"Suspicious joined word \"{combo}\" detected - scammers merge words like this (no space) to dodge spam/keyword filters. Never comply with such requests",
            "risk": "very_high",
            "urgency": "immediate"
        })

    return signs

# ============================================================================
# SCAM DETECTION FUNCTION
# ============================================================================

def detect_scams(text, keyword_table=None):
    """Analyze text for scam indicators and return risk level"""
    if not text or len(text.strip()) == 0:
        return None, []

    if keyword_table is None:
        keyword_table = KEYWORD_TABLE

    text_lower = " " + text.lower() + " "
    detected_warnings = []
    risk_score = 0
    matched_words = set()

    # 1. Check descriptive multi-word phrase patterns first
    for pattern_name, pattern_info in SCAM_PATTERNS.items():
        for keyword in pattern_info["keywords"]:
            if keyword.lower() in text_lower:
                detected_warnings.append({
                    "pattern": pattern_name,
                    "message": pattern_info["message"],
                    "risk": pattern_info["risk"],
                    "urgency": pattern_info.get("urgency", "medium")
                })
                risk_score += RISK_POINTS.get(pattern_info["risk"], 1)
                matched_words.add(keyword.lower())
                break

    # 2. Check single-word / short-phrase keyword table (user-editable)
    for word, value in keyword_table.items():
        if word in matched_words:
            continue
        risk, urgency = value[0], value[1]
        pattern = _to_pattern(word)
        if _re.search(pattern, text_lower):
            detected_warnings.append({
                "pattern": word,
                "message": f"The term \"{word.replace('-', ' ').title()}\" is commonly used in scam messages",
                "risk": risk,
                "urgency": urgency
            })
            risk_score += RISK_POINTS.get(risk, 1)

    # 3. Check structural / behavioral warning signs (non-keyword based)
    for sign in _detect_structural_signs(text):
        detected_warnings.append(sign)
        risk_score += RISK_POINTS.get(sign["risk"], 1)

    # Sort warnings by risk severity (highest first)
    severity_order = {"very_high": 0, "high": 1, "medium_high": 2, "medium": 3}
    detected_warnings.sort(key=lambda w: severity_order.get(w["risk"], 4))

    if risk_score >= 8:
        risk_level = "high_risk"
    elif risk_score >= 4:
        risk_level = "suspicious"
    else:
        risk_level = "safe"

    return risk_level, detected_warnings

# ============================================================================
# LOCAL PERSISTENCE (JSON file next to this script - first-party only:
# uses Python's built-in json/os modules, no third-party storage libs)
# ============================================================================

import json
import os
import hashlib

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scamshield_data.json")
LEADERBOARD_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leaderboard.json")

EDIT_PASSWORD = "8946$"
UNLOCK_USES_REQUIRED = 10

DEFAULT_DATA = {
    "usage_count": 0,           # total number of analyses run on this install
    "editing_unlocked": False,  # whether the password has been entered correctly
    "active_keywords": None,    # None = use built-in KEYWORD_TABLE; else user-edited copy
    "seen_text_hashes": []      # hashes of previously analyzed messages (XP anti-duplicate)
}

DEFAULT_LEADERBOARD = {}        # {player_name: {"xp": int, "analyses": int, "last_active": str}}

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            for k, v in DEFAULT_DATA.items():
                if k not in data:
                    data[k] = v
            return data
        except Exception:
            return json.loads(json.dumps(DEFAULT_DATA))
    return json.loads(json.dumps(DEFAULT_DATA))

def save_data(data):
    # Never let the leaderboard live inside this file - it has its own dedicated JSON store
    to_write = {k: v for k, v in data.items() if k != "leaderboard"}
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(to_write, f, indent=2)
    except Exception:
        pass

# ----------------------------------------------------------------------
# DEDICATED LEADERBOARD JSON STORE (leaderboard.json)
# ----------------------------------------------------------------------

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return dict(DEFAULT_LEADERBOARD)
    return dict(DEFAULT_LEADERBOARD)

def save_leaderboard(leaderboard):
    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(leaderboard, f, indent=2)
    except Exception:
        pass

def get_effective_keyword_table():
    """Return the user-edited keyword table if one exists, else the built-in default."""
    active = st.session_state.persist.get("active_keywords")
    if active:
        return {w: (v[0], v[1]) for w, v in active.items()}
    return KEYWORD_TABLE

def get_level(xp):
    return xp // 100 + 1

def xp_progress_in_level(xp):
    return xp % 100

def award_xp(player_name, amount):
    lb = st.session_state.leaderboard
    entry = lb.setdefault(player_name, {"xp": 0, "analyses": 0, "last_active": ""})
    entry["xp"] = max(0, entry["xp"] + amount)
    entry["analyses"] += 1
    entry["last_active"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_leaderboard(lb)
    return entry["xp"]

MAX_SEEN_HASHES = 5000  # cap stored history to keep the local file small

def _hash_text(text):
    normalized = " ".join(text.strip().lower().split())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

def is_duplicate_text(text):
    """Check if this exact message has already been analyzed (for XP anti-duplicate)."""
    h = _hash_text(text)
    return h in set(st.session_state.persist.get("seen_text_hashes", []))

def register_text(text):
    """Record this message's hash so it can't earn XP again."""
    h = _hash_text(text)
    seen = st.session_state.persist.setdefault("seen_text_hashes", [])
    if h not in seen:
        seen.append(h)
        if len(seen) > MAX_SEEN_HASHES:
            del seen[: len(seen) - MAX_SEEN_HASHES]
        save_data(st.session_state.persist)

# ============================================================================
# GIBBERISH DETECTION (random keyboard-mash strings like "dusgfhbnvcbxuyfg")
# ============================================================================

_VOWELS = set("aeiou")
GIBBERISH_XP_PENALTY = -5

def _looks_like_gibberish_word(word):
    """Flag a single word as gibberish based on vowel scarcity / long consonant runs."""
    w = _re.sub(r'[^a-z]', '', word.lower())
    if len(w) < 5:
        return False

    vowel_count = sum(1 for c in w if c in _VOWELS)
    vowel_ratio = vowel_count / len(w)

    max_consonant_run = 0
    current_run = 0
    for c in w:
        if c not in _VOWELS:
            current_run += 1
            max_consonant_run = max(max_consonant_run, current_run)
        else:
            current_run = 0

    return vowel_ratio < 0.15 or max_consonant_run >= 5

def is_gibberish_text(text):
    """Return True if most 'words' (5+ letters) in the text look like random keyboard mashing."""
    words = [w for w in _re.findall(r"[A-Za-z]+", text) if len(w) >= 5]
    if not words:
        return False
    flagged = sum(1 for w in words if _looks_like_gibberish_word(w))
    return (flagged / len(words)) >= 0.5

# ============================================================================
# INITIALIZE SESSION STATE
# ============================================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "lang" not in st.session_state:
    st.session_state.lang = "English"

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

if "color" not in st.session_state:
    st.session_state.color = "Blue"

if "persist" not in st.session_state:
    st.session_state.persist = load_data()

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = load_leaderboard()

if "player_name" not in st.session_state:
    st.session_state.player_name = "Player1"

if "just_unlocked" not in st.session_state:
    st.session_state.just_unlocked = False

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================

with st.sidebar:
    st.markdown("### " + LANGUAGES["English"]["settings"])
    
    # Language selection
    lang = st.selectbox(
        "Select Language",
        list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(st.session_state.lang),
        key="language_select"
    )
    st.session_state.lang = lang
    
    # Get current language strings
    strings = LANGUAGES[lang]
    
    # Theme selection
    theme = st.radio(
        strings["theme"],
        ["Light", "Dark", "System"],
        index=["Light", "Dark", "System"].index(st.session_state.theme),
        horizontal=True
    )
    st.session_state.theme = theme
    
    # Color selection
    color = st.selectbox(
        strings["color"],
        ["Blue", "Green", "Red", "Purple", "Orange"],
        index=["Blue", "Green", "Red", "Purple", "Orange"].index(st.session_state.color),
    )
    st.session_state.color = color

    st.divider()
    st.markdown("### 🎮 Player Profile")
    player_name = st.text_input(
        "Player Name (for leaderboard)",
        value=st.session_state.player_name,
        max_chars=20,
        key="player_name_input"
    )
    st.session_state.player_name = player_name.strip() or "Player1"

    lb_entry = st.session_state.leaderboard.get(
        st.session_state.player_name, {"xp": 0, "analyses": 0}
    )
    current_xp = lb_entry.get("xp", 0)
    current_level = get_level(current_xp)
    progress_in_level = xp_progress_in_level(current_xp)

    st.markdown(f"**Level {current_level}** &nbsp;•&nbsp; {current_xp} XP")
    st.progress(progress_in_level / 100)
    st.caption(f"{100 - progress_in_level} XP to Level {current_level + 1}")

    usage_count = st.session_state.persist.get("usage_count", 0)
    if not st.session_state.persist.get("editing_unlocked", False):
        capped = min(usage_count, UNLOCK_USES_REQUIRED)
        st.caption(f"🔒 Keyword editing: {capped}/{UNLOCK_USES_REQUIRED} analyses")

    st.divider()
    st.markdown("### " + strings["about"])
    st.info(strings["about_text"])

# ============================================================================
# COLOR AND THEME CONFIGURATION
# ============================================================================

color_map = {
    "Blue": "#0066cc",
    "Green": "#28a745",
    "Red": "#dc3545",
    "Purple": "#6f42c1",
    "Orange": "#fd7e14"
}

primary_color = color_map.get(st.session_state.color, "#0066cc")

# Apply theme CSS
if st.session_state.theme == "Dark":
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
        color: #c9d1d9;
    }
    [data-testid="stSidebar"] {
        background-color: #161b22;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# WARNING GRID RENDERER (side-by-side compact cards)
# ============================================================================

RISK_LABEL_MAP = {
    "very_high": "Very High",
    "high": "High",
    "medium_high": "Medium-High",
    "medium": "Medium"
}
URGENCY_LABEL_MAP = {
    "immediate": "Immediate",
    "high": "High",
    "medium": "Medium"
}
RISK_COLOR_MAP = {
    "very_high": "#dc3545",
    "high": "#fd7e14",
    "medium_high": "#e0a800",
    "medium": "#6c757d"
}

def render_warning_grid(warning_list, cols=3):
    """Render warnings as compact side-by-side cards, `cols` per row."""
    for i in range(0, len(warning_list), cols):
        row = warning_list[i:i + cols]
        columns = st.columns(cols)
        for col, warning in zip(columns, row):
            risk_label = RISK_LABEL_MAP.get(warning["risk"], warning["risk"])
            urgency_label = URGENCY_LABEL_MAP.get(warning["urgency"], warning["urgency"])
            border_color = RISK_COLOR_MAP.get(warning["risk"], "#6c757d")
            with col:
                st.markdown(
                    f"""
                    <div style="
                        border-left: 4px solid {border_color};
                        background-color: rgba(128,128,128,0.08);
                        border-radius: 6px;
                        padding: 10px 12px;
                        margin-bottom: 10px;
                        min-height: 90px;
                    ">
                        <div style="font-size: 13px; font-weight: 600; margin-bottom: 6px;">
                            ⚠️ {warning['message']}
                        </div>
                        <div style="font-size: 11px; opacity: 0.8;">
                            Risk: <code>{risk_label}</code> &nbsp;|&nbsp; Urgency: <code>{urgency_label}</code>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ============================================================================
# MAIN CONTENT
# ============================================================================

st.title(strings["title"])
st.markdown(f"<h3 style='color: {primary_color};'>{strings['subtitle']}</h3>", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size: 15px; font-weight: 600; letter-spacing: 0.5px; opacity: 0.75; margin-top: -8px;'>"
    "Stop. Scan. Stay Safe."
    "</p>",
    unsafe_allow_html=True
)

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Analyze",
    f"📋 {strings['emergency_guide']}",
    f"📱 {strings['emergency_resources']}",
    "🏆 Leaderboard"
])

# ============================================================================
# TAB 1: ANALYZE
# ============================================================================

with tab1:
    st.markdown(f"<h3 style='color: {primary_color};'>Enter Details to Check</h3>", unsafe_allow_html=True)
    
    user_text = st.text_area(
        strings["enter_text"],
        height=150,
        placeholder="Paste the suspicious message here..."
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(strings["analyze_btn"], use_container_width=True, type="primary"):
            if user_text.strip():
                effective_table = get_effective_keyword_table()
                risk_level, warnings = detect_scams(user_text, keyword_table=effective_table)

                duplicate = is_duplicate_text(user_text)
                gibberish = is_gibberish_text(user_text)

                if duplicate:
                    st.error("No duplicates for XP Scams 👾")
                elif gibberish:
                    new_total_xp = award_xp(st.session_state.player_name, GIBBERISH_XP_PENALTY)
                    register_text(user_text)
                    save_data(st.session_state.persist)
                    st.error(f"🤖 Gibberish detected — {GIBBERISH_XP_PENALTY} XP ({new_total_xp} total)")
                else:
                    # Track usage count (for unlocking keyword editing)
                    st.session_state.persist["usage_count"] = st.session_state.persist.get("usage_count", 0) + 1

                    # Award XP: base for analyzing + bonus per warning found (capped)
                    xp_gained = 10 + min(len(warnings), 10) * 3
                    new_total_xp = award_xp(st.session_state.player_name, xp_gained)
                    register_text(user_text)

                    save_data(st.session_state.persist)
                    st.toast(f"+{xp_gained} XP earned! ({new_total_xp} total)", icon="✨")

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
                    st.markdown(f"### {strings['warning_signs']} ({len(warnings)})")
                    MAX_SHOWN = 12
                    render_warning_grid(warnings[:MAX_SHOWN], cols=3)

                    remaining = warnings[MAX_SHOWN:]
                    if remaining:
                        with st.expander(f"➕ Show {len(remaining)} more warning term(s)"):
                            render_warning_grid(remaining, cols=3)
                else:
                    st.info(strings["no_warnings"])
                
                # Emergency checklist for high risk
                if risk_level == "high_risk":
                    st.divider()
                    st.markdown(f"### {strings['checklist_title']}")
                    for item in strings["checklist"]:
                        st.write(item)
            else:
                st.info(strings["no_analysis"])

# ============================================================================
# TAB 2: EMERGENCY GUIDE
# ============================================================================

with tab2:
    st.markdown(f"<h3 style='color: {primary_color};'>{strings['checklist_title']}</h3>", unsafe_allow_html=True)
    
    for item in strings["checklist"]:
        st.write(item)
    
    st.divider()
    st.markdown(f"### {strings['prevention_title']}")
    for tip in strings["prevention_tips"]:
        st.write(f"✓ {tip}")

    st.divider()
    st.markdown("### 🚩 High-Risk Keyword Reference")

    effective_table = get_effective_keyword_table()
    is_custom = st.session_state.persist.get("active_keywords") is not None
    caption_suffix = " (custom edited list)" if is_custom else ""
    st.caption(f"{len(effective_table)} scam-related terms are monitored{caption_suffix}. Search or browse the full list below.")

    risk_label_map = {
        "very_high": "Very high",
        "high": "High",
        "medium_high": "Medium–high",
        "medium": "Medium"
    }
    urgency_label_map = {
        "immediate": "Immediate",
        "high": "High",
        "medium": "Medium"
    }
    risk_reverse_map = {v: k for k, v in risk_label_map.items()}
    urgency_reverse_map = {v: k for k, v in urgency_label_map.items()}

    search_term = st.text_input("🔎 Search keyword", key="keyword_search", placeholder="e.g. otp, refund, arrest...")

    all_words = sorted(effective_table.keys())
    if search_term.strip():
        all_words = [w for w in all_words if search_term.strip().lower() in w]

    if all_words:
        table_data = {
            "Word": [w.replace("-", " ").title() for w in all_words],
            "Risk Level": [risk_label_map.get(effective_table[w][0], effective_table[w][0]) for w in all_words],
            "Urgency": [urgency_label_map.get(effective_table[w][1], effective_table[w][1]) for w in all_words]
        }
        st.dataframe(table_data, use_container_width=True, hide_index=True)
    else:
        st.info("No matching keywords found.")

    # ------------------------------------------------------------------
    # EDITABLE KEYWORD TABLE (password-gated, unlocks after 10 analyses)
    # ------------------------------------------------------------------
    st.divider()
    st.markdown("### ✏️ Edit Keyword Table")

    usage_count = st.session_state.persist.get("usage_count", 0)
    editing_unlocked = st.session_state.persist.get("editing_unlocked", False)

    if not editing_unlocked and usage_count < UNLOCK_USES_REQUIRED:
        st.info(
            f"🔒 Editing is locked. Analyze {UNLOCK_USES_REQUIRED - usage_count} more "
            f"message(s) to unlock this feature. Progress: {usage_count}/{UNLOCK_USES_REQUIRED}"
        )
    elif not editing_unlocked:
        st.success(f"🎉 You've analyzed {usage_count} messages — editing is available! Enter the password to unlock it.")
        pw = st.text_input("Password", type="password", key="edit_password_input")
        if st.button("Unlock Editing"):
            if pw == EDIT_PASSWORD:
                st.session_state.persist["editing_unlocked"] = True
                save_data(st.session_state.persist)
                st.session_state.just_unlocked = True
                st.rerun()
            else:
                st.error("Incorrect password.")
    else:
        if st.session_state.just_unlocked:
            st.success("You unlocked editing!")
            st.balloons()
            st.session_state.just_unlocked = False

        st.caption(
            "Add, remove, or edit rows below. Use the ➕ row at the bottom to add a new word, "
            "or the trash icon on a row to delete it. Click **Save Changes** when done."
        )

        base_table = effective_table
        edit_rows = [
            {
                "Word": w.replace("-", " ").title(),
                "Risk": risk_label_map.get(v[0], v[0]),
                "Urgency": urgency_label_map.get(v[1], v[1])
            }
            for w, v in sorted(base_table.items())
        ]

        edited = st.data_editor(
            edit_rows,
            num_rows="dynamic",
            use_container_width=True,
            hide_index=True,
            column_config={
                "Word": st.column_config.TextColumn("Word", required=True),
                "Risk": st.column_config.SelectboxColumn(
                    "Risk", options=["Very high", "High", "Medium–high", "Medium"], required=True
                ),
                "Urgency": st.column_config.SelectboxColumn(
                    "Urgency", options=["Immediate", "High", "Medium"], required=True
                ),
            },
            key="keyword_data_editor"
        )

        col_save, col_reset = st.columns(2)
        with col_save:
            if st.button("💾 Save Changes", use_container_width=True, type="primary"):
                new_table = {}
                for row in edited:
                    word_raw = str(row.get("Word", "")).strip().lower()
                    if not word_raw:
                        continue
                    word_key = word_raw.replace(" ", "-")
                    risk_key = risk_reverse_map.get(row.get("Risk"), "medium")
                    urgency_key = urgency_reverse_map.get(row.get("Urgency"), "medium")
                    new_table[word_key] = [risk_key, urgency_key]
                st.session_state.persist["active_keywords"] = new_table
                save_data(st.session_state.persist)
                st.success(f"Saved! {len(new_table)} keyword(s) now active.")
                st.rerun()
        with col_reset:
            if st.button("↩️ Reset to Default List", use_container_width=True):
                st.session_state.persist["active_keywords"] = None
                save_data(st.session_state.persist)
                st.success("Reset to the built-in keyword list.")
                st.rerun()

# ============================================================================
# TAB 3: EMERGENCY RESOURCES
# ============================================================================

with tab3:
    st.markdown(f"<h3 style='color: {primary_color};'>{strings['resources']}</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📞 Cybercrime Helpline")
        st.metric("Helpline Number", "1930")
        st.write("Available 24/7 for cybercrime complaints")
    
    with col2:
        st.markdown("### 🌐 Cybercrime Portal")
        st.write("[National Cybercrime Reporting Portal](https://cybercrime.gov.in/)")
        st.write("File complaints online")
    
    st.divider()
    
    st.markdown(f"### {strings['bank_title']}")
    st.info(
        f"{strings['bank_note']}\n\n"
        "- **HDFC Bank**: 1860-419-0888\n"
        "- **ICICI Bank**: 1860-102-4332\n"
        "- **SBI**: 1800-112-211\n"
        "- **Axis Bank**: 1800-209-5959\n"
        "- **Yes Bank**: 1860-106-7777\n"
        "- **Kotak Bank**: 1800-266-6565\n"
        "- **IndusInd Bank**: 1860-123-0456\n\n"
        "*Note: Always verify from official bank website.*"
    )

# ============================================================================
# TAB 4: LEADERBOARD
# ============================================================================

with tab4:
    st.markdown(f"<h3 style='color: {primary_color};'>🏆 Leaderboard</h3>", unsafe_allow_html=True)
    st.caption("Earn XP by analyzing messages. More warning signs found = more XP. Level up as you go!")

    leaderboard = st.session_state.leaderboard

    if leaderboard:
        rows = []
        for name, data in leaderboard.items():
            xp = data.get("xp", 0)
            rows.append({
                "Player": name,
                "Level": get_level(xp),
                "XP": xp,
                "Analyses": data.get("analyses", 0),
                "Last Active": data.get("last_active", "-")
            })
        rows.sort(key=lambda r: r["XP"], reverse=True)
        for i, r in enumerate(rows, 1):
            r["Rank"] = i
        rows = [{"Rank": r["Rank"], "Player": r["Player"], "Level": r["Level"],
                  "XP": r["XP"], "Analyses": r["Analyses"], "Last Active": r["Last Active"]} for r in rows]

        st.dataframe(rows, use_container_width=True, hide_index=True)

        st.divider()
        top3 = rows[:3]
        medals = ["🥇", "🥈", "🥉"]
        cols = st.columns(len(top3)) if top3 else []
        for medal, col, r in zip(medals, cols, top3):
            with col:
                st.markdown(f"### {medal} {r['Player']}")
                st.metric("XP", r["XP"])
                st.caption(f"Level {r['Level']} • {r['Analyses']} analyses")
    else:
        st.info("No players yet — analyze a message in the 🔍 Analyze tab to appear on the leaderboard!")

    st.divider()
    st.markdown("### How XP works")
    st.write("✓ +10 XP for every message you analyze")
    st.write("✓ +3 XP per warning sign detected (up to +30 bonus per message)")
    st.write("✓ Level up every 100 XP")
    st.write("✓ Analyze 10 messages to unlock keyword table editing (📋 Emergency Guide tab)")

# ============================================================================
# DETECTION HISTORY
# ============================================================================

st.divider()

if st.session_state.history:
    with st.expander(f"📋 {strings['history']} ({len(st.session_state.history)})"):
        for idx, record in enumerate(reversed(st.session_state.history[-10:]), 1):
            risk_emoji = "🟢" if record["risk"] == "safe" else "🟡" if record["risk"] == "suspicious" else "🔴"
            st.write(f"{idx}. {record['timestamp']} | {risk_emoji} {record['text']}")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button(strings["clear_history"], use_container_width=True):
                st.session_state.history = []
                st.rerun()

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown(
    f"<p style='text-align: center; color: #888; font-size: 12px;'>"
    f"{strings['footer']}"
    "</p>",
    unsafe_allow_html=True
)