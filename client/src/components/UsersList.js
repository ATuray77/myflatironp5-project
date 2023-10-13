import { React, useState} from 'react'
import { Link } from 'react-router-dom'



function UsersList({ cars, setCars, users, setUsers}) {
    console.log(users)
    //const [first_name, last_name, email, phone, car] = users
    const [make_model, color, license_plate] = cars
    // const [searchTerm, setSearchTerm] = useState("");

    // const onFormSubmission = (e) => {
    //     e.preventDefault();
    
    //     setUsers(users.filter((user) => user.username.toLowerCase().includes(searchTerm)));
    //   };
//---START OF OLD CODE
    //const renderUsers = Object.keys(users).map((userID) => (
    //     <li key={userID}>
    //         <Link to={`/users/${userID}`}>{users[userID].cars}</Link>
    //     </li> 
    // ));
//---END OF OLD CODE
    const renderUsers = Object.keys(cars).map((user_id) => (
        <div key={user_id}> 
            <li key={user_id}> cars: {cars[make_model]}</li>

        </div>
        ));

    return (
        <>
        <ol>{renderUsers}</ol>
        </>
    )     

}

export default UsersList











