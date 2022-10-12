from pathlib import Path
import pandas as pd
import streamlit as st
from PIL import Image
im = Image.open("favicon.ico")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV1.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
experience_letter= current_dir / "assets" / "experience_letter.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ashis Tiwari"
# PAGE_ICON = ":wave:"
NAME = "Ashis Tiwari"
DESCRIPTION = """
Senior Analyst @ Ernst and Young(EY) LLP, enthusiast about ₿ Cryptocurrency and small investor🚀.
"""
EMAIL = "ashistiwari2@gmail.com "
W_EMAIL='Ashis.Tiwari@in.ey.com'
C_EMAIL="ashis_201800333@smit.smu.edu.in"
SOCIAL_MEDIA = {
    "🎫Instagram": "https://www.instagram.com/ashistiwari2",
    "LinkedIn ⬜🟦🟦🟦🟦🟦⬜
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟩🟦⬜🟦🟩🟦
🟦🟩🟦🟩🟦⬜🟦
🟦🟩🟦🟦🟦⬜🟦
⬜🟦🟦🟦🟦🟦🟩": "https://www.linkedin.com/in/ashis-tiwari-9aa527213/",
    "Github⚽⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫🌚🌕⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫🌚⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚪⚪⚪🌚🌚🌚⚫🐘🌕🌚⚫🌕⚪🌚⚪⚪🌕⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚🌚⚪⚪⚪⚪⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫🌕⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🐘⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫🌕⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫🌕⚪⚪⚪⚪
⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫🌕⚪⚪⚪⚪
⚪⚪⚪⚪⚪🌕⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚫⚫⚫🌕⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪🌕⚫⚫⚫🐘🌕⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫🌕⚫⚫⚫⚫⚫🌕⚪⚪⚪⚪⚪🐘⚫⚫⚫⚫⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫🌚⚪⚫⚫⚫🐘⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪🌕⚫⚫⚫⚪⚪⚫⚫🌚⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚫⚫⚫⚫⚪⚪🌚⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫⚫⚫🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚🐘⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚫⚫⚫⚫🌚⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚🌚🌚⚫⚫⚪⚪⚪⚪⚪⚪⚪⚫⚫🐘🌚🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚🐘⚪⚪⚪⚪⚪⚪⚪🌚🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
": "https://github.com/ashistiwari2",
    "🏉Twitter": "https://twitter.com/Ashis_Tiwari_2",
}
PROJECTS = {
    "🏆 Twitter Sentiment Analysis App": "https://ashistiwari2-twitter-sentiment-analysis-app-1-appapp-n0hrlq.streamlitapp.com/",
    "🏆 Machine Learning Model(for predicting fish species)": "https://ashistiwari2-streamlit-app-main-s513q8.streamlitapp.com/",
    "🏆 Small Newsletter form using MongoDB ": "https://ashistiwari.herokuapp.com/",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=im)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("💼 ",W_EMAIL)
    st.write("🎓",C_EMAIL )


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader('Objective')
st.write("---")
st.write(
    """
    To build up my experience and learn problem solving
    in every possibility to make a mark on my career with
    guidance by leaders of this organization. 
    To get best out of internship given by this organization 
    to build up for future career. 
    Life will be Enlighten by learning new things. 
    Belonging to humble background, 
    we all are well versatile with ethics and morale value. 
    To respect the work given by this organization
    and do it by gathering idea from this organization’s great leader. 
    From village boy to building superscalar worker
     is indeed a needed perspective of job.
    """
)
st.write('\n')
st.subheader('Education')
st.write("---")
cols = ['Subject/Course', 'Board/university board', 'School/college','year','Class/Degree']
education=[['Science,Math,Social Science,Hindi,English','CBSE','Pinegrove School, Dharampur,Himachal Pradesh','2015-2016','10'],
           ['Physic,Chemistry,Mathematics,Physical Education,English','CBSE','Pinegrove School, Dharampur,Himachal Pradesh','2016-2018','12'],
           ['Computer Science and Engineering ','Sikkim Manipal University','Sikkim Manipal Institute of Technology','2018-2022','B.Tech']
           ]
edu=education[::-1]
df2 = pd.DataFrame(edu, columns=cols)
st.table(df2)
st.write('\n')
st.write("---")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Good understanding in Python and related Library.
- ✔️ Good hands on experience and knowledge in Fastapi and Docker
- ✔️ Good understanding of Machine Learning Model
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas,Numpy,Fastapi,seaborn), SQL, C++,Java
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees, Linear Discrimant Analysis
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior  Analyst | Ernst and Young(EY) LLP,Kolkata,India**")
st.write("07/2022 - Present")
st.write(
    """
- ► work in team to develop MLOP project
- ► Learned about fastapi,Docker, Jenkins, connecting to Azure database
- ► Deployed Fastapi successfully with using Linear Discrimant Machine Learning  Alogrithm 
"""
)

# --- JOB 2
st.write('\n')
st.write("🈺", "**Intern | Ernst and Young(EY) LLP ,Chennai,India**")
st.write("02/2022 - 06/2022")
st.download_button(
        label="  📖 Experience Letter",
        data=PDFbyte,
        file_name=experience_letter.name,
        mime="application/octet-stream",
    )
st.write(
    """
- ➤ Did Azure certification in AZ-900 and AI-900.
- ➤ Learned About visualization tools like PowerBI and used it to visualize large data.
- ➤ Data manipulation using python library such as numpy and pandas
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


#--- Language known ----
st.write('\n')
st.subheader("Language & Proficiency")
st.write("---")
st.write(
    """
- 🔄 Nepali- Spoken/Native proficiency
- 🔄 English- Spoken/Business proficiency
- 🔄 Hindi - Spoken proficiency
"""
)
st.write('\n')
link = '[Wanna Copy template Click here👈](https://ashistiwari2-copy-digital-cv-main-lvsmxx.streamlitapp.com/)'
st.markdown(link, unsafe_allow_html=True)
st.write('\n')
link1 = '[Leave a message for me here👈](https://ashistiwari2-connect-with-me-main-lrei5a.streamlitapp.com/)'
st.markdown(link1, unsafe_allow_html=True)


