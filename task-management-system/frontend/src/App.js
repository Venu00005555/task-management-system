import React from "react";
import TaskList from "./components/TaskList";
import Login from "./components/Login";
import Register from "./components/Register";

export default function App() {
  return (
    <div style={{ padding: 20, fontFamily: "Arial, sans-serif", textAlign: "center" }}>
      <h1 style={{ color: "#333" }}>Task Management System</h1>

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "flex-start",
          gap: 30,
          marginTop: 20,
        }}
      >
        <div style={{ flex: 1, maxWidth: 300 }}>
          <Register />
          <hr style={{ margin: "1.5rem 0" }} />
          <Login />
        </div>

        <div style={{ flex: 2, maxWidth: 500 }}>
          <TaskList />
        </div>
      </div>
    </div>
  );
}
