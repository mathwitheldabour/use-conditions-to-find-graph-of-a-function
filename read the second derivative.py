import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# إعدادات الصفحة
st.set_page_config(layout="wide", page_title="Calculus Quiz Bank")

# --- CSS للتنسيق ---
st.markdown("""
<style>
    .rtl-box {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-right: 6px solid #2980b9;
        margin-bottom: 10px;
    }
    .ltr-box {
        direction: ltr;
        text-align: left;
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 6px solid #2980b9;
        margin-bottom: 10px;
    }
    .header-text-ar { text-align: right; font-weight: bold; font-size: 20px; margin-bottom: 5px; }
    .header-text-en { text-align: left; font-weight: bold; font-size: 20px; margin-bottom: 5px; }
    .stButton button { width: 100%; font-weight: bold; }
    /* تنسيق النتيجة النهائية */
    .final-score {
        text-align: center;
        padding: 30px;
        background-color: #d4edda;
        border-radius: 10px;
        border: 2px solid #c3e6cb;
        color: #155724;
        font-size: 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- دوال الرسم (كما هي) ---
def plot_textbook_graph(x, y):
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x, y, color='#007acc', linewidth=3)
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

# --- بنك الأسئلة (Question Bank) ---
# هنا تضع كل الأسئلة التي لديك (50، 100 سؤال...)
def get_full_question_bank():
    bank = []
    
    # --- سؤال 1 (من النوع 37) ---
    bank.append({
        "id": "q1", # معرف فريد
        "en_latex": r'''
        \begin{aligned}
        &f(0)=0 \\
        &f'(x) > 0 \quad \text{for} \quad x < -1 \quad \text{and} \quad -1 < x < 1 \\
        &f'(x) < 0 \quad \text{for} \quad x > 1 \\
        &f''(x) > 0 \quad \text{for} \quad x < -1, \ 0 < x < 1, \ x > 1 \\
        &f''(x) < 0 \quad \text{for} \quad -1 < x < 0
        \end{aligned}
        ''',
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

    # --- سؤال 2 (من النوع 38) ---
    bank.append({
        "id": "q2",
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

    # --- سؤال 3 (من النوع 39) ---
    bank.append({
        "id": "q3",
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

    # --- سؤال 4 (من النوع 40) ---
    bank.append({
        "id": "q4",
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
    
    # --- سؤال 5 (إضافي لتجربة البنك - مقعر لأعلى دائماً) ---
    bank.append({
        "id": "q5",
        "en_latex": r'''
        \begin{aligned}
        &f(0)=0 \\
        &f''(x) > 0 \quad \text{for all } x
        \end{aligned}
        ''',
        "ar_latex": r'''
        \begin{aligned}
        &f(0)=0 \\
        &f''(x) > 0 \quad \text{لجميع قيم } x
        \end{aligned}
        ''',
        "correct_func": lambda v: v**2, # قطع مكافئ لأعلى
        "distractors": [lambda v: -(v**2), lambda v: v**3, lambda v: np.sin(v)]
    })
    
    # ملاحظة: قم بنسخ وتعديل الأسئلة أعلاه لإضافة المزيد للبنك
    
    return bank

# --- إدارة حالة الاختبار (Session State Management) ---

# 1. بدء اختبار جديد (سحب 5 أسئلة عشوائية)
def start_new_quiz():
    full_bank = get_full_question_bank()
    # سحب 5 أسئلة عشوائياً (أو أقل إذا كان البنك صغير)
    num_questions = min(5, len(full_bank))
    selected_questions = random.sample(full_bank, num_questions)
    
    st.session_state['quiz_questions'] = selected_questions
    st.session_state['current_index'] = 0
    st.session_state['score'] = 0
    st.session_state['quiz_finished'] = False
    st.session_state['shuffled_options'] = None # لإعادة خلط الخيارات
    st.session_state['feedback_given'] = False # هل أجاب الطالب على السؤال الحالي؟

if 'quiz_questions' not in st.session_state:
    start_new_quiz()

# --- المتغيرات الحالية ---
questions = st.session_state['quiz_questions']
idx = st.session_state['current_index']
score = st.session_state['score']
is_finished = st.session_state['quiz_finished']

# --- واجهة التطبيق ---

# شريط التقدم والنتيجة الحالية
if not is_finished:
    st.progress((idx) / len(questions))
    st.caption(f"Question {idx + 1} of {len(questions)} | Current Score: {score}")

st.write("---")

# --- حالة: الاختبار انتهى ---
if is_finished:
    final_score_pct = (score / len(questions)) * 100
    
    # رسالة النتيجة
    if final_score_pct == 100:
        msg = "Excellent! درجة كاملة 🎉"
        st.balloons()
    elif final_score_pct >= 80:
        msg = "Great Job! عمل رائع 👏"
    else:
        msg = "Good effort, try again! حاول مرة أخرى 💪"
        
    st.markdown(f"""
    <div class="final-score">
    {msg}<br><br>
    Your Score: {score} / {len(questions)}
    </div>
    """, unsafe_allow_html=True)
    
    # زر إعادة المحاولة
    st.write("")
    if st.button("🔄 Start New Quiz / ابدأ اختباراً جديداً", type="primary"):
        start_new_quiz()
        st.rerun()

# --- حالة: الاختبار جارٍ ---
else:
    curr_q = questions[idx]
    
    # خلط الخيارات للسؤال الحالي (مرة واحدة فقط لكل سؤال)
    if st.session_state['shuffled_options'] is None:
        opts = [{'func': curr_q['correct_func'], 'is_correct': True}]
        for d in curr_q['distractors']:
            opts.append({'func': d, 'is_correct': False})
        random.shuffle(opts)
        st.session_state['shuffled_options'] = opts
    
    opts = st.session_state['shuffled_options']

    # رأس السؤال
    h_en, h_ar = st.columns(2)
    with h_en:
        st.markdown('<div class="header-text-en">Choose the graph that satisfies:</div>', unsafe_allow_html=True)
    with h_ar:
        st.markdown('<div class="header-text-ar">اختر التمثيل البياني الذي يحقق:</div>', unsafe_allow_html=True)

    # عرض الشروط
    col_en, col_ar = st.columns(2)
    with col_en:
        st.markdown('<div class="ltr-box">', unsafe_allow_html=True)
        st.latex(curr_q['en_latex'])
        st.markdown('</div>', unsafe_allow_html=True)
    with col_ar:
        st.markdown('<div class="rtl-box">', unsafe_allow_html=True)
        st.latex(curr_q['ar_latex'])
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")

    # عرض الخيارات
    x_vals = np.linspace(-3.2, 3.2, 500)
    
    # استخدام حاوية للأزرار لتحديث الحالة
    row1 = st.columns(2)
    row2 = st.columns(2)
    
    feedback_placeholder = st.empty() # مكان لعرض النتيجة المؤقتة

    for i, col in enumerate(row1 + row2):
        with col:
            y_vals = opts[i]['func'](x_vals)
            fig = plot_textbook_graph(x_vals, y_vals)
            st.pyplot(fig, use_container_width=True)
            
            # زر الاختيار
            # إذا لم يتم الإجابة بعد، نظهر الأزرار
            if not st.session_state['feedback_given']:
                if st.button(f"Select Graph {i+1}", key=f"btn_{curr_q['id']}_{i}"):
                    # منطق التحقق من الإجابة
                    if opts[i]['is_correct']:
                        st.session_state['score'] += 1
                        st.toast("Correct Answer! ✅")
                    else:
                        st.toast("Wrong Answer ❌")
                    
                    # تسجيل أن الطالب أجاب
                    st.session_state['feedback_given'] = True
                    st.rerun()
            
            # إذا تم الإجابة، نظهر أي إجابة كانت الصحيحة (تمييز بصري)
            else:
                if opts[i]['is_correct']:
                    st.success("✅ Correct Graph")
                else:
                    st.button(f"Graph {i+1}", key=f"disabled_{i}", disabled=True)

    # زر الانتقال للسؤال التالي (يظهر فقط بعد الإجابة)
    if st.session_state['feedback_given']:
        st.write("---")
        btn_text = "Next Question ➡" if idx < len(questions) - 1 else "Show Results 🏁"
        
        if st.button(btn_text, type="primary"):
            if idx < len(questions) - 1:
                st.session_state['current_index'] += 1
                st.session_state['shuffled_options'] = None
                st.session_state['feedback_given'] = False
            else:
                st.session_state['quiz_finished'] = True
            st.rerun()
