import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

// Get the root container element
const container = document.getElementById("root");

// Create a React root and render the main App component
const root = createRoot(container);
root.render(<App />);
