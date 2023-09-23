import Login from './components/auth/login';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './components/home/home';


function App() {
  const isAuthenticated = false;
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route exact path="/" element={isAuthenticated ? <Home /> : <Navigate to="/login" />} />

      </Routes>
    </Router>
  );
}

export default App;
