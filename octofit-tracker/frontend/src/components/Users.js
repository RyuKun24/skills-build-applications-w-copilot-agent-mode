import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Users: fetching from', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Users: fetched data', data);
        setUsers(Array.isArray(data) ? data : data.results || []);
      })
      .catch(err => console.error('Users fetch error:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Username</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user, idx) => (
            <tr key={user._id || idx}>
              <td>{user.username}</td>
              <td>{user.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Users;
