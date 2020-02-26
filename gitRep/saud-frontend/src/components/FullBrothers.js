import React, {useState, useEffect} from 'react'
import axios from 'axios'


function FullBrothers() {
    const [fullBrothers, setFullBrothers] = useState(
        []
    )
    
    // this is how to use awaits with use effects
    // async function fetchApi() {
    //   let res = await axios.get('https://jsonplaceholder.typicode.com/todos?_limit=10')
    //   setTodos(res.data)
    // }
  
    useEffect(() => {
      axios
        .get('http://127.0.0.1:5000/sons/full_brothers')
        .then(res => setFullBrothers(res.data.result));
    },[]); 

    let fulldata = fullBrothers.map(element =>{
        return(
        <div>
            Mother: {element._id}
            <br/>
            Total: {element.count}
            <br/>
            Sons: {element.records.map(son => <ul>{son}</ul>)}
        </div>
        )
    })


    if(fullBrothers.length > 0) {
        return (
            <div>
                {console.log(fullBrothers[0])}
                {fulldata}
            </div>
        )
    }
    else {
        return (
            <div>
            </div>
        )  
    }
}

export default FullBrothers
