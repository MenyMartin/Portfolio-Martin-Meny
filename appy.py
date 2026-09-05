import streamlit as st
import streamlit_shadcn_ui as ui

from pathlib import Path

css_file = Path(__file__).parent / "styles" / "styles.css"

with open(css_file, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)   

resume_file = "assets/CV_MARTIN_MENY_(IT_2026).pdf"
resume_file_name = "CV_Martin_Meny.pdf"
profile_pic = "assets/Foto_CV.jpg"

layout = "centered"
page_title = "Portfolio | Martin Meny" 
page_icon = ""
name = "Martin Meny"
description = """
Desarrollador Full Stack Junior  
Técnico Universitario en Programación (UTN, 2025)

Desarrollador Junior con formación en programación y experiencia práctica en desarrollo de aplicaciones web 
y sistemas de gestión. Enfocado principalmente en C#/.NET y bases de datos, con experiencia adicional en Java y C++
"""

social_media = {
    "LinkedIn": "https://www.linkedin.com/in/martin-meny/",
    "GitHub": "https://github.com/MenyMartin",
    
}

email = "martinmeny@live.com.ar"




proyectos = [
    {
        "nombre": "eCommerce - (ASP.NET, HTML y C#) Aplicación web con niveles comprador y vendedor",
        "imagenes": [
            "assets/ecommerce1.png",
            "assets/ecommerce2.png",
            "assets/ecommerce3.png"
        ],
        "links": [
            ("📂 GitHub", "https://github.com/MenyMartin/eCommerce"),
            ("🎬 Video", "https://youtu.be/FWX5zpJE8ds")
        ]
    },
    {
        "nombre": "Home Banking - (Java) Aplicación web con niveles usuario y operario bancario. Realizado en grupo de 5 personas",
        "imagenes": [
            "assets/homebanking1.png",
            "assets/homebanking2.png",
            "assets/homebanking3.png"
        ],
        "links": [
            ("📂 GitHub", "https://github.com/MenyMartin/HomeBanking-Java/tree/main")
        ]
    },
    {
        "nombre": "Sistema ERP de cafetería (en desarrollo) - Gestión completa del negocio · App de escritorio con C# · .NET · WPF · SQL Server · EF Core",
        "imagenes": [
            "assets/desarrollo1.png",
            
        ],
        "links": [
            ("📂 GitHub", "https://github.com/MenyMartin/ERP_Cafeteria")
        ]
    }
]

otros_proyectos = [
    {
        "nombre": "Juego 2D Hale Bopp - (C++ y SFML) Proyecto académico con director de eventos, puntajes y niveles de dificultad variada",
        "imagenes": [
            "assets/hale-bopp1.png",
            "assets/hale-bopp2.png",
            "assets/hale-bopp3.png"
        ],
        "links": [
            ("📂 GitHub", "https://github.com/MenyMartin/Juego_Hale_Bopp"),
            ("🎬 Video", "https://www.youtube.com/watch?v=sg0UOpJjQ7I")
        ]
    }
]

#config pagina
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# cabecera
col1, col2 = st.columns(2)

with col1:
    st.image(profile_pic, width=250)

    

with col2:
    st.title(name)

    col_linkedin, col_github, _ = st.columns(
        [1.4, 1.4, 3],
        gap="small"
    )

    with col_linkedin:
        st.link_button(
            "💼 LinkedIn",
            social_media["LinkedIn"],
            use_container_width=True
        )

    with col_github:
        st.link_button(
            "📂 GitHub",
            social_media["GitHub"],
            use_container_width=True
        )

    st.markdown(
    f'<div class="email">📧 <a href="mailto:{email}">{email}</a></div>',
    unsafe_allow_html=True
)



    col_cv, _ = st.columns([1, 1])

    with col_cv:
        st.download_button(
            label="Descargar CV",
            data=PDFbyte,
            file_name=resume_file_name,
            use_container_width=True
        )

st.write(description)


# proyectos
st.write("---")
st.subheader('💻 Proyectos')

for project in proyectos:

    st.markdown(
                '<div class="project-divider"></div>',
                unsafe_allow_html=True
            )

    st.markdown(f"**{project['nombre']}**")
    
    link_cols = st.columns(len(project["links"]))
    
    for col, (nombre, link) in zip(link_cols, project["links"]):
            with col:
                st.markdown(f"[{nombre}]({link})")
    
    cols = st.columns(3)

    

    for col, image in zip(cols, project["imagenes"]):
        with col:
            st.image(image, use_container_width=True)

    

    "###"

    


# otros proyectos
st.write("---")
st.subheader('💻 Otros Proyectos')

for project in otros_proyectos:

    st.markdown(f"**{project['nombre']}**")

    link_cols = st.columns(len(project["links"]))

    for col, (nombre, link) in zip(link_cols, project["links"]):
        with col:
            st.markdown(f"[{nombre}]({link})")

    
    cols = st.columns(3)

    for col, image in zip(cols, project["imagenes"]):
        with col:
            st.image(image, use_container_width=True)

    
    st.markdown(
        '<div class="project-divider"></div>',
        unsafe_allow_html=True
    )

#habilidades
st.write("---")
st.subheader('🛠️ Habilidades técnicas')
st.write(
    """
⚙️ Desarrollo: C# - .NET - ASP.NET - Java - JSP - Servlets - C++ - Python

🗄️ Bases de datos: SQL Server - MySQL 

🌐 Web: HTML - CSS - JavaScript - Bootstrap

🛠️ Herramientas: Git - GitHub - Visual Studio - Eclipse - Apache Tomcat - Azure Data Studio

🧠 Conceptos: POO - Arquitectura en capas - CRUD - APIs - Autenticación - Manejo de sesiones
"""
)

#ecperiencia
st.write("---")
st.subheader('💼 Experiencia profesional')
st.markdown("""

**2026 - Actualidad - Administrativo Técnico y Postventa** • Nogalpark • Benavidez

**2024 - 2026 - Administrativo** • ASEN (Asociación Empresaria Noreste de PBA Hotelera Gastronómica) • San Isidro


**2023 - 2024 - Inspector de Control de Calidad** • Wenlen S.A. • Bella Vista


**2021 - 2023 - Coordinador de Servicio Técnico** • Kaeser Compresores • Garín


**2017 - 2021 - Producción y Oficina Técnica** • ROWA S.A. • Escobar

""")


