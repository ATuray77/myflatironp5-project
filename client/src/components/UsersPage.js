import React from 'react'
import { Route, useRouteMatch } from 'react-router-dom'
import UsersList from './UsersList'
import MyCars from './MyCars/MyCars';

function UsersPage({ user, setUser}) {
    console.log(user)
    const match = useRouteMatch();

  return (
    <div>
        <h3>Choose a User to see their information</h3>
        <UsersList users={user} setUsers={setUser}/>
        <Route exact path={match.url}></Route>

        <Route path={`${match.url}/:userID`}>
            <MyCars users={user}/>
        </Route>
      
    </div>
  );
}

export default UsersPage
