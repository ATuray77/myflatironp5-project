import React from 'react'
import MyCars from './MyCars/MyCars';

function UsersPage({ cars, user, setUser }) {

    
    
  return (
    <div>
    
       
        <MyCars user={user} cars={user.cars} />
      
    </div>
  );
}

export default UsersPage
