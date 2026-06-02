# Socket + Streamlit Chat Application

This project demonstrates a basic chat system using **Python sockets** for networking and **Streamlit** for the client interface.

## 📂 Project Structure
- **server.py** → Python socket server code
- **client.py** → Streamlit-based chat client code

## 🚀 How It Works
1. **Server (`server.py`)**
   - Creates a TCP socket bound to `127.0.0.1:6000`.
   - Waits for a client connection.
   - Receives messages from the client and allows the server operator to reply via console input.
   - Ends the chat when either side types `exit`.

2. **Client (`client.py`)**
   - Built with Streamlit for a simple web interface.
   - Connects to the server at `127.0.0.1:6000`.
   - Displays chat history inside the Streamlit app.
   - Provides input box and buttons to send messages or exit the chat.
   - Handles server disconnection gracefully.

## ▶️ Running the Application
1. Start the **server**:
   ```bash
   python server.py

2. Run the client with Streamlit
   ```bash
   streamlit run client.py

