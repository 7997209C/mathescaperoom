import streamlit as st 

# st.title("Math Escape Room")

# Questions and answers
questions = [
    {
        "image": "l1.png",
        "story": "a mummy is telling you: In order to escape, you must find the volume of the pyramid you are in. Here are the dimensions: width 100, height 49, depth 24.",
        "question": "What is the volume of the pyramid?",
        "answer": "39200"
    },
    {
        "image": "l2.png",
        "story": "you see a camel and a guide on a camel that weighs 13 pounds. The guide also has 4 more camels that have gifts on them which are very heavy. Now the camels together weigh 52 pounds.",
        "question": "What is the total weight of the gifts on the camels?",
        "answer": "39"
    },
    {
        "image": "l3.png",
        "story": "After solving the camel puzzle, you reach an ancient temple. To open the gate, you need to solve another riddle. The gatekeeper says: 'I am thinking of a number. If you multiply it by 2 and then subtract 5, you get 9. What is the number?'",
        "question": "What is the number?",
        "answer": "7"
    },
    {
        "image": "l22.png",
        "story": "You arrive at a village where a festival is taking place. To enter the festival, you must solve this problem: The ticket price for adults is 12, and for children, its 7. If a family of 2 adults and 3 children goes to the festival, how much do they need to pay in total?",
        "question": "How much do they need to pay in total?",
        "answer": "45"
    },
    {
        "image": "l5.png",
        "story": "With the treasure in hand, you encounter a bridge guarded by a troll. The troll will only let you pass if you solve his riddle: 'I have three daughters. Each of them has a brother. How many children do I have?'",
        "question": "How many children does the troll have?",
        "answer": "4"
    }
]

# Function to display the question
def show_question(index):
    st.image(questions[index]['image'])
    st.subheader(questions[index]['story'])
    st.subheader(questions[index]['question'])
    answer = st.text_input("Your answer:", key=index)
    if st.button("Submit"):
        if answer == questions[index]['answer']:
            st.success("Correct! Moving to the next question...")
            st.session_state['question_index'] += 1
            st.experimental_rerun()
        else:
            st.error("Incorrect. Try again!")

# Main function
def main():
    st.title("5th Grade Math Adventure Game")
   
    if 'question_index' not in st.session_state:
        st.session_state['question_index'] = 0

    if st.session_state['question_index'] >= len(questions):
        st.write("Congratulations! You've completed the game.")
        st.balloons()
    else:
        show_question(st.session_state['question_index'])

# Start the app
if __name__ == "__main__":
    main()

