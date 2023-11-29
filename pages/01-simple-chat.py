import streamlit as st

st.title("Echo Bot")
st.markdown("#### Mirror your response!")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = []
    st.balloons()

# Display chat chat from history on app rerun
for message in st.session_state.chat:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.chat.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.chat.append(
        {"role": "assistant", "content": response})
