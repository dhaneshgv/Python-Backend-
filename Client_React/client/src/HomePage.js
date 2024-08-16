import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

function HomePage({ onLogout }) {
  const handleLogout = () => {
    localStorage.removeItem('token');
    onLogout();
  };

  return (
    <div className="home-container">
      <h1>Welcome to the Student Management System</h1>
      <button onClick={handleLogout}>Logout</button>
      <nav>
        <Link to="/students">View Students</Link>
        <Link to="/add">Add Student</Link>
      </nav>
    </div>
  );
}

export default HomePage;
