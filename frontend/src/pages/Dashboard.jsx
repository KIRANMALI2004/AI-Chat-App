import { Link } from "react-router-dom";
import {
  MessageSquare,
  Plus,
  Search,
  Settings,
  User,
  Crown,
  Bot,
} from "lucide-react";

import "./dashboard.css";

function Dashboard() {
  const chats = [
    "Build AI Chat App",
    "React Interview",
    "Flask JWT Guide",
    "MongoDB CRUD",
    "Python Questions",
    "Machine Learning",
  ];

  return (
    <div className="dashboard">

      <aside className="sidebar">

        <div className="logo">
          <Bot size={34} />
          <span>AI Assistant</span>
        </div>

        <button className="new-chat">
          <Plus size={18} />
          New Chat
        </button>

        <div className="search-box">
          <Search size={18} />
          <input
            type="text"
            placeholder="Search conversations..."
          />
        </div>

        <div className="chat-history">

          <h4>Recent Chats</h4>

          {chats.map((chat, index) => (
            <div className="chat-item" key={index}>
              <MessageSquare size={18} />
              {chat}
            </div>
          ))}

        </div>

        <div className="pro-card">
          <Crown size={28} />
          <h3>AI Pro</h3>
          <p>Unlock GPT-5, Image AI and more.</p>

          <button>Upgrade</button>
        </div>

        <div className="bottom-menu">

          <Link to="/profile">
            <User size={18} />
            Profile
          </Link>

          <Link to="/settings">
            <Settings size={18} />
            Settings
          </Link>

        </div>

      </aside>

      <main className="content">

        <div className="welcome">

          <h1>
            Welcome Back 👋
          </h1>

          <p>
            What would you like to build today?
          </p>

          <Link to="/chat/1">
            <button className="start-btn">
              Start New Chat
            </button>
          </Link>

        </div>

      </main>

    </div>
  );
}

export default Dashboard;