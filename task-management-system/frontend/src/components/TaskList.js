import React, { useState, useEffect } from "react";
import API from "../api";

export default function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const fetchTasks = async () => {
    const token = localStorage.getItem("token");
    if (!token) return;
    try {
      const res = await API.get("/tasks", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setTasks(res.data);
    } catch (err) {
      console.error("Failed to fetch tasks", err);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const addTask = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    if (!token) {
      alert("Please log in first.");
      return;
    }
    try {
      await API.post(
        "/tasks",
        { title, description: "" },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setTitle("");
      fetchTasks();
    } catch (err) {
      alert("Failed to add task.");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "2rem" }}>
      <h2>Your Tasks</h2>
      <form onSubmit={addTask} style={{ marginBottom: "1rem" }}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="New task"
          required
        />
        <button type="submit" style={{ marginLeft: "0.5rem" }}>
          Add
        </button>
      </form>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {tasks.map((t) => (
          <li key={t._id}>
            {t.title} — <strong>{t.completed ? "Done" : "Open"}</strong>
          </li>
        ))}
      </ul>
    </div>
  );
}
