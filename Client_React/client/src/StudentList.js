import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './StudentList.css';  // Import the CSS file

const StudentList = () => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/student/')
      .then(response => setStudents(response.data))
      .catch(error => console.error(error));
  }, []);

  const deleteStudent = (id) => {
    axios.delete(`http://localhost:8000/student/${id}/`)
      .then(() => setStudents(students.filter(student => student.id !== id)))
      .catch(error => console.error(error));
  };

  return (
    <div className="student-list">
      <h1>Student List</h1>
      <Link to="/"><button className="btn">Back to Home</button></Link>
      <ul>
        {students.map(student => (
          <li key={student.id}>
            {student.name} - {student.address} - {student.fee}
            <Link to={`/edit/${student.id}`}><button className="btn">Edit</button></Link>
            <button className="btn" onClick={() => deleteStudent(student.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StudentList;
