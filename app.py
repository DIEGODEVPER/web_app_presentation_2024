import streamlit as st
import re
from streamlit_lottie import st_lottie
import requests

#Variables
email = "diegofiis10@gmail.com"
path_css = "styles/style.css"
lottie_url = "https://lottie.host/bea690db-d27b-405f-9120-075358e5fc74/V7PGdaRwLW.json"
lottie_contact_url = "https://lottie.host/9b81543c-add6-4c0f-86da-5e5b1328237b/Oh4udOR9Nk.json"

#configuracion web app
st.set_page_config(page_title="DGSRAPP", page_icon="🤖", layout= "wide")


#Funciones 

#Esta funcion esta en regex, la extraje de ChatGTP
def validate_email(email):
    # Define the regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use re.match to check if the provided email matches the pattern
    match = re.match(pattern, email)

    # If there is a match, the email is valid; otherwise, it's not
    return bool(match)

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load(path_css)

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Definir el frontend
#seccion introduccion

with st.container():
    st.header("Hola, bienvenido a nuestra web 👋")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write("""
             Somos unos apasionados de la tecnología y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos.
             """)
    st.write("[Saber más](https://valerapp.com/)")


#seccion sobre nosotros

with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)

    with text_column:
        st.header("Sobre nosotros 🔍")
        st.write("""
                 Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:

            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
                 
                 """)
        st.write("[Más sobre nosotros>](https://valerapp.com/about/)")

    with animation_column:
        lottie = load_lottie(lottie_url)
        st_lottie(lottie, height=500)

#Seccion servicios
with st.container():
    st.write("---")
    st.header("Servicios 💻")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("assets/apps.png")
    with text_column:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.    
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")
    
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("assets/automation.png")
    with text_column:
        st.subheader("Automatización de procesos")
        st.write(
            """
            Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras tareas más productivas.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("assets/visualizacion.png")
    with text_column:
        st.subheader("Visualización de datos")
        st.write(
            """
            Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una aplicación en la que puedas tener toda la información de interes de tu empresa.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    st.header("Contacta con nosotros 📩")
    st.write("##")
    formulario, vacio = st.columns(2)
    contact_form = f"""
    <form action="https://formsubmit.co/{email}" method="POST">
    <input type="hidden" name="_captcha" value="false"> 
     <label for="fname">Tu Nombre </label>
     <input type="text" name="name" placeholder ="Tu nombre" required>
     <label for="fname">Tu email </label>
     <input type="email" name="email" placeholder ="Tu email" required>
     <label for="fname">Tu mensaje </label>
     <textarea type="message" name="message" placeholder ="Tu mensaje aquí" required></textarea>
     <button type="submit">Enviar</button>
    </form>
    """
    with formulario:
        st.markdown(contact_form,unsafe_allow_html=True)
    with vacio:
        lottie_contact = load_lottie(lottie_contact_url)
        st_lottie(lottie_contact, height=300)
