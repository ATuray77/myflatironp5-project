import { React, useState} from 'react'
import { Link } from 'react-router-dom'



function UsersList({ users, setUsers}) {
    console.log(users)
    //const [first_name, last_name, email, phone, car] = users
    // const [searchTerm, setSearchTerm] = useState("");

    // const onFormSubmission = (e) => {
    //     e.preventDefault();
    
    //     setUsers(users.filter((user) => user.username.toLowerCase().includes(searchTerm)));
    //   };

    const renderUsers = Object.keys(users).map((userID) => (
        <li key={userID}>
            <Link to={`/users/${userID}`}>{users[userID].username}</Link>
        </li> 
    ));
    console.log(renderUsers)
    return (
        <>
        <ol>{renderUsers}</ol>
        </>
    )     
}

export default UsersList











