import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# إعدادات الصفحة
st.set_page_config(layout="wide", page_title="Calculus Quiz")

# --- CSS مخصص للصناديق الملونة ---
st.markdown("""
<style>
    .rtl-box {
        direction: rtl;
        text-align: right;
        font-family: 'Arial';
        font-size: 18px;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        border-right: 5px solid #2980b9;
        margin-bottom: 5px;
    }
    .ltr-box {
        direction: ltr;
        text-align: left;
        font-family: 'Arial';
        font-size: 18px;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        border-left: 5px solid #2980b9;
        margin-bottom: 5px;
    }
    .stButton button {
        width: 100%;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- دوال الرسم (نفس المنطق السابق) ---
def plot_textbook_graph(x, y):
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x, y, color='#007acc', linewidth=2.5)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xticks([-2, -1, 1, 2])
    ax.set_yticks([-2, -1, 1, 2])
    plt.tight_layout()
    return fig

# --- البيانات (باستخدام نصوص خام r-strings) ---
def get_questions():
    questions = []
    
    # Q37
    questions.append({
        "id": 37,
        # الإنجليزية
        "en_latex": r'''
        \begin{aligned}
        &f(0)=0 \\
        &f'(x) > 0 \quad \text{for} \quad x < -1 \quad \text{and} \quad -1 < x < 1 \\
        &f'(x) < 0 \quad \text{for} \quad x > 1 \\
        &f''(x) > 0 \quad \text{for} \quad x < -1, \ 0 < x < 1, \ x > 1 \\
        &f''(x) < 0 \quad \text{for} \quad -1 < x < 0
        \end{aligned}
        ''',
        # العربية (نستخدم نصوص عربية داخل text)
        "ar_latex": r'''
        \begin{aligned}
        &f(0)=0 \\
        &f'(x) > 0 \quad \text{عندما} \quad x < -1 \quad \text{و} \quad -1 < x < 1 \\
        &f'(x) < 0 \quad \text{عندما} \quad x > 1 \\
        &f''(x) > 0 \quad \text{عندما} \quad x < -1, \ 0 < x < 1, \ x > 1 \\
        &f''(x) < 0 \quad \text{عندما} \quad -1 < x < 0
        \end{aligned}
        ''',
        "correct_func": lambda v: -0.5*((v**4)/4 + (v**3)/3 - (v**2)/2 - v),
        "distractors": [lambda v: v**3 - 3*v, lambda v: -(v**2) + 1, lambda v: np.sin(v)]
    })

    # Q38
    questions.append({
        "id": 38,
        "en_latex": r'''
        \begin{aligned}
        &f(0)=2 \\
        &f'(x) > 0 \quad \text{for all } x \\
        &f'(0)=1 \\
        &f''(x) > 0 \quad \text{for} \quad x < 0 \\
        &f''(x) < 0 \quad \text{for} \quad x > 0
        \end{aligned}
        ''',
        "ar_latex": r'''
        \begin{aligned}
        &f(0)=2 \\
        &f'(x) > 0 \quad \text{لجميع قيم } x \\
        &f'(0)=1 \\
        &f''(x) > 0 \quad \text{عندما} \quad x < 0 \\
        &f''(x) < 0 \quad \text{عندما} \quad x > 0
        \end{aligned}
        ''',
        "correct_func": lambda v: 2 + np.arctan(v),
        "distractors": [lambda v: 2 + v**3, lambda v: 2 + v**2, lambda v: 2 - np.arctan(v)]
    })

    # Q39
    questions.append({
        "id": 39,
        "en_latex": r'''
        \begin{aligned}
        &f(0)=0, \ f(-1)=-1, \ f(1)=1 \\
        &f'(x) > 0 \quad \text{for} \quad x < -1 \quad \text{and} \quad 0 < x < 1 \\
        &f'(x) < 0 \quad \text{for} \quad -1 < x < 0 \quad \text{and} \quad x > 1 \\
        &f''(x) < 0 \quad \text{for} \quad x < 0 \quad \text{and} \quad x > 0
        \end{aligned}
        ''',
        "ar_latex": r'''
        \begin{aligned}
        &f(0)=0, \ f(-1)=-1, \ f(1)=1 \\
        &f'(x) > 0 \quad \text{عندما} \quad x < -1 \quad \text{و} \quad 0 < x < 1 \\
        &f'(x) < 0 \quad \text{عندما} \quad -1 < x < 0 \quad \text{و} \quad x > 1 \\
        &f''(x) < 0 \quad \text{عندما} \quad x < 0 \quad \text{و} \quad x > 0
        \end{aligned}
        ''',
        "correct_func": lambda v: 2*v**2 - v**4,
        "distractors": [lambda v: v**3, lambda v: v**2, lambda v: -(2*v**2 - v**4)]
    })

    # Q40
    questions.append({
        "id": 40,
        "en_latex": r'''
        \begin{aligned}
        &f(1)=0 \\
        &f'(x) < 0 \quad \text{for} \quad x < 1 \\
        &f'(x) > 0 \quad \text{for} \quad x > 1 \\
        &f''(x) < 0 \quad \text{for} \quad x < 1 \quad \text{and} \quad x > 1
        \end{aligned}
        ''',
        "ar_latex": r'''
        \begin{aligned}
        &f(1)=0 \\
        &f'(x) < 0 \quad \text{عندما} \quad x < 1 \\
        &f'(x) > 0 \quad \text{عندما} \quad x > 1 \\
        &f''(x) < 0 \quad \text{عندما} \quad x < 1 \quad \text{و} \quad x > 1
        \end{aligned}
        ''',
        "correct_func": lambda v: (np.abs(v-1))**(2/3),
        "distractors": [lambda v: (v-1)**2, lambda v: -(v-1)**2, lambda v: (v-1)**3]
    })
    
    return questions

# --- إدارة التطبيق ---
if 'q_idx' not in st.session_state:
    st.session_state['q_idx'] = 0
if 'shuffled_opts' not in st.session_state:
    st.session_state['shuffled_opts'] = None

all_questions = get_questions()
idx = st.session_state['q_idx']
curr_q = all_questions[idx]

# خلط الخيارات
if st.session_state['shuffled_opts'] is None:
    opts = [{'func': curr_q['correct_func'], 'is_correct': True}]
    for d in curr_q['distractors']:
        opts.append({'func': d, 'is_correct': False})
    random.shuffle(opts)
    st.session_state['shuffled_opts'] = opts

opts = st.session_state['shuffled_opts']

# --- أزرار التنقل ---
c1, c2, c3 = st.columns([1, 6, 1])
with c1:
    if st.button("⬅ Previous"):
        if idx > 0:
            st.session_state['q_idx'] -= 1
            st.session_state['shuffled_opts'] = None
            st.rerun()
with c3:
    if st.button("Next ➡"):
        if idx < len(all_questions) - 1:
            st.session_state['q_idx'] += 1
            st.session_state['shuffled_opts'] = None
            st.rerun()

st.write("")

# --- عرض الشروط (الحل السحري لظهور المعادلات) ---
col_en, col_ar = st.columns(2)

with col_en:
    # نفتح الصندوق بكود HTML
    st.markdown('<div class="ltr-box">', unsafe_allow_html=True)
    # نكتب المعادلة باستخدام st.latex لضمان التنسيق
    st.latex(curr_q['en_latex'])
    # نغلق الصندوق
    st.markdown('</div>', unsafe_allow_html=True)

with col_ar:
    st.markdown('<div class="rtl-box">', unsafe_allow_html=True)
    st.latex(curr_q['ar_latex'])
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- عرض الرسومات ---
x_vals = np.linspace(-3.2, 3.2, 500)
row1 = st.columns(2)
row2 = st.columns(2)

for i, col in enumerate(row1 + row2):
    with col:
        y_vals = opts[i]['func'](x_vals)
        fig = plot_textbook_graph(x_vals, y_vals)
        st.pyplot(fig, use_container_width=True)
        if st.button(f"Choose Graph {i+1}", key=f"btn_{idx}_{i}"):
            if opts[i]['is_correct']:
                st.success("✅ Correct! إجابة صحيحة")
                st.balloons()
            else:
                st.error("❌ Incorrect Answer")
