import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './pages/App';
import DashboardPage from './pages/DashboardPage';
import MePage from './pages/MePage'; 
import MyTeamPage from './pages/MyTeamPage'; 
import OrganizationPage from './pages/OrganizationPage'; 
import ProfilePage from './pages/ProfilePage';
import Header from './components/Header';
import Footer from './components/Footer';
import './App.css';

function AppWrapper() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/app" element={<App />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/me" element={<MePage />} />
        <Route path="/myteam" element={<MyTeamPage />} />
        <Route path="/organization" element={<OrganizationPage />} />
        <Route path="/profile" element={<ProfilePage />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default AppWrapper;