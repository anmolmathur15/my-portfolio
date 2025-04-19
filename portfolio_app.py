import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Anmol Mathur - Portfolio", page_icon=":briefcase:", layout="wide")

# --- CONTACT INFO ---
NAME = "Anmol Mathur"
LOCATION = "Paderborn, Germany"
EMAIL = "anmolmathur2024@gmail.com"
LINKEDIN_URL = "https://linkedin.com/in/anmolmathur1999"
LINKEDIN_TEXT = "linkedin.com/in/anmolmathur1999" # Text to display for the link

# --- SOCIAL MEDIA (Optional - Add more if needed) ---
SOCIAL_MEDIA = {
    "LinkedIn": LINKEDIN_URL,
    # "GitHub": "https://github.com/your_username", # Example
    # "Twitter": "https://twitter.com/your_username", # Example
}

# --- MAIN CONTENT ---

# --- Header Section ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    # You can add a profile picture here if you have one hosted online
    # st.image("your_image_url.jpg", width=230)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 230px; background-color: #f0f2f6; border-radius: 50%; width: 230px; margin: auto;">
        <span style="font-size: 1.5em; color: #888;">Add Photo</span>
    </div>
    """, unsafe_allow_html=True) # Placeholder for image

with col2:
    st.title(NAME)
    st.write(f"📍 {LOCATION}")
    st.write(f"📧 [{EMAIL}](mailto:{EMAIL})") # Clickable email link
    st.write(f"🔗 [{LINKEDIN_TEXT}]({LINKEDIN_URL})") # Clickable LinkedIn link

    # Display other social media links if any
    if SOCIAL_MEDIA:
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")

st.write("---") # Divider

# --- ABOUT ME ---
st.header("About Me")
st.write(
    """
    Software Engineer, Programmer, Researcher and most importantly Learner.
    Experienced in building applications with Scala, Akka, and Kafka within microservices architectures.
    Passionate about continuous learning and applying technical skills to solve complex problems.
    Currently pursuing a Master's in Computer Engineering with a focus on Machine Learning and Data Driven Engineering.
    """
)
st.write("##") # Add vertical space

# --- SKILLS ---
st.header("Skills")
st.write(
    """
    Below is a summary of my technical and soft skills.
    """
)

# Using columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Languages")
    st.markdown("""
    * Scala (3 years)
    * C/C++
    * Python
    * SQL
    * LaTeX
    """)

with col2:
    st.subheader("Tools")
    st.markdown("""
    * Git & Bitbucket
    * Unix
    * MySQL
    * VS Code & IntelliJ IDEA
    * Docker
    * Teamcity
    """)

with col3:
    st.subheader("Technical Skills")
    st.markdown("""
    * Akka Framework & Actor Model
    * Apache Kafka
    * OOP & LLD
    * SDLC & Agile
    * Networking Fundamentals
    * Automation Testing
    * Concurrent Computation
    * OS & DBMS
    * SaaS Business Model
    * Data Formats (SysML, UML, XML)
    """)

st.write("---") # Divider

col4, col5 = st.columns(2)

with col4:
    st.subheader("Soft Skills")
    st.markdown("""
    * Leadership
    * Time Management
    * Hard Working
    * Teamwork
    * Problem Solving
    * Critical Thinking
    """)

with col5:
    st.subheader("Test Scores & Languages")
    st.markdown("""
    * GRE: 317/340
    * IELTS: 7.5/9
    * Deutsch Proficiency: A1
    """)

st.write("##") # Add vertical space

# --- EXPERIENCE ---
st.header("Experience")
st.write("---")

# --- Ciena ---
st.subheader("Ciena Corp | Gurgaon, India")
st.markdown("**Software Engineer Applications 1B** (Jan 2024 - Sept 2024)")
st.markdown("**Software Engineer Applications 1A** (Oct 2021 - Jan 2024)")
st.markdown("""
* Built applications using Scala, Akka, Apache Kafka and Docker.
* Designed and Implemented new features, performed Debugging and Automation Testing.
* Demonstrated technical expertise in the Telco industry.
* Worked on MCP Network Management Software in Microservices based Architectures creating solutions for routing and switching for Networking and Photonic Data transmission in Optical Networks.
""")
st.write("##")

# --- Wipro ---
st.subheader("Wipro Limited | Delhi, India")
st.markdown("**Project Engineer** (July 2021 – Sept 2021)")
st.markdown("""
* Planned and organized technical projects from conception to completion.
* Utilized engineering knowledge for project management; estimate timelines and schedules.
""")
st.write("##")

# --- Ministry of Defence ---
st.subheader("Ministry of Defence | Delhi, India")
st.markdown("**Research Intern** (June 2019 - July 2019)")
st.markdown("""
* Worked on a project about Output Voltage Compensation of MEMS-Accelerometer with the change in temperature in Embedded C.
* Architected a system which extrapolated data and adjusted the Arduino Microcontroller to compensate for the Voltage values by applying algorithms.
""")
st.write("---") # Divider

# --- EDUCATION ---
st.header("Education")
st.write("---")

# --- Paderborn University ---
st.subheader("Universität Paderborn | North Rhine-Westphalia, Germany")
st.markdown("**Master of Science in Computer Engineering** (Oct 2024 - Present)")
st.markdown("""
* *Coursework:* Statistical Machine Learning, Advanced Computer Architecture, Data Driven Engineering, Statistical Signal Processing, Human Factors in Security & Privacy
""")
st.write("##")

# --- NSIT ---
st.subheader("Netaji Subhas Institute of Technology - University of Delhi | Delhi, India")
st.markdown("**Bachelors of Engineering in Electronics and Communication** (2017-2021)")
st.markdown("*CGPA:* 7.32/10")
st.write("##")

# --- School ---
st.subheader("N. K. Bagrodia Public School | Delhi, India")
st.markdown("**Class 12th - CBSE Board** (2017)")
st.markdown("*Percentage:* 94.4%")
st.write("---") # Divider


# --- PROJECTS ---
st.header("Projects")
st.write("---")

# --- Project 1: Mini Bank ---
with st.expander("**Mini Bank : Scala project with Akka, Cats and Cassandra | Scala**"):
    st.write("""
    * Implemented Akka (typed) Actors for the business logic and Cassandra for storage.
    * Ran an HTTP server with a sleek DSL and REST API.
    * _(Optional: Add a link to the project repository if available)_
    """)

# --- Project 2: Drowsiness Detection ---
with st.expander("**Drowsiness Detection using Deep Learning and Computer Vision | Python**"):
    st.write("""
    * Built a Convolutional Neural Network Model which can predict if a person is drowsy or not using video feed.
    * Created a CNN model with an accuracy of approximately 94%.
    * _(Optional: Add a link to the project repository if available)_
    """)
st.write("---") # Divider


# --- CERTIFICATIONS ---
st.header("Certifications")
st.write("---")
st.markdown("""
* Stanford Online - Supervised Machine Learning: Regression and Classification
* Yale University - Financial Markets (with Honors)
* University of California San Diego - Data Structures
* University of California San Diego - Algorithmic Toolbox
""")
st.write("---") # Divider

# --- VOLUNTEER EXPERIENCE ---
st.header("Volunteer Experience")
st.write("---")
st.subheader("NGO: Shubhakshika Educational Society")
st.markdown("""
* Volunteered 20 hours/month during summer holidays.
* Trained poor and unprivileged children.
* Taught Mathematics and Science to up to 30 primary school students per day.
""")
st.write("---") # Divider

# --- Footer ---
st.write(" ") # Add some space before footer
st.write("© Anmol Mathur | Built with Streamlit")

