import streamlit as st
import importlib

def show_page(page_name):
    modules ={
        "Início": "inicio",
        "Projetos": "projetos",
        "Dashboards": "dashboards",
        "Contatos": "contato"   
    }

    module_name = modules.get(page_name)
    if module_name:
        module = importlib.import_module(module_name)
        
        if hasattr(module, "run"):
            module.run()
        else: 
            st.write("O módulo não tem uma função 'run' para exibir o conteúdo.")
    else:
        st.write("Página não encontrada.")
        

#### Selectbox

page = st.sidebar.selectbox(
    "Navegação",
    ['Início', 'Projetos', 'Dashboards','Contatos'] 
)
    
        

#### Streamlit

if page == "Início":

    st.title("Portifólio de Análise de Dados")




    st.write("""
        👋 Olá, me chamo Antonny Fernando, graduando em Análise e Desenvolvimento de Sistemas e apaixonado pelo universo da tecnologia! 
        
        Trilhei um caminho profissional até aqui, direcionado para análise e organização de dados, sempre buscando eficiência e resolução de problemas.    
            
        Se você procura alguém comprometido, analítico e fascinado por dados e tecnologia, entre em contato comigo! Será um prazer conhecê-lo(a).  
    """)
else:
    show_page(page)