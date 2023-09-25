import Login from './components/auth/login';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './components/home/home';
import { useState, useEffect } from 'react';


function App() {
  const isTokenExpired = () => {
    const expiration = localStorage.getItem('tokenExpiration');
    if (!expiration) return true;

    const currentTime = new Date().getTime();
    return currentTime > parseInt(expiration, 10);
  };
  const [isAuthenticated, setIsAuthenticated] = useState(
    isTokenExpired() ? false : true
  );

  useEffect(() => {
    // Check authentication status from local storage or any other method
    const token = localStorage.getItem('token');
    if (token) {
      setIsAuthenticated(true);
    }
  }, []);
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
        <Route exact path="/" element={isAuthenticated ? <Home /> : <Navigate to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;
