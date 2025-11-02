import streamlit as st
#def un():

def gq():
    st.write(f"hello Mr. {uname}")
    st.title("🧠 Quiz App")
    q= ["""**Q1:** What is the capital of India?
    \nA. Mumbai
    \nB. Kolkata
    \nC. New Delhi
    \nD. Chennai""",
         """**Q2:** Who painted the Mona Lisa?
       \n A. Vincent van Gogh
        \nB. Leonardo da Vinci
        \nC. Pablo Picasso
        \nD. Claude Monet""",
         """**Q3:** What is the chemical symbol for water?
         \nA. o2
         \nB. co2
         \nC. h2o
         \nD. nacl""",
         """**Q4:** Which is the largest continent by land area?
         \nA. Africa
         \nB. North America
         \nC. Asia
         \nD. Europe """,
         """**Q5:** Which of these is a primary color?
        \n A. Green
         \nB. Orange
         \nC. Purple
         \nD. Blue """,
         """**Q6:** What is the currency of the United States?
        \n A. Euro
         \nB. Yen
         \nC. Dollar
         \nD. Pound""",
         """**Q7:** Which planet is known as the Red Planet?
         \nA. Earth
         \nB. Mars
         \nC. Jupiter
         \nD. Saturn""",
         """**Q8:** How many colors are in a rainbow?
         \nA. 5
         \nB. 6
         \nC. 7
         \nD. 8""",
         """**Q9:** Who invented the telephone?
         \na) Thomas Edison
         \nb) Alexander Graham Bell
         \nc) Nikola Tesla
         \nd) Samuel Morse""",
         """**Q10:** Which festival is known as the Festival of Lights?
         \na) Holi
         \nb) Eid
         \nc) Diwali
         \nd) Christmas"""]
    ans = ["c", "b", "c", "c", "d", "c", "b", "c", "b", "c"]
    ua = []
    sum = 0
    for i in range(10):
        st.write(q[i])
        uas = st.text_input("choose option...",key=i)
        st.write("---")
        ua.append(uas)
        if ua[i] == ans[i]:
            sum = sum + 10
            st.balloons()
    st.write(sum)
    if sum == 100:
        st.write("you got 100 points you are topper")
    elif sum == 90:
        st.write("you got 90 points you are intermediate")
    elif sum == 80:
        st.write("you got 80 points work on your general knowledge")
    elif sum == 70:
        st.write("you got 70 points you are topper")
    elif sum == 60:
        st.write("you got 60 points you are intermediate")
    elif sum == 50:
        st.write("you got 50 points work on your general knowledge")
    elif sum == 40:
        st.write("you got 40 points you are topper")
    elif sum == 30:
        st.write("you got 30 points you are intermediate")
    elif sum == 20:
        st.write("you got 20 points work on your general knowledge")
    elif sum == 10:
        st.write("you got 10 points work on your general knowledge")
    else:
        st.write("better luck next time")

uname=st.text_input("enter your name")
# un()
gq()
st.sidebar.button("Restart")
# if but==1:
    
