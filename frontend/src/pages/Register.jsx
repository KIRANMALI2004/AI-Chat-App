import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../services/api";
import "./register.css";

function Register() {
  const navigate = useNavigate();

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleRegister = async () => {
  if (password !== confirmPassword) {
    alert("Passwords do not match");
    return;
  }

  try {
    const response = await api.post("/auth/register", {
      username: fullName,
      email,
      password,
    });

    alert(response.data.message);

    navigate("/");

  } catch (error) {
    console.log(error.response?.data);

    alert(
      error.response?.data?.message || "Registration Failed"
    );
  }
};

  return (
    <div className="register-container">
      <div className="register-blur"></div>

      <div className="register-card">
        <div className="register-logo">🚀</div>

        <h1>Create Account</h1>

        <p className="subtitle">
          Join AI Chat Assistant and start chatting smarter.
        </p>

        <input
  type="text"
  placeholder="👤 Full Name"
  value={fullName}
  onChange={(e) => setFullName(e.target.value)}
/>

        <input
          type="email"
          placeholder="📧 Email Address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="🔒 Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <input
          type="password"
          placeholder="🔐 Confirm Password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />

        <button onClick={handleRegister}>
          Create Account
        </button>

        <div className="divider">
          <span>OR</span>
        </div>

        <p className="login-text">
          Already have an account?{" "}
          <Link to="/">Login</Link>
        </p>
      </div>
    </div>
  );
}

export default Register;