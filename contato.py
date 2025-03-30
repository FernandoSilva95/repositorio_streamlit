import streamlit as st

def run():
    st.subheader("Contatos")
    st.write("Para nossa comunicação, você pode enviar um e-mail para: [antonnyfernando@gmail.com](mailto:antonnyfernando@gmail.com)")
    st.write("Me encontre nas redes sociais:")
    
    # LinkedIn
    linkedin_url = "https://www.linkedin.com/in/fernandosilva29"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><ing src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24"/> LinkedIn: @fernandosilva29</a>', unsafe_allow_html=True)
    
     # LinkedIn
    github_url = "https://github.com/FernandoSilva95"
    st.markdown(f'<a href="{github_url}" target="_blank"><ing src="https://cdn-icons-png.flaticon.com/512/733/733609.png" width="24"/> GitHub: @FernandoSilva95</a>', unsafe_allow_html=True)
    
    