import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# إعدادات الصفحة
st.set_page_config(layout="wide", page_title="Calculus Graphical Quiz")

# --- CSS مخصص للتنسيق (RTL/LTR) ---
st.markdown("""
<style>
    .rtl-box {
        direction: rtl;
        text-align: right;
        font-family: 'Arial';
        font-size: 20px;
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-right: 5px solid #2980b9;
        margin-bottom: 10px;
    }
    .ltr-box {
        direction: ltr;
        text-align: left;
        font-family: 'Arial';
        font-size: 20px;
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2980b9;
        margin-bottom: 10px;
    }
    .stButton button {
        width: 100%;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- دوال الرسم (Graphic Engine) ---

def plot_textbook_graph(x, y, title=None):
    """رسم بياني نظيف بأسلوب الكتاب المدرسي"""
    fig, ax = plt.subplots(figsize=(5, 4))
    
    # رسم المنحنى
    ax.plot(x, y, color='#007acc', linewidth=2.5)
    
    # تنسيق المحاور في المنتصف
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # إضافة الأسهم
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    
    # الشبكة
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
    
    # حدود الرسم
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    
    # إخفاء الأرقام ليكون التركيز على الشكل العام
    ax.set_xticks([-2, -1, 1, 2])
    ax.set_yticks([-2, -1, 1, 2])
    
    if title:
        ax.set_title(title, fontsize=10, color='gray')
        
    plt.tight_layout()
    return fig

# --- بيانات الأسئلة (الشروط فقط بصيغة MathJax) ---

def get_questions():
    x = np.linspace(-3.5, 3.5, 400)
    questions = []
    
    # --- السؤال 37 ---
    # الدوال التقريبية للرسم
    def q37_func(v): return -0.5*( (v**4)/4 + (v**3)/3 - (v**2)/2 - v )
    def q37_w1(v): return v**3 - 3*v
    def q37_w2(v): return -(v**2) + 1
    def q37_w3(v): return np.sin(v)

    q37 = {
        "id": 37,
        # تم كتابة الشروط فقط بدقة MathJax
        "ar": r"""
        $$
        \begin{aligned}
        &f(0)=0 \\
        &f'(x) > 0 \quad \text{عندما} \quad x < -1 \quad \text{و} \quad -1 < x < 1 \\
        &f'(x) < 0 \quad \text{عندما} \quad x > 1 \\
        &f''(x) > 0 \quad \text{عندما} \quad x < -1, \ 0 < x < 1, \ x > 1 \\
        &f''(x) < 0 \quad \text{عندما} \quad -1 < x < 0
        \end{aligned}
        $$
        """,
        "en": r"""
        $$
        \begin{aligned}
        &f(0)=0 \\
        &f'(x) > 0 \quad \text{for} \quad x < -1 \quad \text{and} \quad -1 < x < 1 \\
        &f'(x) < 0 \quad \text{for} \quad x > 1 \\
        &f''(x) > 0 \quad \text{for} \quad x < -1, \ 0 < x < 1, \ x > 1 \\
        &f''(x) < 0 \quad \text{for} \quad -1 < x < 0
        \end{aligned}
        $$
        """,
        "correct_func": q37_func,
        "distractors": [q37_w1, q37_w2, q37_w3]
    }
    questions.append(q37)

    # --- السؤال 38 ---
    def q38_func(v): return 2 + np.arctan(v)
    def q38_w1(v): return 2 + v**3
    def q38_w2(v): return 2 + v**2
    def q38_w3(v): return 2 - np.arctan(v)

    q38 = {
        "id": 38,
        "ar": r"""
        $$
        \begin{aligned}
        &f(0)=2 \\
        &f'(x) > 0 \quad \text{لجميع قيم } x \\
        &f'(0)=1 \\
        &f''(x) > 0 \quad \text{عندما} \quad x < 0 \\
        &f''(x) < 0 \quad \text{عندما} \quad x > 0
        \end{aligned}
        $$
        """,
        "en": r"""
        $$
        \begin{aligned}
        &f(0)=2 \\
        &f'(x) > 0 \quad \text{for all } x \\
        &f'(0)=1 \\
        &f''(x) > 0 \quad \text{for} \quad x < 0 \\
        &f''(x) < 0 \quad \text{for} \quad x > 0
        \end{aligned}
        $$
        """,
        "correct_func": q38_func,
        "distractors": [q38_w1, q38_w2, q38_w3]
    }
    questions.append(q38)

    # --- السؤال 39 ---
    def q39_func(v): return 2*v**2 - v**4
    def q39_w1(v): return v**3
    def q39_w2(v): return v**2
    def q39_w3(v): return -(2*v**2 - v**4)

    q39 = {
        "id": 39,
        "ar": r"""
        $$
        \begin{aligned}
        &f(0)=0, \ f(-1)=-1, \ f(1)=1 \\
        &f'(x) > 0 \quad \text{عندما} \quad x < -1 \quad \text{و} \quad 0 < x < 1 \\
        &f'(x) < 0 \quad \text{عندما} \quad -1 < x < 0 \quad \text{و} \quad x > 1 \\
        &f''(x) < 0 \quad \text{عندما} \quad x < 0 \quad \text{و} \quad x > 0
        \end{aligned}
        $$
        """,
        "en": r"""
        $$
        \begin{aligned}
        &f(0)=0, \ f(-1)=-1, \ f(1)=1 \\
        &f'(x) > 0 \quad \text{for} \quad x < -1 \quad \text{and} \quad 0 < x < 1 \\
        &f'(x) < 0 \quad \text{for} \quad -1 < x < 0 \quad \text{and} \quad x > 1 \\
        &f''(x) < 0 \quad \text{for} \quad x < 0 \quad \text{and} \quad x > 0
        \end{aligned}
        $$
        """,
        "correct_func": q39_func,
        "distractors": [q39_w1, q39_w2, q39_w3]
    }
    questions.append(q39)

    # --- السؤال 40 ---
    def q40_func(v): return (np.abs(v-1))**(2/3)
    def q40_w1(v): return (v-1)**2
    def q40_w2(v): return -(v-1)**2
    def q40_w3(v): return (v-1)**3

    q40 = {
        "id": 40,
        "ar": r"""
        $$
        \begin{aligned}
        &f(1)=0 \\
        &f'(x) < 0 \quad \text{عندما} \quad x < 1 \\
        &f'(x) > 0 \quad \text{عندما} \quad x > 1 \\
        &f''(x) < 0 \quad \text{عندما} \quad x < 1 \quad \text{و} \quad x > 1
        \end{aligned}
        $$
        """,
        "en": r"""
        $$
        \begin{aligned}
        &f(1)=0 \\
        &f'(x) < 0 \quad \text{for} \quad x < 1 \\
        &f'(x) > 0 \quad \text{for} \quad x > 1 \\
        &f''(x) < 0 \quad \text{for} \quad x < 1 \quad \text{and} \quad x > 1
        \end{aligned}
        $$
        """,
        "correct_func": q40_func,
        "distractors": [q40_w1, q40_w2, q40_w3]
    }
    questions.append(q40)
    
    return questions

# --- منطق التطبيق ---

# تهيئة الحالة (Session State)
if 'current_q_index' not in st.session_state:
    st.session_state['current_q_index'] = 0
if 'shuffled_options' not in st.session_state:
    st.session_state['shuffled_options'] = None

questions = get_questions()
q_idx = st.session_state['current_q_index']
current_q = questions[q_idx]

# خلط الخيارات عند تغيير السؤال فقط
if st.session_state['shuffled_options'] is None:
    options = [{'func': current_q['correct_func'], 'is_correct': True}]
    for dist in current_q['distractors']:
        options.append({'func': dist, 'is_correct': False})
    random.shuffle(options)
    st.session_state['shuffled_options'] = options

options = st.session_state['shuffled_options']

# --- الواجهة ---

# أزرار التنقل (بدون رقم السؤال)
c_prev, c_space, c_next = st.columns([1, 6, 1])
with c_prev:
    if st.button("⬅ Previous"):
        if q_idx > 0:
            st.session_state['current_q_index'] -= 1
            st.session_state['shuffled_options'] = None
            st.rerun()
with c_next:
    if st.button("Next ➡"):
        if q_idx < len(questions) - 1:
            st.session_state['current_q_index'] += 1
            st.session_state['shuffled_options'] = None
            st.rerun()

st.write("") # مسافة فارغة

# عرض نص السؤال (الشروط فقط)
col_en, col_ar = st.columns(2)
with col_en:
    st.markdown(f'<div class="ltr-box">{current_q["en"]}</div>', unsafe_allow_html=True)
with col_ar:
    st.markdown(f'<div class="rtl-box">{current_q["ar"]}</div>', unsafe_allow_html=True)

st.write("---")

# عرض الخيارات
x_vals = np.linspace(-3.2, 3.2, 500)

col1, col2 = st.columns(2)

def show_option(container, index, option_data):
    with container:
        y_vals = option_data['func'](x_vals)
        fig = plot_textbook_graph(x_vals, y_vals, title=None)
        st.pyplot(fig, use_container_width=True)
        
        # زر الاختيار
        if st.button(f"Choose Graph {index+1}", key=f"btn_{q_idx}_{index}"):
            if option_data['is_correct']:
                st.success("✅ Correct Answer! إجابة صحيحة")
                st.balloons()
            else:
                st.error("❌ Incorrect Answer.")

# الصف الأول
show_option(col1, 0, options[0])
show_option(col2, 1, options[1])

# فاصل
st.write("")

# الصف الثاني
col3, col4 = st.columns(2)
show_option(col3, 2, options[2])
show_option(col4, 3, options[3])
