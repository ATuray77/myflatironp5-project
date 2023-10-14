import React from 'react'
import MyCars from './MyCars/MyCars';

function UsersPage({ cars, user, setUser }) {
    //const match = useRouteMatch();

    if (!user.cars) {
      return  <div> Loading...</div>
    }
    
  return (
    <div>
        {cars.map((car) =>(
            <car key={car.id} car={car}/>
        ))}
       
        <MyCars user={user} cars={user.cars} />
      
    </div>
  );
}

export default UsersPage
