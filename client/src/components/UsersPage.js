import React from 'react'
import { Route, useRouteMatch } from 'react-router-dom'
import UsersList from './UsersList'

function UsersPage({ user, setUser}) {
    const match = useRouteMatch();

  return (
    <div>
        <h3>Choose a User to see their information</h3>
        <UsersList user={user} setUser={setUser}/>
        <Route exact path={match.url}></Route>
      
    </div>
  )
}

export default UsersPage
