import { Routes, Route } from "react-router-dom";
import ChatPage from "./pages/ChatPage";
import PlanPage from "./pages/PlanPage";
import CorrectionPage from "./pages/CorrectionPage";
import ProfilePage from "./pages/ProfilePage";
import AdminKnowledgePage from "./pages/AdminKnowledgePage";
import AdminUsersPage from "./pages/AdminUsersPage";
import AdminDashboardPage from "./pages/AdminDashboardPage";
import TabBar from "./components/TabBar";

export default function App() {
  return (
    <div className="max-w-mobile mx-auto min-h-screen bg-white relative">
      <Routes>
        <Route path="/" element={<ChatPage />} />
        <Route path="/plan" element={<PlanPage />} />
        <Route path="/correction" element={<CorrectionPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/admin/knowledge" element={<AdminKnowledgePage />} />
        <Route path="/admin/users" element={<AdminUsersPage />} />
        <Route path="/admin/dashboard" element={<AdminDashboardPage />} />
      </Routes>
      {/* TabBar only shows on user pages, not admin */}
      <Routes>
        <Route path="/admin/*" element={null} />
        <Route path="*" element={<TabBar />} />
      </Routes>
    </div>
  );
}