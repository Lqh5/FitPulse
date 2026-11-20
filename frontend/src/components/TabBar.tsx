import { NavLink, useLocation } from "react-router-dom";

const tabs = [
  { path: "/", label: "Coach", icon: "💬" },
  { path: "/plan", label: "Plan", icon: "📋" },
  { path: "/correction", label: "Correct", icon: "📷" },
  { path: "/profile", label: "Profile", icon: "👤" },
];

export default function TabBar() {
  const location = useLocation();

  return (
    <nav className="tab-bar">
      {tabs.map((tab) => (
        <NavLink
          key={tab.path}
          to={tab.path}
          className={`tab-item ${location.pathname === tab.path ? "active" : ""}`}
        >
          <span className="text-xl">{tab.icon}</span>
          <span>{tab.label}</span>
        </NavLink>
      ))}
    </nav>
  );
}