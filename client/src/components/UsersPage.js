import React from 'react'
import { Route, useRouteMatch } from 'react-router-dom'
import UsersList from './UsersList'

function UsersPage({ users, setUsers}) {
    const match = useRouteMatch();

  return (
    <div>
        <h3>Choose a User to see their information</h3>
        <UsersList users={users} setUsers={setUsers}/>
        <Route exact path={match.url}></Route>
      
    </div>
  )
}

export default UsersPage
