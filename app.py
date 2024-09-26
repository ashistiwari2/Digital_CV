from pathlib import Path
import pandas as pd
import streamlit as st
from PIL import Image
#import hydralit_components as hc
import streamlit.components.v1 as components
import time
from annotated_text import annotated_text
im = Image.open("favicon.ico")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV1.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
experience_letter_ey = current_dir / "assets" / "experience_letter.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ashis Tiwari"
# PAGE_ICON = ":wave:"
NAME = "Ashis Tiwari"
DESCRIPTION = """
Associate consultant @ Ernst and Young(EY) LLP, enthusiast about ₿ Cryptocurrency and small investor🚀.
Holder of BLZ,Polkadot(DOT),MANA,Matic,Dogecoin(DOGE),Synthetix Network Token(SNX)
"""
#PUSH,LCX,LUNC,SWEAT,BABYDOGE,GALA,CHILIZ,NEM,ADA,IOST,ONE,PHB,ETN,WPR,ACT,XVG,LET,ODE,ZEBI
#BNS,BNSD,SPRINK,TLM,FOHO,GARI,BUSD,BNB,XRP,LPT,CHR,BURGER,ALGO,FRONT,HIGH,OM,LSK,TNB,SHIBDOGE,VOLTV2,ALTPAY,SAITANOBI
EMAIL = "ashistiwari2@gmail.com "
W_EMAIL='Ashis.Tiwari@in.ey.com'
C_EMAIL="ashis_201800333@smit.smu.edu.in"
SOCIAL_MEDIA = {
    "🎫Instagram": "https://www.instagram.com/ashistiwari2",
    "🟦LinkedIn": "https://www.linkedin.com/in/ashis-tiwari-9aa527213/",
    "⚽Github": "https://github.com/ashistiwari2",
    "🏉Twitter": "https://twitter.com/Ashis_Tiwari_2",
}
PROJECTS = {
    "🏆 Twitter Sentiment Analysis App": "https://ashistiwari2-twitter-sentiment-analysis-app-1-appapp-n0hrlq.streamlitapp.com/",
    "🏆 Machine Learning Model(for predicting fish species)": "https://ashistiwari2-streamlit-app-main-s513q8.streamlitapp.com/",
    "🏆 Small Newsletter form using MongoDB ": "https://ashistiwari.herokuapp.com/",
    "🏆ToDo List with Nodejs":"https://ashistiwari22.herokuapp.com/"

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=im)
#with hc.HyLoader("Ashis Tiwari CV is Loading wait for seconds",hc.Loaders.standard_loaders,index=5):
    #time.sleep(5)

#with hc.HyLoader('Ashis Tiwari CV is Loading wait for seconds',hc.Loaders.standard_loaders,index=[3,0,5]):
    #time.sleep(5)

#with hc.HyLoader('Ashis Tiwari CV is Loading wait for seconds',hc.Loaders.standard_loaders,index=[2,2,2,2]):
    #time.sleep(5)


components.html(
    """
    <script type="text/javascript" src="https://files.coinmarketcap.com/static/widget/coinMarquee.js"></script><div id="coinmarketcap-widget-marquee" coins="1,1027,825,2586,10407,5994,5617,4195,3513,8425,16086,74" currency="INR" theme="dark" transparent="true" show-symbol-logo="true"></div>
    """
)
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
    annotated_text(" ",("Ashis"," ","#faa"),("Tiwari","⨁","#faa")," ")
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
with st.container ():
    def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
            <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="ashistiwari2" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/ashistiwari2?trk=profile-badge"></a></div>""", 'medium':"""<div style="overflow-y: auto; height:540px;"> <div id="retainable-rss-embed" 
    data-rss="https://medium.com/feed/retainable,https://medium.com/feed/data-science-in-your-pocket"
    <div class="badge-base LI-profile-badge" 
    data-locale="pt_BR" 
    data-size="large" 
    data-theme="light" 
    data-type="HORIZONTAL"
    data-maxcols="3" 
    data-layout="grid"
    data-poststyle="inline" 
    data-readmore="Read the rest" 
    data-buttonclass="btn btn-primary" 
    data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""}
    azure_dp_100={'certi':"""<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="b7ae14df-e829-4e68-b9cc-2ed5ecf9420d" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""}
    embeded_component_1={'twitter':"""<blockquote class="twitter-tweet"><p lang="en" dir="ltr">With great thought, let me take you through short story.<br>If you feel hardwork really payoff then look at people carrying load of sack behind their back, just barely keep both ends meet.<br>And people who smartly invest enjoy a large piece of profit..</p>&mdash; Ashis Tiwari (@Ashis_Tiwari_2) <a href="https://twitter.com/Ashis_Tiwari_2/status/1510101434506768387?ref_src=twsrc%5Etfw">April 2, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>"""}
    embeded_comp_2={'instagram':"""<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/p/CkGbA1nvc-5/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/p/CkGbA1nvc-5/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/CkGbA1nvc-5/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Ashis Tiwari (@ashistiwari2)</a></p></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>"""}
    embeded_comp_3={'github':"""<div class="github-card" data-github="ashistiwari2" data-width="400" data-height="318" data-theme="medium"></div><script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>"""}
    git={'github':"""<div class="github-card" data-user="ashistiwari2"></div> <script src="http://lab.lepture.com/github-cards/widget.js"></script>"""}
    fb={'facebook':"""<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fashistiwari2%2Fposts%2Fpfbid02neCS9JNYx6FWn8cavBjYfVJ3rZK1budbyzxdNLpvswjs2rZfS1JsgjWVgjd5e1dEl&show_text=true&width=500" width="500" height="277" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>"""}
    #scan={'scan':"""<img src="https://chart.googleapis.com/chart?cht=qr&chl=https%3A%2F%2Fapi.whatsapp.com%2Fsend%3Fphone%3D7432047169%26text%3DHi%2520%252CThank%2520You%2520For%2520messaging%2520Me&chs=180x180&choe=UTF-8&chld=L|2" alt="qr code"><a href="www.qr-code-generator.com/" border="0" style="cursor:default" rel="nofollow"></a>"""}
    azure_ai={'certi':"""<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="df9b0f90-c92d-4e25-97c6-4d91cf35f8dc" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""}
    azure_fd={'certi':"""<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="4a73b896-5c22-4ae8-90bf-9f9d7393e240" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""}
    ey_bade_1={'certi':"""<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="837afe26-d5b6-4e63-9b7a-05098745cbad" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""}
    ey_bade_2={'certi':"""<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="ecdce311-0dab-4ee9-90be-ed039cdc3c11" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""}


with st.sidebar:
		components.html(embed_component['linkedin'],height=400)
		components.html(azure_dp_100['certi'],height=335)
		components.html(embeded_component_1['twitter'],height=400)
		components.html(azure_ai['certi'],height=335)
		components.html(embeded_comp_2['instagram'],height=800)
		components.html(azure_fd['certi'],height=335)
		components.html(fb['facebook'],height=300)
		components.html(ey_bade_1['certi'],height=335)
		#components.html(scan['scan'],height=250)
		components.html(ey_bade_2['certi'],height=335)
		
# 		components.html('''
# 			<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
#             <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="ashistiwari2" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/ashistiwari2?trk=profile-badge"></a></div>""", 'medium':"""<div style="overflow-y: auto; height:540px;"> <div id="retainable-rss-embed" 
#     data-rss="https://medium.com/feed/retainable,https://medium.com/feed/data-science-in-your-pocket"
#     <div class="badge-base LI-profile-badge" 
#     data-locale="pt_BR" 
#     data-size="large" 
#     data-theme="light" 
#     data-type="HORIZONTAL"
#     data-maxcols="3" 
#     data-layout="grid"
#     data-poststyle="inline" 
#     data-readmore="Read the rest" 
#     data-buttonclass="btn btn-primary" 
#     data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>
#     <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="b7ae14df-e829-4e68-b9cc-2ed5ecf9420d" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
#     <blockquote class="twitter-tweet"><p lang="en" dir="ltr">With great thought, let me take you through short story.<br>If you feel hardwork really payoff then look at people carrying load of sack behind their back, just barely keep both ends meet.<br>And people who smartly invest enjoy a large piece of profit..</p>&mdash; Ashis Tiwari (@Ashis_Tiwari_2) <a href="https://twitter.com/Ashis_Tiwari_2/status/1510101434506768387?ref_src=twsrc%5Etfw">April 2, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
#     <div class="github-card" data-github="ashistiwari2" data-width="400" data-height="318" data-theme="medium"></div><script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>
#     <div class="github-card" data-user="ashistiwari2"></div> <script src="http://lab.lepture.com/github-cards/widget.js"></script>
#     <iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fashistiwari2%2Fposts%2Fpfbid02neCS9JNYx6FWn8cavBjYfVJ3rZK1budbyzxdNLpvswjs2rZfS1JsgjWVgjd5e1dEl&show_text=true&width=500" width="500" height="277" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>
#     <img src="https://chart.googleapis.com/chart?cht=qr&chl=https%3A%2F%2Fapi.whatsapp.com%2Fsend%3Fphone%3D7432047169%26text%3DHi%2520%252CThank%2520You%2520For%2520messaging%2520Me&chs=180x180&choe=UTF-8&chld=L|2" alt="qr code"><a href="www.qr-code-generator.com/" border="0" style="cursor:default" rel="nofollow"></a>
#     ''',height=1600)
    
			
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
st.write('----------------------------------------------------')
# # components.html(
#     """
#     <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7140902499537328"
#      crossorigin="anonymous"></script>
# <ins class="adsbygoogle"
#      style="display:block"
#      data-ad-format="fluid"
#      data-ad-layout-key="-fb+5w+4e-db+86"
#      data-ad-client="ca-pub-7140902499537328"
#      data-ad-slot="5599862418"></ins>
# <script>
#      (adsbygoogle = window.adsbygoogle || []).push({});
# </script>
# """,height=150)
st.write('--------------------------------------')


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
st.write("💻","**Associate Consultant | Ernst and Young(EY) LLP,Kolkata,India**")
st.write("10/2023 - 09/2024")
st.write(
    """
- ► work in team to Support and develop many project at Hindustan Unilever limited(HUL,India)
- ► Processing of invoice of client to pass on to SAP System using ABBYY and python.
- ► won the Extraordinaires Award as being recognised as Client Extraordinaire.
"""
)
with open("assets/1702176715477.jpg", "rb") as file:
    btn=st.download_button(
    label=" 📖Client Extraordinaire award",
    data=file,
    file_name="Client Extraordinaire award.jpg",
    mime="application/octet-stream"
)

# --- JOB 1
st.write("🚧", "**Senior  Analyst | Ernst and Young(EY) LLP,Kolkata,India**")
st.write("07/2022 - 09/2023")
st.write(
    """
- ► work in team to develop MLOP project
- ► Learned about fastapi,Docker, Jenkins, connecting to Azure database
- ► Deployed Fastapi successfully with using Linear Discrimant Machine Learning  Alogrithm 
- ► Azure certified Data Scientist Associate
"""
)

# --- JOB 2
st.write('\n')
st.write("🈺", "**Intern | Ernst and Young(EY) LLP ,Chennai,India**")
st.write("02/2022 - 06/2022")
# st.download_button(
#         label="📖 Experience Letter",
#         data=experience_letter_ey,
#         file_name=experience_letter_ey.name,
#         mime="application/octet-stream",
#     )
with open("assets/experience_letter.pdf", "rb") as file:
    btn=st.download_button(
    label=" 📖 Experience Letter",
    data=file,
    file_name="experience_letter.pdf",
    mime="application/octet-stream"
)
st.write(
    """
- ➤ Did Azure certification in AZ-900 and AI-900.
- ➤ Learned About visualization tools like PowerBI and used it to visualize large data.
- ➤ Data manipulation using python library such as numpy and pandas
"""
)
# components.html(
#     """
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7140902499537328"
#      crossorigin="anonymous"></script>
    
# </head>
# <body>
# </body>
# </html>
# """,height=200,)
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
# components.html(
#     """
#             <div class="github-card" data-user="ashistiwari2"></div> 
#             <script src="http://lab.lepture.com/github-cards/widget.js"></script>
#             """
#                            ,height=500)
	
# components.html(
#     """
#     <script type="text/javascript" src="https://files.coinmarketcap.com/static/widget/coinPriceBlock.js"></script><div id="coinmarketcap-widget-coin-price-block" coins="1,1027,825,2586,5617,8425" currency="USD" theme="dark" transparent="false" show-symbol-logo="true"></div>
    
#     <br>
#     <br>
    
# """,
#     height=300,)
# st.write("------
col1, col2 = st.columns(2, gap="small")
with col2:
	components.html("""
	<script 
      type="text/javascript"
      src="https://d3mkw6s8thqya7.cloudfront.net/integration-plugin.js"
      id="aisensy-wa-widget"
      widget-id="gLwq0K"
    >
    </script>
    """,height=700)
with col1:
	components.html("""
	</script>
    
    <script src="https://apps.elfsight.com/p/platform.js" defer></script>
<div class="elfsight-app-fd79d4ed-5179-4b71-900c-26160a6805c9"></div>"""
			,height=600)
# components.html(
#     """
#     <!DOCTYPE html>
#  <html lang="en">
#  <head>
#      <meta charset="UTF-8">
  
#         <script src="https://widgets.coingecko.com/coingecko-coin-heatmap-widget.js"></script>
    
#  </head>
#  <body>
#  <coingecko-coin-heatmap-widget  height="400" locale="en" top="100"></coingecko-coin-heatmap-widget>
# </body>
# </html>
    
    

# """,
#     height=600,)
st.write("-------------------------------------------------------------------------------------------")
# components.html(
#     """
     
#     <script 
#       type="text/javascript"
#       src="https://d3mkw6s8thqya7.cloudfront.net/integration-plugin.js"
#       id="aisensy-wa-widget"
#       widget-id="gLwq0K"
#     >
#     </script>
	
#     """,
#     height=500,)
# components.html(
#     """
#     <!DOCTYPE html>
#  <html lang="en">
#  <head>
#      <meta charset="UTF-8">
#     <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7140902499537328"
#      crossorigin="anonymous"></script>
      
    
#  </head>
#  <body>
#  <p>Google Ads</p>
# </body>
# </html>
    
    

# """,
#     height=200,)
# st.write("-------------------------------------------------------------------------------------------")
# components.html(
#     """
#     <script src="https://widgets.coingecko.com/coingecko-random-coin-widget.js"></script>
# <coingecko-random-coin-widget  locale="en" width="0"></coingecko-random-coin-widget>
# """,
#     height=150,)

components.html(
	"""
	<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/6386f692daff0e1306da279e/1gj3j6c8g';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
</script>
<!--End of Tawk.to Script-->
</body>
</html>
""",height=600)
