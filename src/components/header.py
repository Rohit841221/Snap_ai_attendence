# # # # import streamlpython3 -m streamlit run app.pyit as st
# # # # from src.components.header import header_home

# # # # def home_screen():
# # # #     st.header('Home Screen')


# # # # header_home()
# # # # col1, col2 = st.columns(2)

# # # # with col1:
# # # #     if st.button('Teacher Portal'):
# # # #         st.session_state['login_type']='teacher'
# # # #         st.rerun()
# # # # with col2:
# # # #     if st.button('Student Portal'):
# # # #         st.session_state['login_type']='student'
# # # #         st.rerun()
# import streamlit as st


# def header_home():
#        st.header('Snap Class')
# import streamlit as st
import streamlit as st
import base64

def header_home():
    with open("/Users/rohitkumar/Desktop/Aiproject/PHOTO-2026-11-11-22-31-12.jpg", "rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px;">
            <img src="data:image/jpeg;base64,{img_data}" style="height:100px; border-radius:15px;" />
            <h1 style="text-align:center; color:#E0E3FF;">SNAP<br/> CLASS</h1>
        </div>
    """, unsafe_allow_html=True)



