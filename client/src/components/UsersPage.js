import React from 'react'
import MyCars from './MyCars/MyCars';

function UsersPage({ cars, user, setUser, handleDeleteCar}) {



    
    
  return (
    <div>
        <MyCars user={user} cars={user.cars} handleDeleteCar={handleDeleteCar} />
    </div>
  );
}

export default UsersPage
