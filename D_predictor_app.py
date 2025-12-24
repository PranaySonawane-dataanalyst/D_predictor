
# installing required libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import time
import joblib

model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

# --- Sidebar ---

with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu',
        options=['Home', 'Project', 'Contact',],
        default_index=0,
        menu_icon='cast',
        icons=['house-door', 'book', 'envelope'],
        styles={"background-color": "white", "color": "black", "outline-color": "black"}
    )

    st.sidebar.markdown('---')
    st.sidebar.markdown("""
    <div style='text-align: center; font-weight: 600; font-size: 18px;'>
        : How To Use :
    </div>
    """, unsafe_allow_html=True)

    # Create a placeholder for video
    video_container = st.empty()

    # Reset video on page change
    if selected == "Home":
        video_container.video(r"Intro Video Of D_predictor App.mp4", start_time=0.0)

    elif selected == "Project":
        video_container.video(r"Intro Video Of D_predictor App.mp4", start_time=0.0)

    elif selected == "Contact":
        video_container.video(r"Intro Video Of D_predictor App.mp4", start_time=0.0)
    else:
        pass

if selected == 'Home':
    st.session_state.name_disabled = False
    st.session_state.reset_triggered = True
    # Page Title
    st.title("🩸 Diabetes Predictor")
    st.write("### Empowering Early Detection Through Data & Machine Learning")

    st.markdown("---")

    # Why I Made This App
    st.subheader("🤖 Why I Made This App")
    st.write("""
        Diabetes is one of the fastest-growing health challenges in the world.  
        Many people live with diabetes without realizing it until complications arise.  
        This app was built to **raise awareness** and help users **predict their diabetes risk** 
        using **machine learning** — in a simple and interactive way.
        """)

    st.markdown("---")

    # Introduction to Diabetes
    st.subheader("🩺 Introduction to Diabetes")
    st.write("""
        **Diabetes mellitus**, commonly known as **diabetes**, is a chronic condition that occurs when 
        the body either doesn’t produce enough insulin or cannot effectively use the insulin it produces.  
        Insulin is a hormone responsible for regulating blood glucose (sugar) levels. Without proper insulin 
        function, glucose builds up in the blood, leading to serious health complications over time.

        There are primarily two major types of diabetes:
        - **Type 1 Diabetes:** An autoimmune condition where the body attacks insulin-producing cells in the pancreas.  
        - **Type 2 Diabetes:** A metabolic disorder often linked to lifestyle factors such as poor diet, lack of exercise, and obesity.
        """)

    # Early Detection Section
    st.markdown("### 🌟 Importance of Early Detection")
    st.write("""
        Detecting diabetes **early** can make a significant difference in a person’s health and quality of life.  
        Early diagnosis allows for:
        - Better **blood sugar management** through diet, exercise, and medication.  
        - Prevention of severe complications such as **heart disease**, **kidney failure**, **nerve damage**, and **vision loss**.  
        - Improved **energy levels** and overall well-being.  
        - The opportunity to **reverse prediabetes** or delay the progression of Type 2 diabetes.
        """)

    # Late Detection Section
    st.markdown("### ⚠️ Risks of Late Detection")
    st.write("""
        Failing to identify diabetes in its early stages can have serious and irreversible consequences.  
        Late diagnosis often leads to:
        - **Chronic fatigue**, blurred vision, and unexplained weight loss.  
        - Damage to vital organs including the **heart**, **eyes**, **kidneys**, and **nerves**.  
        - Increased risk of **stroke**, **foot ulcers**, and **amputations**.  
        - Higher long-term medical costs and reduced quality of life.
        """)

    st.markdown("---")

    # How This App Works
    st.subheader("🧮 How This App Works")
    st.write("""
        This is a **Diabetes Prediction App** that provides predictions based on user input values  
        using a **Logistic Regression Machine Learning Model**.  
        The model analyzes the input features — such as glucose level, BMI, age, blood pressure, etc. —  
        to estimate the likelihood of having diabetes.
        """)

    st.info(
        "💡 *Note: This app is for educational and awareness purposes only and should not replace professional medical advice.*")

    st.markdown("---")

    # Tools / Author Section
    st.markdown("### 🧰 Tools & Libraries Used")
    st.write("""
        - 🐍 **Python**
        - 🎨 **Streamlit**
        - 🤖 **Machine Learning**
        - ☁️ **Google Colab**
        - 💻 **PyCharm**
        - 📊 **Matplotlib**, **Seaborn**
        - 🧮 **Scikit-learn (Sklearn)**, **NumPy**, **Pandas**
        """)

    # Author Info
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: grey; font-size: 14px;'>
            <b>Author :</b> Pranay Rohidas Sonawane<br>
            <b>Year Created :</b> 2025<br>
            <b>© Diabetes Predictor | Powered by Streamlit</b>
        </div>
        """,
        unsafe_allow_html=True
    )


elif selected == 'Project':
    # Initialize Default session_state for user info

    if "identity" not in st.session_state:
        st.session_state.identity = 'Who Are You❓'
    if "title" not in st.session_state:
        st.session_state.title = ''
    if "first_name" not in st.session_state:
        st.session_state.first_name = ''
    if "middle_name" not in st.session_state:
        st.session_state.middle_name = ''
    if "last_name" not in st.session_state:
        st.session_state.last_name = ''
    if "identity_expander" not in st.session_state:
        st.session_state.identity_expander = True
    if "reset_triggered" not in st.session_state:
        st.session_state.reset_triggered = False
    if 'name_disabled' not in st.session_state:
        st.session_state.name_disabled = False

    # Initialize Default session_state for patient info
    if "patient_reset_triggered1" not in st.session_state:
        st.session_state.patient_reset_triggered1 = False
    if "patient_reset_triggered2" not in st.session_state:
        st.session_state.patient_reset_triggered2 = False
    if "disable_column" not in st.session_state:
        st.session_state.disable_column = False
    if "text" not in st.session_state:
        st.session_state.text = "💾Patients Data"
    if "text_triggered" not in st.session_state:
        st.session_state.text_triggered = False
    if "edited_table" not in st.session_state:
        st.session_state.edited_table = pd.DataFrame(columns = [
            "Patient_name", "Age", "Gender", "BMI", "BloodPressure", "Glucose",
            "Insulin", "SkinThickness", "FamilyHistory",
            "Exercise_Occasionally", "Exercise_Sometimes", "Exercise_Yes",
            "Smoking_Occasionally", "Smoking_Yes", "Alcohol_Occasionally", "Alcohol_Yes"
        ])

    if "final_table" not in st.session_state:
        st.session_state.final_table = pd.DataFrame(columns = [
            "Patient_name", "Age", "Gender", "BMI", "BloodPressure", "Glucose",
            "Insulin", "SkinThickness", "FamilyHistory",
            "Exercise_Occasionally", "Exercise_Sometimes", "Exercise_Yes",
            "Smoking_Occasionally", "Smoking_Yes", "Alcohol_Occasionally", "Alcohol_Yes", "Outcome"
        ])

    if st.session_state.text_triggered:
        st.session_state.text = "📋Patients Reports"
    else:
        st.session_state.text = "💾Patients Data"

    # THIS IS CORRECT ⬇
    if "table_switch" not in st.session_state:
        st.session_state.table_switch = False  # default: show edited_table


    # ----------------- DISPLAY ACTIVE TABLE -----------------

    if "Perspective" not in st.session_state:
        st.session_state.Perspective = None

    # A trigger to change perspective on next rerun
    if "perspective_trigger" not in st.session_state:
        st.session_state.perspective_trigger = None

    # ------------------ Handle Perspective Change Before Widget ------------------
    if st.session_state.perspective_trigger is not None:
        st.session_state.Perspective = st.session_state.perspective_trigger
        st.session_state.perspective_trigger = None  # reset trigger
        st.rerun()

    #Default value of "for checking my diabetes"
    if "Age1" not in st.session_state:
        st.session_state.Age1 = 20
    if "Gender_MF" not in st.session_state:
        st.session_state.Gender_MF = "Male"
    if "Bmi1" not in st.session_state:
        st.session_state.Bmi1 = 10.00
    if "Blood_Pressure1" not in st.session_state:
        st.session_state.Blood_Pressure1 = 40.00
    if "Glucose1" not in st.session_state:
        st.session_state.Glucose1 = 47.00
    if "Insulin1" not in st.session_state:
        st.session_state.Insulin1 = 0.00
    if "Skin_Thickness1" not in st.session_state:
        st.session_state.Skin_Thickness1 = 0.00
    if "Family_YN" not in st.session_state:
        st.session_state.Family_YN = "No"
    if "Exercise_New" not in st.session_state:
        st.session_state.Exercise_New = "Yes"
    if "Smoking_New" not in st.session_state:
        st.session_state.Smoking_New = "No"
    if "Alcohol_New" not in st.session_state:
        st.session_state.Alcohol_New = "No"
    if "Exercise_Occasionally1" not in st.session_state:
        st.session_state.Exercise_Occasionally1 = 0
    if "Exercise_Sometimes1" not in st.session_state:
        st.session_state.Exercise_Sometimes1 = 0
    if "Exercise1" not in st.session_state:
        st.session_state.Exercise1 = 0
    if "Smoking_Occasionally1" not in st.session_state:
        st.session_state.Smoking_Occasionally1 = 0
    if "Smoking1" not in st.session_state:
        st.session_state.Smoking1 = 0
    if "Alcohol_Occasionally1" not in st.session_state:
        st.session_state.Alcohol_Occasionally1 = 0
    if "Alcohol1" not in st.session_state:
        st.session_state.Alcohol1 = 0


    if st.session_state.patient_reset_triggered1:
        st.session_state.Age1 = 20
        st.session_state.Gender_MF = "Male"
        st.session_state.Bmi1 = 10.00
        st.session_state.Blood_Pressure1 = 40.00
        st.session_state.Glucose1 = 47.00
        st.session_state.Insulin1 = 0.00
        st.session_state.Skin_Thickness1 = 0.00
        st.session_state.Family_YN = "No"
        st.session_state.Exercise_New = "Yes"
        st.session_state.Smoking_New = "No"
        st.session_state.Alcohol_New = "No"
        st.session_state.perspective_trigger = "For Checking My Diabetes"

        st.session_state.patient_reset_triggered1 = False
        st.rerun()

    # Default value of "for checking Friends, Relatives or Others Diabetes"
    if "Patient_Name2" not in st.session_state:
        st.session_state.Patient_Name2 = ''
    if "Age2" not in st.session_state:
        st.session_state.Age2 = 20
    if "Gender2" not in st.session_state:
        st.session_state.Gender2 = 'Male'
    if "Bmi2" not in st.session_state:
        st.session_state.Bmi2 = 10.00
    if "Blood_Pressure2" not in st.session_state:
        st.session_state.Blood_Pressure2 = 40.00
    if "Glucose2" not in st.session_state:
        st.session_state.Glucose2 = 47.00
    if "Insulin2" not in st.session_state:
        st.session_state.Insulin2 = 0.00
    if "Skin_Thickness2" not in st.session_state:
        st.session_state.Skin_Thickness2 = 0.00
    if "Family_History2" not in st.session_state:
        st.session_state.Family_History2 = 0
    if "Exercise_Occasionally2" not in st.session_state:
        st.session_state.Exercise_Occasionally2 = 0
    if "Exercise_Sometimes2" not in st.session_state:
        st.session_state.Exercise_Sometimes2 = 0
    if "Exercise2" not in st.session_state:
        st.session_state.Exercise2 = 0
    if "Smoking_Occasionally2" not in st.session_state:
        st.session_state.Smoking_Occasionally2 = 0
    if "Smoking2" not in st.session_state:
        st.session_state.Smoking2 = 0
    if "Alcohol_Occasionally2" not in st.session_state:
        st.session_state.Alcohol_Occasionally2 = 0
    if "Alcohol2" not in st.session_state:
        st.session_state.Alcohol2 = 0
    if "Family_Hist" not in st.session_state:
        st.session_state.Family_Hist = "No"
    if "Smoking" not in st.session_state:
        st.session_state.Smoking = "No"
    if "Alcohol" not in st.session_state:
        st.session_state.Alcohol = "No"
    if "Exercise" not in st.session_state:
        st.session_state.Exercise = "Yes"
    if "dynamic_table_reset" not in st.session_state:
        st.session_state.dynamic_table_reset = False

    if st.session_state.dynamic_table_reset:
        st.session_state.final_table.drop(st.session_state.final_table.index, inplace=True)
        st.session_state.edited_table.drop(st.session_state.edited_table.index, inplace=True)
        st.session_state.table_switch = False
        st.session_state.text = "💾Patients Data"
        st.session_state.disable_column = False

    if st.session_state.patient_reset_triggered2:
        st.session_state.Patient_Name2 = ''
        st.session_state.Age2 = 20
        st.session_state.Gender2 = 'Male'
        st.session_state.Bmi2 = 10.00
        st.session_state.Blood_Pressure2 = 40.00
        st.session_state.Glucose2 = 47.00
        st.session_state.Insulin2 = 0.00
        st.session_state.Skin_Thickness2 = 0.00
        st.session_state.Family_History2 = 0
        st.session_state.Exercise_Occasionally2 = 0
        st.session_state.Exercise_Sometimes2 = 0
        st.session_state.Exercise2 = 0
        st.session_state.Smoking_Occasionally2 = 0
        st.session_state.Smoking2 = 0
        st.session_state.Alcohol_Occasionally2 = 0
        st.session_state.Alcohol2 = 0
        st.session_state.Family_Hist = "No"
        st.session_state.Smoking = "No"
        st.session_state.Alcohol = "No"
        st.session_state.Exercise = "Yes"
        st.session_state.Gender_text = "Male"

        st.session_state.patient_reset_triggered2 = False
        st.rerun()


    if st.session_state.reset_triggered:
        st.session_state.identity = 'Who Are You❓'
        st.session_state.title = ''
        st.session_state.first_name = ''
        st.session_state.middle_name = ''
        st.session_state.last_name = ''
        st.session_state.identity_expander = True
        st.session_state.reset_triggered = False
        st.rerun()

    st.session_state.dynamic_table_reset = True

    st.subheader(st.session_state.identity)

    with st.expander("📝 View/Edit Your Details", expanded = st.session_state.identity_expander):
        st.write("Please Enter Your Details Below Carefully :")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.session_state.title = st.session_state.title
            st.text_input("Title", key = "title", placeholder="Mr.", disabled = st.session_state.name_disabled)
        with col2:
            st.session_state.first_name = st.session_state.first_name
            st.text_input("First Name", key = "first_name", placeholder = "Pranay", disabled = st.session_state.name_disabled)
        with col3:
            st.session_state.middle_name = st.session_state.middle_name
            st.text_input("Middle Name", key = "middle_name", placeholder = "Rohidas", disabled = st.session_state.name_disabled)
        with col4:
            st.session_state.last_name = st.session_state.last_name
            st.text_input("Last Name", key = "last_name", placeholder = "Sonawane", disabled = st.session_state.name_disabled)

        col5, col6 = st.columns(2)
        with col5:
            submitted = st.button('Submit', help="Please Click Here For Your Identity", width=500, icon = "📤", disabled = st.session_state.name_disabled)
        with col6:
            reset = st.button('Reset', help="Please Click Here For Clear Form", width=500, icon = "🔄")

        title_input = st.session_state.title.isdigit()
        first_input = st.session_state.first_name.isdigit()
        middle_input = st.session_state.middle_name.isdigit()
        last_input = st.session_state.last_name.isdigit()

        if submitted:
            if title_input and first_input and middle_input and last_input:
                st.error("🛑Please enter your details correctly")
            else:
                if title_input:
                    st.error("🛑Please type a **text** in Title instead of number")
                if first_input:
                    st.error("🛑Please type a **text** in First Name instead of number")
                if middle_input:
                    st.error("🛑Please type a **text** in Middle Name instead of number")
                if last_input:
                    st.error("🛑Please type a **text** in Last Name instead of number")
                elif (title_input == False) and (first_input == False) and (middle_input == False) and (last_input == False):
                    full_name = f"🙏 {st.session_state.title.strip()} {st.session_state.first_name.strip()} {st.session_state.middle_name.strip()} {st.session_state.last_name.strip()} "
                    if (st.session_state.title and st.session_state.first_name and st.session_state.middle_name and st.session_state.last_name) or (st.session_state.title and st.session_state.first_name and st.session_state.last_name) or (st.session_state.title and st.session_state.first_name):
                        st.session_state.identity = full_name
                        st.session_state.identity_expander = False
                        st.session_state.name_disabled = True
                        msg = st.empty()
                        msg.success("👍 Details submitted successfully!")
                        time.sleep(2)
                        msg.empty()
                        st.rerun()
                    else:
                        st.error("🛑Please enter your details correctly")
                else:
                    pass


        @st.dialog("Are You Sure :")
        def dialog():
            st.markdown("⚠️You Loss Your All Data After Clicking **Yes**")
            col7, col8 = st.columns(2)
            with col7:
                yes = st.button("Yes", icon='✔️', width=200)
                if yes:
                    st.session_state.reset_triggered = True
                    st.session_state.name_disabled = False
                    st.rerun()
            with col8:
                no = st.button("No", icon='❌', width=200)
                if no:
                    st.session_state.reset_triggered = False
                    st.session_state.name_disabled = True
                    st.rerun()

        if reset:
            if st.session_state.Perspective is not None :
                dialog()
            elif st.session_state.Perspective is None:
                st.session_state.reset_triggered = True
                st.session_state.name_disabled = False
                st.rerun()
        else:
            pass

    st.subheader("🧐Please Put Patient Details Below Carefully : ")
    Perspective = st.selectbox("🤔What's Your Perspective?",
                 ["For Checking My Diabetes", "For Checking Friends,Relatives Or Others Diabetes"],
                 key="Perspective")
    st.session_state.dynamic_table_reset = True

    if Perspective == "For Checking My Diabetes":
        col9, = st.columns(1)
        with col9:
            st.number_input("👦|👴🏻What's Your Age ?", min_value=20, max_value=119, key="Age1")

        col10, col11, col12, col13 = st.columns(4)

        with col10:
            st.write("")
            Gender_MF = st.selectbox("♂️|♀️Select Gender :", ["Male", "Female"], key="Gender_MF")
            if Gender_MF == "Female":
                st.session_state.Gender1 = 0
            elif Gender_MF == "Male":
                st.session_state.Gender1 = 1
            else:
                pass

        with col11:
            st.write("")
            st.number_input("⚖️Bmi(Body Mass Index) :", min_value=10.00, max_value=60.00, key="Bmi1")
        with col12:
            st.write("")
            st.number_input("💉Blood Pressure :", min_value=40.00, max_value=200.00, key="Blood_Pressure1")

        with col13:
            st.write("")
            st.number_input("🧪Glucose :", min_value=47.00, max_value=193.00, key="Glucose1")

        col14, col15, col16, col17 = st.columns(4)
        with col14:
            st.number_input("🧬Insulin :", min_value=0.00, max_value=300.00, key="Insulin1")
        with col15:
            st.number_input("📏Skin Thickness :", min_value=0.00, max_value=80.00, key="Skin_Thickness1")
        with col16:
            Family_YN = st.selectbox("👨‍👩‍👧Family History :", ["No", "Yes"], key="Family_YN")

            # Converted value
            if Family_YN == "Yes":
                st.session_state.Family_History1 = 1
            else:
                st.session_state.Family_History1 = 0

        with col17:
            Exercise_New = st.selectbox(
                "🏃Exercise :",
                ["Yes", "No", "Sometimes", "Occasionally"],
                key="Exercise_New"
            )

            if Exercise_New == "No":
                st.session_state.Exercise1 = 0
                st.session_state.Exercise_Sometimes1 = 0
                st.session_state.Exercise_Occasionally1 = 0
            elif Exercise_New == "Yes":
                st.session_state.Exercise1 = 1
                st.session_state.Exercise_Sometimes1 = 0
                st.session_state.Exercise_Occasionally1 = 0
            elif Exercise_New == "Occasionally":
                st.session_state.Exercise1 = 0
                st.session_state.Exercise_Sometimes1 = 0
                st.session_state.Exercise_Occasionally1 = 1
            elif Exercise_New == "Sometimes":
                st.session_state.Exercise1 = 0
                st.session_state.Exercise_Sometimes1 = 1
                st.session_state.Exercise_Occasionally1 = 0
            else:
                pass

        col18, col19 = st.columns(2)
        with col18:
            Smoking_New = st.selectbox(
                "🚬Smoking :",
                ["No", "Yes", "Occasionally"],
                key="Smoking_New"
            )

            if Smoking_New == "No":
                st.session_state.Smoking1 = 0
                st.session_state.Smoking_Occasionally1 = 0
            elif Smoking_New == "Yes":
                st.session_state.Smoking1 = 1
                st.session_state.Smoking_Occasionally1 = 0
            elif Smoking_New == "Occasionally":
                st.session_state.Smoking1 = 0
                st.session_state.Smoking_Occasionally1 = 1
            else:
                pass

        with col19:
            Alcohol_New = st.selectbox(
                "🍺Alcohol :",
                ["No", "Yes", "Occasionally"],
                key="Alcohol_New"
            )

            st.session_state.Alcohol1 = 1 if Alcohol_New == "Yes" else 0
            st.session_state.Alcohol_Occasionally1 = 1 if Alcohol_New == "Occasionally" else 0

        col20, col21 = st.columns(2)
        with col20:
            Pridict = st.button("Result", help="Please Click Here to see result", width=500, icon = "📊")
        with col21:
            Reset_to_default = st.button("Clear", help="Please Click Here to reset your numbers into default face",
                                         width=500, key = "reset_button_1", icon = '🗑️')


        # Define dialogs
        @st.dialog("⚠️ Diabetes Risk Detected")
        def show_positive_dialog(identity):
            st.write(f"👋 {identity}, you have chances of diabetes.")
            st.write("💡 Please consult a medical expert for diagnosis.")
            space, col22, space = st.columns(3)
            with col22:
                if st.button("OK", icon='✔️', width=200):
                    st.rerun()


        @st.dialog("💪 You’re Healthy!")
        def show_negative_dialog(identity):
            st.write(f"🎉 {identity}, you seem healthy.")
            st.write("Keep maintaining your healthy habits! 💪")
            space, col23, space = st.columns(3)
            with col23:
                if st.button("OK", icon = '✔️', width = 200):
                    st.rerun()

        Data = {
            "Age" :st.session_state.Age1,
            "Gender" : st.session_state.Gender1,
            "BMI" : st.session_state.Bmi1,
            "BloodPressure" : st.session_state.Blood_Pressure1,
            "Glucose" : st.session_state.Glucose1,
            "Insulin" : st.session_state.Insulin1,
            "SkinThickness" : st.session_state.Skin_Thickness1,
            "FamilyHistory" : st.session_state.Family_History1,
            "Exercise_Occasionally" : st.session_state.Exercise_Occasionally1,
            "Exercise_Sometimes" : st.session_state.Exercise_Sometimes1,
            "Exercise_Yes" : st.session_state.Exercise1,
            "Smoking_Occasionally" : st.session_state.Smoking_Occasionally1,
            "Smoking_Yes" : st.session_state.Smoking1,
            "Alcohol_Occasionally" : st.session_state.Alcohol_Occasionally1,
            "Alcohol_Yes" : st.session_state.Alcohol1
        }

        if Pridict:
            if st.session_state.identity != 'Who Are You❓':
                Patient_data = pd.DataFrame([Data])
                scaled_input = scaler.transform(Patient_data)
                prediction = model.predict(scaled_input)[0]

                if prediction == 1:
                    show_positive_dialog(f"{st.session_state.title} {st.session_state.first_name} {st.session_state.middle_name} {st.session_state.last_name}")
                else:
                    show_negative_dialog(f"{st.session_state.title} {st.session_state.first_name} {st.session_state.middle_name} {st.session_state.last_name}")
            else:
                st.error("🛑Please First Fill User Details Instead Of Patient Details")
        else:
            pass

        if Reset_to_default:
            st.session_state.patient_reset_triggered1 = True
            st.rerun()
        else:
            pass

        st.markdown("""
                <div style='text-align: center; margin-top: 25px; font-size: 18px; color: #d4d4d4; font-style: italic;'>
                    “Early to bed and early to rise makes a man healthy, wealthy, and wise.”<br>
                    — <b>Benjamin Franklin</b>
                </div>
                """, unsafe_allow_html=True)

    elif Perspective == "For Checking Friends,Relatives Or Others Diabetes":
        col24, col25 = st.columns(2)
        with col24:
            st.text_input("🛏️Enter Your Patient Name :", placeholder="Mr. Pranay R. Sonawane" , key="Patient_Name2")
        with col25:
            st.number_input("👦|👴🏻What's Your age ?", min_value=20, max_value=119, key="Age2")

        col26, col27, col28, col29 = st.columns(4)

        with col26:
            st.write("")
            Gender_text = st.selectbox("♂️|♀️Select Gender :", ["Male", "Female"], key = 'Gender_text')
            if Gender_text == "Female":
                st.session_state.Gender2 = 0
            elif Gender_text == "Male":
                st.session_state.Gender2 = 1
            else:
                pass

        with col27:
            st.write("")
            st.number_input("⚖️Bmi(Body Mass Index) :", min_value=10.00, max_value=60.00, key="Bmi2")
        with col28:
            st.write("")
            st.number_input("💉Blood Pressure :", min_value=40.00, max_value=200.00,
                                            key="Blood_Pressure2")

        with col29:
            st.write("")
            st.number_input("🧪Glucose :", min_value=47.00, max_value=193.00, key="Glucose2")

        col30, col31, col32, col33 = st.columns(4)
        with col30:
            st.number_input("🧬Insulin :", min_value=0.00, max_value=300.00, key="Insulin2")
        with col31:
            st.number_input("📏Skin Thickness :", min_value=0.00, max_value=80.00, key="Skin_Thickness2")
        # --- FAMILY HISTORY ---
        with col32:
            Family_Hist = st.selectbox("👨‍👩‍👧Family History :", ["No", "Yes"], key="Family_Hist")

        # Converted value
        if Family_Hist == "Yes":
            st.session_state.Family_History2 = 1
        else:
            st.session_state.Family_History2 = 0

        # --- EXERCISE ---
        with col33:
            Exercise = st.selectbox(
                "🏃Exercise :",
                ["Yes", "No", "Sometimes", "Occasionally"],
                key="Exercise"
            )

        if Exercise == "No":
            st.session_state.Exercise2 = 0
            st.session_state.Exercise_Sometimes2 = 0
            st.session_state.Exercise_Occasionally2 = 0
        elif Exercise == "Yes":
            st.session_state.Exercise2 = 1
            st.session_state.Exercise_Sometimes2 = 0
            st.session_state.Exercise_Occasionally2 = 0
        elif Exercise == "Occasionally":
            st.session_state.Exercise2 = 0
            st.session_state.Exercise_Sometimes2 = 0
            st.session_state.Exercise_Occasionally2 = 1
        elif Exercise == "Sometimes":
            st.session_state.Exercise2 = 0
            st.session_state.Exercise_Sometimes2 = 1
            st.session_state.Exercise_Occasionally2 = 0
        else:
            pass

        # --- SMOKING ---
        col34, col35 = st.columns(2)
        with col34:
            Smoking = st.selectbox(
                "🚬Smoking :",
                ["No", "Yes", "Occasionally"],
                key="Smoking"
            )

        if Smoking == "No":
            st.session_state.Smoking2 = 0
            st.session_state.Smoking_Occasionally2 = 0
        elif Smoking == "Yes":
            st.session_state.Smoking2 = 1
            st.session_state.Smoking_Occasionally2 = 0
        elif Smoking == "Occasionally":
            st.session_state.Smoking2 = 0
            st.session_state.Smoking_Occasionally2 = 1
        else:
            pass

        # --- ALCOHOL ---
        with col35:
            Alcohol = st.selectbox(
                "🍺Alcohol :",
                ["No", "Yes", "Occasionally"],
                key="Alcohol"
            )

        Alcohol2 = 1 if Alcohol == "Yes" else 0
        Alcohol_Occasionally2 = 1 if Alcohol == "Occasionally" else 0

        # --- Create new data row ---
        Data2 = pd.DataFrame([{
            "Patient_name": st.session_state.Patient_Name2,
            "Age": st.session_state.Age2,
            "Gender": st.session_state.Gender2,
            "BMI": st.session_state.Bmi2,
            "BloodPressure": st.session_state.Blood_Pressure2,
            "Glucose": st.session_state.Glucose2,
            "Insulin": st.session_state.Insulin2,
            "SkinThickness": st.session_state.Skin_Thickness2,
            "FamilyHistory": st.session_state.Family_History2,
            "Exercise_Occasionally": st.session_state.Exercise_Occasionally2,
            "Exercise_Sometimes": st.session_state.Exercise_Sometimes2,
            "Exercise_Yes": st.session_state.Exercise2,
            "Smoking_Occasionally": st.session_state.Smoking_Occasionally2,
            "Smoking_Yes": st.session_state.Smoking2,
            "Alcohol_Occasionally": st.session_state.Alcohol_Occasionally2,
            "Alcohol_Yes": st.session_state.Alcohol2
        }])

        table = st.session_state.edited_table

        col36, col37, col38 = st.columns(3)
        with col36:
            st.space()
            Add_Into_Table = st.button(
                "Add To Table",
                help="Click here for adding above blocks of data into below table",
                use_container_width=True,
                disabled = st.session_state.disable_column,
                icon = "➕",
                width = 500
            )


        def delete_rows():

            def execute():
                row = st.session_state.delete_row_input  # read from session_state
                if row in table.index:
                    table.drop(index=row, inplace=True)
                    table.reset_index(drop=True, inplace=True)
                    table.index = range(1, len(table) + 1)
                    if len(table) > 0:
                        table.index.name = 'Sr.No.'
                    else:
                        table.drop(table.index, inplace=True)

            row_main = st.number_input(
                '❌Delete By Rows :',
                key="delete_row_input",
                width=250,
                min_value=0,
                max_value=len(table),
                on_change=execute,
                disabled=st.session_state.disable_column
            )


        with col37:
            delete_rows()

        with col38:
            st.space()
            Delete = st.button(
                "Delete Table",
                help="Click here for deleting all data from below table",
                use_container_width=True,
                icon = '🗑️',
                width = 500
            )

        # ---------------------- ADD INTO TABLE ----------------------
        if Add_Into_Table:
            if (st.session_state.identity == "Who Are You❓") and (st.session_state.Patient_Name2 != ""):
                st.error("🛑Please Introduce **yourself** first")

            elif (st.session_state.Patient_Name2 == "") and (st.session_state.identity != "Who Are You❓"):
                st.error("🛑Please Add A Patient Name")

            elif (st.session_state.identity != "Who Are You❓") and (st.session_state.Patient_Name2.isdigit()):
                st.error("🛑Please Put a text in patient name")
            elif (st.session_state.identity == "Who Are You❓") and (st.session_state.Patient_Name2 == ""):
                st.error("🛑Please Introduce Yourself First Then Add A Patient Name")

            else:
                table = pd.concat([table, Data2], ignore_index=True)
                table.index = range(1, len(table) + 1)
                table.index.name = "Sr.No."
                st.session_state.edited_table = table
                st.session_state.patient_reset_triggered2 = True
                st.session_state.perspective_trigger = "For Checking Friends,Relatives Or Others Diabetes"
                st.session_state.dynamic_table_reset = False
                st.session_state.text = "💾Patients Data"
                msg = st.empty()
                msg.success("👍 Patient Added Successfully")
                while time.sleep(1):
                    st.session_state.patient_disabled = True
                else:
                    st.session_state.patient_disabled = False
                msg.empty()
                st.rerun()
        # ---------------------- Delete Rows ----------------------

        if Delete:

            if len(table) == 0:
                st.error("🛑The table is empty 😕")
            else:
                table.drop(table.index, inplace=True)
                table.index = range(1, len(table) + 1)
                st.session_state.disable_column = False
                st.session_state.table_switch = False
                st.session_state.text_triggered = False
                st.session_state.dynamic_table_reset = False
                msg = st.empty()
                msg.error('🧹 All Data Are Deleted Successfully')
                time.sleep(2)
                msg.empty()
                st.rerun()

            st.session_state.perspective_trigger = "For Checking Friends,Relatives Or Others Diabetes"

        # SHOW TABLE WITH SR.NO. STARTING FROM 1
        col38, = st.columns(1)
        with col38:
            st.subheader(st.session_state.text)

        def highlight_rows(row):
            if row["Outcome"] == 1:
                return ["background-color: red; color: white; font-weight: bold;"] * len(row)
            else:
                return [""] * len(row)


        table_container = st.container()
        with table_container:
            if not st.session_state.table_switch:
                # show user’s added data (editable)
                st.dataframe(st.session_state.edited_table, use_container_width = True)
            else:
                user_name = f"{st.session_state.first_name + ' ' + st.session_state.middle_name + ' ' + st.session_state.last_name}"
                total_positive = (st.session_state.final_table['Outcome'] == 1).sum()
                total_negative = (st.session_state.final_table['Outcome'] == 0).sum()
                with st.form("Patient Reports"):
                    st.text(f"User Name : {user_name}")
                    col41, col42 = st.columns(2, width = 350)
                    with col41:
                        st.markdown(f'''
                        Total :red[Positive Cases] : {total_positive}
                        ''')
                    with col42:
                        st.markdown(f'''
                        Total :green[Negative Cases] : {total_negative}
                        ''')

                    styled_table = (
                        st.session_state.final_table
                        .style
                        .apply(highlight_rows, axis=1)
                        .format({
                            "BMI": "{:.2f}",
                            "BloodPressure": "{:.2f}",
                            "Glucose": "{:.2f}",
                            "Insulin": "{:.2f}",
                            "SkinThickness": "{:.2f}",
                        })
                    )


                    st.dataframe(styled_table, use_container_width=True)

                    csv_data = st.session_state.final_table.to_csv(index=False)

                    custom_csv = (
                        f"User Name :-,{user_name}\n"
                        f"Total Positive Cases :-,{total_positive}\n"
                        f"Total Negative Cases :-,{total_negative}\n\n"
                        f"\t,Note : If Patient Have 0 Outcome Then Patient Don't have The Diabetes And If Patient Have 1 Outcome Then The Patient Have Diabetes\n\n"
                        f"{csv_data}"
                    )

                    Download = st.form_submit_button("Download Your Report", icon = '⬇️')

                if Download:
                    with st.spinner('Prepare For Downloading...', width = 500):
                        time.sleep(5)
                    st.download_button(
                        label="📥 Download Report",
                        data = custom_csv,
                        file_name="patient_report.csv",
                        mime="text/csv"
                    )


        @st.dialog ("⚠️Caution")
        def caution():
            st.write("🧐Check All Added Details Before Checking The Reports")
            space, col43, space = st.columns(3)
            with col43:
                confirm = st.button("Confirm", use_container_width = True, icon = '✔️')
                if confirm:
                    input_data = st.session_state.edited_table.copy()
                    input_data = input_data.loc[:, "Age":"Alcohol_Yes"]
                    scaled_step = scaler.transform(input_data)
                    prediction_step = model.predict(scaled_step)
                    input_data["Outcome"] = prediction_step
                    input_data["Patient_name"] = st.session_state.edited_table["Patient_name"].values

                    input_data = input_data[[
                        "Patient_name", "Age", "Gender", "BMI", "BloodPressure", "Glucose",
                        "Insulin", "SkinThickness", "FamilyHistory",
                        "Exercise_Occasionally", "Exercise_Sometimes", "Exercise_Yes",
                        "Smoking_Occasionally", "Smoking_Yes", "Alcohol_Occasionally", "Alcohol_Yes", "Outcome"
                    ]]

                    st.session_state.final_table = input_data
                    st.session_state.text_triggered = True
                    st.session_state.disable_column = True
                    st.session_state.table_switch = True
                    st.session_state.dynamic_table_reset = False
                    st.rerun()

        st.session_state.dynamic_table_reset = False
        Final_Reports = st.button("Final Report", disabled = st.session_state.disable_column, icon = '📄')
        if (len(st.session_state.edited_table) == 0 ) and Final_Reports:
            st.error("🛑The Table Is Empty")
        elif Final_Reports:
            caution()
        else:
            pass

        st.markdown("""
                <div style='text-align: center; margin-top: 25px; font-size: 18px; color: #d4d4d4; font-style: italic;'>
                    “Early to bed and early to rise makes a man healthy, wealthy, and wise.”<br>
                    — <b>Benjamin Franklin</b>
                </div>
                """, unsafe_allow_html=True)

# Contact Page
elif selected == 'Contact':
    st.session_state.name_disabled = False
    st.session_state.reset_triggered = True
    st.title("📞 Contact Information")
    st.write("### Get in Touch with Me")

    st.markdown("""
        Thank you for exploring the **Diabetes Predictor App**!  
        I'm always open to feedback, collaboration, or discussions about data science, machine learning, and analytics projects.  

        If you have any questions, suggestions, or just want to say hi — feel free to reach out through the details below.
        """)

    st.markdown("---")

    st.markdown("### 🧑‍💻 Developer Information")
    st.write("""
        **Name:** Pranay Rohidas Sonawane  
        **Role:** Data Analyst & Machine Learning Enthusiast  
        **Year Created:** 2025  
        """)

    st.markdown("---")

    st.markdown("### 🌐 Connect with Me")
    st.write("""
        📧 **Email:** [pranay.sonawane99@gmail.com](mailto:pranay.sonawane99@gmail.com)  
        💼 **LinkedIn:** [https://www.linkedin.com/in/sonawane-pranay/](https://www.linkedin.com/in/sonawane-pranay/)  
        🧠 **GitHub:** [github.com/pranay-sonawane](https://github.com/Pranay-R-Sonawane)  
        """)

    st.markdown("---")
    st.info("💡 *Feel free to connect for collaborations, ideas, or feedback related to this project!*")

    st.markdown(
        """
        <div style='text-align: center; color: grey; font-size: 14px;'>
            © 2025 Diabetes Predictor | Developed by <b>Pranay Rohidas Sonawane</b>
        </div>
        """,
        unsafe_allow_html=True
    )

