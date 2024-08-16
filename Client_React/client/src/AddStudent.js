import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './AddStudent.css';  // Import the CSS file

const AddStudent = () => {
  const [name, setName] = useState('');
  const [address, setAddress] = useState('');
  const [fee, setFee] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/student/', { name, address, fee })
      .then(() => navigate('/students'))
      .catch(error => console.error(error));
  };

  return (
    <div className="add-student">
      <h1>Add Student</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} required />
        <input type="text" placeholder="Address" value={address} onChange={e => setAddress(e.target.value)} required />
        <input type="number" placeholder="Fee" value={fee} onChange={e => setFee(e.target.value)} required />
        <button type="submit" className="btn">Add Student</button>
      </form>
      <button className="btn" onClick={() => navigate('/students')}>Back to Student List</button>
    </div>
  );
};

export default AddStudent;
