import { React, useState} from 'react'
import { Link } from 'react-router-dom'


function UsersList({ users, setUsers}) {
    const [searchTerm, setSearchTerm] = useState("");

    const onFormSubmission = (e) => {
        e.preventDefault();
    
        setUsers(users.filter((user) => user.username.toLowerCase().includes(searchTerm)));
      };

    const renderUsers = Object.keys(users).map((userID) => (
        <li key={userID}>
            <Link to={`/users/${userID}`}>{users[userID].username}</Link>
        </li>
    ));

  return (
    <div>
      <form onSubmit={onFormSubmission}>
        <label>
          🔎
          <input type="search" value={searchTerm} placeholder="search..." onChange={(e) => setSearchTerm(e.target.value.toLowerCase())} />
        </label>
      </form>
      <ol>{renderUsers}</ol>
    </div>
  );
}

export default UsersList
