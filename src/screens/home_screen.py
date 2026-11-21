# # # import streamlit as st 
# # # from src.components.header import header_home 


# # # def home_screen():
# # #     st.header("Home screen")
# # #     col1,col2=st.columns(2)

# # #     with col1:
# # #        if st.button('Teacher portal'):
# # #             st.session_state['login_type']='teacher'
# # #             st.rerun()
            
# # #     with col2:
# # #         if st.button('student portal'):
# # #             st.session_state['login_type']='student'
# # #             st.rerun()
        
# # import streamlit as st
# # from src.components.header import header_home

# # def home_screen():
# #     st.header('Home Screen')


# # header_home()
# # col1, col2 = st.columns(2)

# # with col1:
# #     if st.button('Teacher Portal'):
# #         st.session_state['login_type']='teacher'
# #         st.rerun()
# # with col2:
# #     if st.button('Student Portal'):
# #         st.session_state['login_type']='student'
# #         st.rerun()
# import streamlit as st
# from src.components.header import header_home

# def home_screen():
#     header_home()
#     style_base_layout()
#     st.header('Home Screen')
    
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button('Teacher Portal'):
#             st.session_state['login_type'] = 'teacher'
#             st.rerun()
            
#     with col2:
#         if st.button('Student Portal'):
#             st.session_state['login_type'] = 'student'
#             st.rerun()
import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():


    header_home()
    style_background_home( )

    style_base_layout()


    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.header("i am teacher")
        st.image("/Users/rohitkumar/Desktop/Aiproject/image_4d73211d.jpg",width=200)
        if st.button('Teacher Portal'):
            st.session_state['login_type']='teacher'
            st.rerun()
    with col2:
        st.header("i am student")
        st.image("/Users/rohitkumar/Desktop/Aiproject/image_5e713535.jpg",width=200)
        if st.button('Student Portal'):
            st.session_state['login_type']='student'
            st.rerun()
