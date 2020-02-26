import React, {useState, useEffect} from 'react'
import axios from 'axios'
import PeopleCard from './PeopleCard'
import {Carousel, Col, Row} from 'react-bootstrap'


function FullBrothers() {
    const [fullBrothers, setFullBrothers] = useState(
        []
    )
    
    useEffect(() => {
      axios
        .get('http://127.0.0.1:5000/sons/full_brothers')
        .then(res => setFullBrothers(res.data.result));
    },[]); 

    let fulldata = fullBrothers.map(element =>{
        return(
        <div style={{border:"1px solid", margin:"2em"}}>
            Mother: {element._id}
            <br/>
            Total: {element.count}
            <br/>
            Sons: 
            <Row>
                    {element.records.map(son => { 
                        return(
                            <Col sm="3" style={{padding:'0.5em'}}> 
                                {son} 
                            </Col> 
                        )
                    })}
            </Row>
        </div>    
        )
    })

{/* 
peopleCards = sortedOldToYoung.map(person => {
            return (
            <Col sm="3" stlye={{padding:'0.5em'}} key={person.name}>
                <PeopleCard key={person.name} prince={person} id={setid} filter={setFilter} x={data.sortFilter}/>
            </Col>
            )
        }) */}

    let x = (
        <Carousel>
  <Carousel.Item>
    <img
      className="d-block w-100"
      src="holder.js/800x400?text=First slide&bg=373940"
      alt="First slide"
    />
    <Carousel.Caption>
      <h3>First slide label</h3>
      <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img
      className="d-block w-100"
      src="holder.js/800x400?text=Second slide&bg=282c34"
      alt="Third slide"
    />

    <Carousel.Caption>
      <h3>Second slide label</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img
      className="d-block w-100"
      src="holder.js/800x400?text=Third slide&bg=20232a"
      alt="Third slide"
    />

    <Carousel.Caption>
      <h3>Third slide label</h3>
      <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
    </Carousel.Caption>
  </Carousel.Item>
</Carousel>
    )



    
    


    if(fullBrothers.length > 0) {
        return (
            <div>
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
