import { useState, useRef, useEffect } from "react";
import api from "../services/api";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

import {
  Bot,
  Send,
  Paperclip,
  Mic,
  Plus,
  MessageSquare,
} from "lucide-react";

import "./chat.css";

function Chat() {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: "👋 Hello Kiran! Welcome to AI Chat Assistant.",
    },
  ]);
  const fileInputRef = useRef(null);

const uploadFile = async (event) => {
  console.log("📎 uploadFile called");

  const file = event.target.files[0];

  if (!file) {
    console.log("No file selected");
    return;
  }

  console.log(file);

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await api.post("/upload/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    console.log(response.data);

localStorage.setItem(
  "uploadedText",
  response.data.text
);

setMessages((prev) => [
  ...prev,
  {
    sender: "ai",
    text: "✅ " + response.data.filename + " uploaded successfully.",
  },
]);
  } catch (error) {
    console.error("Upload Error:", error.response || error);

    setMessages((prev) => [
      ...prev,
      {
        sender: "ai",
        text: "❌ Upload Failed",
      },
    ]);
  }
};
    const {
  transcript,
  listening,
  resetTranscript,
  browserSupportsSpeechRecognition,
} = useSpeechRecognition();

console.log("Browser Support:", browserSupportsSpeechRecognition);
console.log("Listening:", listening);
console.log("Transcript:", transcript);

useEffect(() => {
  console.log("Transcript Updated:", transcript);
  setMessage(transcript);
}, [transcript]);

if (!browserSupportsSpeechRecognition) {
  return <h2>Your browser does not support speech recognition.</h2>;
}
    const sendMessage = async () => {
  if (!message.trim()) return;

  const userMessage = message;

  setMessages((prev) => [
    ...prev,
    { sender: "user", text: userMessage },
  ]);

  setMessage("");
  resetTranscript();

  try {
    const response = await api.post(
  "/chat/ask",
  {
    message:
  localStorage.getItem("uploadedText")
    ? "Document:\n" +
      localStorage.getItem("uploadedText") +
      "\n\nQuestion: " +
      userMessage
    : userMessage,
  }
);

console.log(response.data);
const aiReply = response.data.reply;

setMessages((prev) => [
  ...prev,
  {
    sender: "ai",
    text: aiReply,
  },
]);
window.speechSynthesis.cancel();

const speech = new SpeechSynthesisUtterance(aiReply);

speech.lang = "en-US";
speech.rate = 1;
speech.pitch = 1;

window.speechSynthesis.speak(speech);
  } catch (error) {
    console.error(error);

 setMessages((prev) => {
  const updated = [
    ...prev,
    {
      sender: "ai",
      text: "❌ Failed to get AI response.",
    },
  ];

  console.log(updated);

  return updated;
});
  }
};
  return (
    <div className="chat-page">

      <aside className="chat-sidebar">

        <div className="chat-logo">
          <Bot size={30}/>
          <span>AI Assistant</span>
        </div>

        <button className="new-chat">
          <Plus size={18}/>
          New Chat
        </button>

        <div className="history">

          <div className="history-item">
            <MessageSquare size={16}/>
            React Project
          </div>

          <div className="history-item">
            <MessageSquare size={16}/>
            Flask API
          </div>

          <div className="history-item">
            <MessageSquare size={16}/>
            MongoDB
          </div>

        </div>

      </aside>

      <main className="chat-main">

        <div className="chat-header">
          AI Chat Assistant
        </div>

        <div className="messages">

          {messages.map((msg,index)=>(

            <div
              key={index}
              className={
                msg.sender==="user"
                ?"bubble user"
                :"bubble ai"
              }
            >
              {msg.text}
            </div>

          ))}

        </div>

        <div className="input-box">

          <>
  <input
    type="file"
    ref={fileInputRef}
    style={{ display: "none" }}
    onChange={uploadFile}
  />

  <button onClick={() => fileInputRef.current.click()}>
    <Paperclip size={18} />
  </button>
</>

          <input
            value={message}
            onChange={(e)=>setMessage(e.target.value)}
            placeholder="Ask anything..."
          />
<button
  onClick={() => {
    console.log("🎤 Mic clicked");

    if (listening) {
      console.log("🛑 Stop listening");
      SpeechRecognition.stopListening();
    } else {
      console.log("🎙️ Start listening");

      resetTranscript();

      SpeechRecognition.startListening({
        continuous: true,
        language: "en-US",
      });
    }
  }}
>
  <Mic size={18} color={listening ? "red" : "black"} />
</button>
<button
  className="send-btn"
  onClick={() => {
    console.log("Send button clicked");
    sendMessage();
  }}
>
  <Send size={18} />
</button>
<button
  onClick={() => window.speechSynthesis.cancel()}
>
  Stop Voice
</button>

        </div>

      </main>

    </div>
  );
}

export default Chat;