import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';
import './EditStudent.css';  // Import the CSS file

const EditStudent = () => {
  const [name, setName] = useState('');
  const [address, setAddress] = useState('');
  const [fee, setFee] = useState('');
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`http://localhost:8000/student/${id}/`)
      .then(response => {
        setName(response.data.name);
        setAddress(response.data.address);
        setFee(response.data.fee);
      })
      .catch(error => console.error(error));
  }, [id]);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.put(`http://localhost:8000/student/${id}/`, { name, address, fee })
      .then(() => navigate('/students'))
      .catch(error => console.error(error));
  };

  return (
    <div className="edit-student">
      <h1>Edit Student</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} required />
        <input type="text" placeholder="Address" value={address} onChange={e => setAddress(e.target.value)} required />
        <input type="number" placeholder="Fee" value={fee} onChange={e => setFee(e.target.value)} required />
        <button type="submit" className="btn">Update Student</button>
      </form>
      <button className="btn" onClick={() => navigate('/students')}>Back to Student List</button>
    </div>
  );
};

export default EditStudent;
