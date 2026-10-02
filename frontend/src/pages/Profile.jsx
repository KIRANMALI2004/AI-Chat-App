import { useEffect, useState } from "react";
import api from "../services/api";
import "./profile.css";

function Profile() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadProfile();
  }, []);

  const loadProfile = async () => {
    try {
      const res = await api.get("/user/profile");

      setName(res.data.user.name);
      setEmail(res.data.user.email);
    } catch (error) {
      console.error(error);
      alert("Failed to load profile");
    }
  };

  const updateProfile = async () => {
    setLoading(true);

    try {
      await api.put("/user/profile", {
        name,
        email,
      });

      alert("Profile Updated Successfully");
    } catch (error) {
      console.error(error);
      alert("Failed to update profile");
    }

    setLoading(false);
  };

  return (
    <div className="profile-page">
      <div className="profile-card">

        <div className="avatar">
          👤
        </div>

        <h1>My Profile</h1>

        <input
          type="text"
          placeholder="Full Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <button onClick={updateProfile}>
          {loading ? "Updating..." : "Update Profile"}
        </button>

      </div>
    </div>
  );
}

export default Profile;