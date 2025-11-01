questions = [
    """**Q1:** What is the capital of France?  
A. Berlin  
B. Madrid  
C. Paris  
D. Rome""",
    """**Q2:** Which planet is known as the Red Planet?  
A. Earth  
B. Mars  
C. Venus  
D. Jupiter""",
    """**Q3:** What is 5 + 3?  
A. 5  
B. 8  
C. 10  
D. 15""",
    """**Q4:** What color is the sky?  
A. Green  
B. Blue  
C. Yellow  
D. Red""",
    """**Q5:** Which of these is a primary color?  
A. Green  
B. Orange  
C. Purple  
D. Blue"""
]
ans=["a","b","b","b","b"]
st.title("🧠 Quiz App")
sum=0
for i in range (0,5):
    st.write(questions[i])
    ua =st.text_input("Your answer:", key=i)  # Each input gets a unique key
    st.write("---------------------------")  # Adds a line separator between questions
    if ua==ans[i]:
        st.balloons()
        sum=sum+10

st.sidebar.button("restart")
st.write(f"your score is = {sum}")
