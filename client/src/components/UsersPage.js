import React from 'react'
import { Route, useRouteMatch } from 'react-router-dom'
import UsersList from './UsersList'
import MyCars from './MyCars/MyCars';

function UsersPage({ user, setUser }) {
    console.log(user)
    //const match = useRouteMatch();

    if (!user.cars) {
      return  <div> Loading...</div>
    }
    
  return (
    <div>
        <h3>Choose a User to see their information</h3>
       
        <MyCars user={user} cars={user.cars} />
      
    </div>
  );
}

export default UsersPage
