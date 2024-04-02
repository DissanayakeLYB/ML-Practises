import streamlit as st

def main():
    st.title("LASITH DISSANAYAKE")

    # About section
    st.header("ABOUT ME")
    #st.image("/portfolio/images/pixelcut-export.png", use_column_width=True)
    st.write("""
    Hi there! I'm Lasith, a passionate programmer and technology enthusiast. 
    I love building cool stuff and learning new things.
    """)

    # Interests section
    st.header("INTERESTS")
    st.write("""
    Some of my interests include:
    - Machine Learning and Artificial Intelligence
    - Web Development
    - Data Science and Analytics
    - Open Source Contribution
    """)

    # Projects section
    st.header("PROJECTS")
    st.write("""
    Here are a few projects I've worked on recently:

    1. [Project 1](#) - Description of Project 1.
       - Technologies used: Python, Flask, HTML/CSS, Bootstrap
       - ![Project 1](project1.jpg)
    2. [Project 2](#) - Description of Project 2.
       - Technologies used: Python, TensorFlow, React
       - ![Project 2](project2.jpg)
    3. [Project 3](#) - Description of Project 3.
       - Technologies used: Python, Django, PostgreSQL
       - ![Project 3](project3.jpg)
    """)

    # Contact section
    st.header("CONTACT")
    st.write("""
    Feel free to reach out to me via email at [lasithdissanayake.official@gmail.com](mailto:lasithdissanayake.official@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/lasith-dissanayake-430853192/).
    """)

    # Footer
    st.markdown("---")
    st.write("""
    © 2024 My Portfolio | Built with Streamlit
    """)

    # Contact form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message", height=200)
    if st.button("Send"):
        # Code to send email goes here
        st.success("Message sent successfully!")

if __name__ == "__main__":
    main()
