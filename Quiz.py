import streamlit as st
def un():

def gq():
    st.write(f"hello Mr. {uname}")
      st.title("🧠 Quiz App")
    q= ["""**Q1:** What is the capital of India?
        A. Mumbai
        B. Kolkata
        C. New Delhi
        D. Chennai""",
         """**Q2:** Who painted the Mona Lisa?
        A. Vincent van Gogh
        B. Leonardo da Vinci
        C. Pablo Picasso
        D. Claude Monet""",
         """**Q3:** What is the chemical symbol for water?
         A. o2
         B. co2
         C. h2o
         D. nacl""",
         """**Q4:** Which is the largest continent by land area?
         A. Africa
         B. North America
         C. Asia
         D. Europe """,
         """**Q5:** Which of these is a primary color?
         A. Green
         B. Orange
         C. Purple
         D. Blue """,
         """**Q6:** What is the currency of the United States?
         A. Euro
         B. Yen
         C. Dollar
         D. Pound""",
         """**Q7:** Which planet is known as the Red Planet?
         A. Earth
         B. Mars
         C. Jupiter
         D. Saturn""",
         """**Q8:** How many colors are in a rainbow?
         A. 5
         B. 6
         C. 7
         D. 8""",
         """**Q9:** Who invented the telephone?
         a) Thomas Edison
         b) Alexander Graham Bell
         c) Nikola Tesla
         d) Samuel Morse""",
         """**Q10:** Which festival is known as the Festival of Lights?
         a) Holi
         b) Eid
         c) Diwali
         d) Christmas"""]
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

