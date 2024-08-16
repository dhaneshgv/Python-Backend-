import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import HomePage from './HomePage';
import StudentList from './StudentList';
import AddStudent from './AddStudent';
import EditStudent from './EditStudent';
import LoginPage from './LoginPage';
import SignupPage from './SignupPage';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check authentication status from localStorage or cookies
    const token = localStorage.getItem('token');
    setIsAuthenticated(!!token);
  }, []);

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setIsAuthenticated(false);
  };

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={isAuthenticated ? <Navigate to="/" /> : <LoginPage onLogin={handleLogin} />} />
          <Route path="/signup" element={isAuthenticated ? <Navigate to="/" /> : <SignupPage />} />
          <Route path="/" element={isAuthenticated ? <HomePage onLogout={handleLogout} /> : <Navigate to="/login" />} />
          <Route path="/students" element={isAuthenticated ? <StudentList /> : <Navigate to="/login" />} />
          <Route path="/add" element={isAuthenticated ? <AddStudent /> : <Navigate to="/login" />} />
          <Route path="/edit/:id" element={isAuthenticated ? <EditStudent /> : <Navigate to="/login" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
