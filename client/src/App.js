import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './pages/App';
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
      </Routes>
      <Footer />
    </Router>
  );
}

export default AppWrapper;