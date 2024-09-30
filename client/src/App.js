import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './pages/App';
import DashboardPage from './pages/DashboardPage';
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
        <Route path="/dashboard" element={<DashboardPage />} /> {/* Added DashboardPage route */}
      </Routes>
      <Footer />
    </Router>
  );
}

export default AppWrapper;