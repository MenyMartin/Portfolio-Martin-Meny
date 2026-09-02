import streamlit as st
import streamlit_shadcn_ui as ui

from pathlib import Path

css_file = Path(__file__).parent / "styles" / "styles.css"

with open(css_file, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)   

resume_file = "assets\CV_MARTIN _MENY_(IT_2026).pdf"
resume_file_name = "CV_Martin_Meny.pdf"
profile_pic = "assets\Foto_CV.jpg"

layout = "centered"
page_title = "Portfolio | Martin Meny" 
page_icon = ""
name = "Martin Meny"
description = """
Desarrollador Full Stack Junior  
Técnico Universitario en Programación (UTN, 2025)

Desarrollador Full Stack Junior con formación en Programación y experiencia práctica en el desarrollo de aplicaciones web. 
He desarrollado proyectos utilizando C#, ASP.NET, SQL Server, Java, JSP, Servlets, MySQL, C++ y SFML, 
aplicando Programación Orientada a Objetos, arquitectura en capas, desarrollo CRUD, autenticación, manejo de sesiones 
e integración con bases de datos. Mi experiencia profesional previa en administración, coordinación y control de calidad 
complementa mi perfil técnico con habilidades de organización, comunicación, análisis y resolución de problemas. Busco mi 
primera oportunidad profesional en IT para aportar mis conocimientos y continuar creciendo como desarrollador de 
software. 
"""

social_media = {
    "LinkedIn": "https://www.linkedin.com/in/martin-meny/",
    "GitHub": "https://github.com/MenyMartin"
}

email = "martinmeny@live.com.ar"




proyectos = [
    (
        "🎬 eCommerce - (ASP.NET, HTML y C#) Aplicación web con niveles comprador y vendedor",
        "https://youtu.be/FWX5zpJE8ds"
    ),
    (
        "📂 eCommerce - (ASP.NET, HTML y C#) Aplicación web con niveles comprador y vendedor",
        "https://github.com/MenyMartin/eCommerce"
    ),

    ("-", ""),

    (
        "📂 Home Banking - (Java) Aplicación web con niveles usuario y operario bancario. Realizado en grupo de 5 personas",
        "https://github.com/MenyMartin/HomeBanking-Java/tree/main"
    ),

    ("-", ""),

    (
        "🎬 Juego 2D Hale Bopp - (C++ y SFML) Proyecto académico con director de eventos, puntajes y niveles de dificultad variada",
        "https://www.youtube.com/watch?v=sg0UOpJjQ7I"
    ),
    (
        "📂 Juego 2D Hale Bopp - (C++ y SFML) Proyecto académico con director de eventos, puntajes y niveles de dificultad variada",
        "https://github.com/MenyMartin/Juego_Hale_Bopp"
    ),

    ("-", ""),

    (
        "📂 Sistema ERP de cafetería (en desarrollo) - Gestión completa del negocio · App de escritorio con C# · .NET · WPF · SQL Server · EF Core",
        "https://github.com/MenyMartin/ERP_Cafeteria"
    )
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


#proyectos
st.write("---")
st.subheader('💻 Proyectos')
for project, link in proyectos:
    if project == "-":
        st.markdown(
            '<div class="project-divider"></div>',
            unsafe_allow_html=True
        )
    else:
        st.write(f"[{project}]({link})")

#habilidades
st.write("---")
st.subheader('🛠️ Habilidades técnicas')
st.write(
    """
- Lenguajes: C#, Java, C++, Python, SQL, JavaScript, HTML5, CSS3
- Backend: ASP.NET, JSP, Servlets, JDBC
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Bases de datos: SQL Server, MySQL
- Ingles: Lectura avanzada - Conversación básica
- Desarrollo: Programación Orientada a Objetos, arquitectura en capas, CRUD, autenticación y autorización, manejo de sesiones, validación de datos, integración con bases de datos
Herramientas: Visual Studio, Eclipse, Apache Tomcat, Azure Data Studio, Git/GitHub
Otros: C++ / SFML
"""
)

#ecperiencia
st.write("---")
st.subheader('💼 Experiencia profesional')
st.markdown("""

**2026 - Actual — Administrativo Técnico y Postventa** • Nogalpark • Benavidez
- Administración: contabilización de FC, ND y NC; recepción de mercadería y remitos; generación de OP y seguimiento de cuentas corrientes de proveedores.
- Ventas: comercialización de máquinas y repuestos, con asesoramiento a clientes particulares y empresas.
- Postventa: recepción, control, seguimiento y entrega de máquinas ingresadas al taller de reparación.

**2024 - 2026 — Administrativo** • ASEN (Asociación Empresaria Noreste de PBA Hotelera Gastronómica) • San Isidro
- Gestión y administración de documentación institucional.
- Redacción formal de documentos institucionales (libros de actas y comunicaciones oficiales).
- Preparación de documentación y coordinación logística de viajes a asambleas a nivel nacional.
- Gestión de certificaciones notariales y presentaciones ante organismos como DPPJ y FEHGRA.
- Organización y coordinación de la agenda del presidente de la asociación.
- Atención y resolución de consultas de empresarios vía telefónica y email, derivando eficientemente a áreas legales y contables.

**2023 - 2024 — Inspector de Control de Calidad** • Wenlen S.A. • Bella Vista
- Control de trazabilidad y verificación del correcto armado de válvulas e insumos para la industria de petróleo y gas (normas API 6A y API 6D).
- Detección de desvíos y generación de alertas de calidad ante productos fuera de especificación.
- Verificación de pedidos y control de despachos, asegurando concordancia con órdenes de producción.

**2021 - 2023 — Coordinador de Servicio Técnico** • Kaeser Compresores • Garín
- Coordinación y seguimiento de servicios técnicos (preventivos y de emergencia).
- Gestión de un equipo de 4 técnicos de campo.
- Atención directa a clientes, relevando necesidades y brindando soluciones técnicas.
- Cotización y seguimiento de servicios y repuestos mediante sistema SAP.
- Organización de agenda operativa, optimizando tiempos de respuesta.

**2017 - 2021 — Producción y Oficina Técnica** • ROWA S.A. • Escobar
- Reparación y puesta a punto de productos terminados.
- Ensayos funcionales utilizando bancos de pruebas electroneumáticos y eléctricos.
- Participación en tareas de laboratorio: investigación, desarrollo y mejora de productos.
- Elaboración y gestión de documentación técnica.
""")


