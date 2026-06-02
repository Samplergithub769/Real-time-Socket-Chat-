import streamlit as st
import socket
import time

st.title("Chat Client(Socket+Streamlit)")

if "messages" not in st.session_state:
    st.session_state.messages=[]
if "connected" not in st.session_state:
    st.session_state.connected=False
    
if not st.session_state.connected:
    if st.button("Connected to server"):
        try:
            client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect(("127.0.0.1",6000))
            client.setblocking(False)
            
            st.session_state.client=client
            st.session_state.connected=True
            
        except Exception as E:
            st.error(f"Connection failed:{E}")


def receive_messages():
  try:
      msg=st.session_state.client.recv(1024).decode()
      if msg=="" or msg.lower()=="exit":
          st.session_state.messages.append({
              "role":"server","content":"Server disconnected"
          })
          st.session_state.connected=False
          st.session_state.client.close()
          return
      if msg:
          st.session_state.messages.append({"role":"server","content":msg})         
  except:
      pass
  
def send_messages(): 
    try:
        msg=st.session_state.get("input","")
        
        if msg.lower()=="exit":
            exit_chat()
            return
        if msg:
            st.session_state.client.send(msg.encode())
            st.session_state.messages.append({
                "role":"you","content":msg
            })
            st.session_state.input=""
    except:
        st.session_state.messages.append({
            "role":"system","content":"Send failed(server down)"
        })
        st.session_state.connected=False

def exit_chat(): 
        try:
            st.session_state.client.send("exit".encode())
            st.session_state.client.close()
        except:
            pass
        st.session_state.connected=False
        st.session_state.messages.append({
            "role":"client","content":"Disconnected"
        })   
                   
if st.session_state.connected:
    receive_messages()
    
    for msg in st.session_state.messages:
        st.write(f"{msg['role']}:{msg['content']}")
        
    st.text_input("you:",key="input")
    
    st.button("Send",on_click=send_messages)
    
    st.button("Exit",on_click=exit_chat)
    
    time.sleep(0.3)
    st.rerun()
    
else:
    st.info("Disconnected.Connect to start chat.") 