import streamlit as st
st.header("HEY")

contact_form= '''
<form action="https://formsubmit.co/shrawil.sarve.it@ghrce.raisoni.net" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Enter yout Email" required>
     <textarea name="message" placeholder="Enter yout message here"></textarea>
     <button type="submit">Send</button>
</form>
'''

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

