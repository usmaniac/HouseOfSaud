import React, { useState, useEffect } from 'react'
import axios from 'axios'
import {  Row, Col, Container, } from 'react-bootstrap';
import PeopleCard from './PeopleCard'
import Description from './Description';
import SortAndFilter from './SortAndFilter';
import FullBrothers from './FullBrothers'

function Data() {

    const [data, setData] = useState({
        values:[],
        id: "Nayef",
        sortFilter:"young_first",
    })

    // NEED TO USE STATE
    // resolveData()
    useEffect(() => {
       resolveData()
      },[]); 
    
    async function resolveData () {
        let data = await axios.get('http://127.0.0.1:5000/sons/all')
        let x = await Promise.resolve(data)
        let results = await x['data']['result']
        setData({
            values:results,
            id: "Nayef",
            sortFilter: "old_first"
        })
        
    }

    const gridStyle = {
        gridTemplateColumns: "repeat(4, 1fr)",
        gridAutoRows: "1fr",
        gridColumnGap: "30px",
        gridRowGap: "30px"
    }

    const setid = (id,filter) => {
        setData({
                values: data.values,    // keep all other key-value pairs
                id: id,      // update the value of specific key
                sortFilter:filter
        })
    }

    const setFilter = (filter) => {
        setData({
            values: data.values,  
            id: data.id,      
            sortFilter:filter
        })
    }

    let peopleCards
    if (data.sortFilter === "old_first"){
        let sortedOldToYoung = data.values.sort((a, b) => {
            return a.born-b.born
        })

        peopleCards = sortedOldToYoung.map(person => {
            return (
            <Col sm="3" stlye={{padding:'0.5em'}} key={person.name}>
                <PeopleCard key={person.name} prince={person} id={setid} filter={setFilter} x={data.sortFilter}/>
            </Col>
            )
        })
    }

    else if (data.sortFilter === "young_first"){
        let sortedOldToYoung = data.values.sort((a, b) => {
            return b.born-a.born
        })

        peopleCards = sortedOldToYoung.map(person => {
            return (
            <Col sm="3" stlye={{padding:'0.5em'}} key={person.name}>
                <PeopleCard key={person.name} prince={person} id={setid} filter={setFilter}  x={data.sortFilter}/>
            </Col>
            )
        })
    }
    else if (data.sortFilter === "kings"){
        let kings =  data.values.filter(prince => {
            return prince.king === true
        });

        peopleCards = kings.map(person => {
            return (
            <Col sm="3" stlye={{padding:'0.5em'}} key={person.name}>
                <PeopleCard key={person.name} prince={person} id={setid} filter={setFilter}  x={data.sortFilter}/>
            </Col>
            )
        })
    }
    else if (data.sortFilter === "alive"){
        let kings =  data.values.filter(prince => {
            return prince.deceased === false
        });

        peopleCards = kings.map(person => {
            return (
            <Col sm="3" stlye={{padding:'0.5em'}} key={person.name}>
                <PeopleCard key={person.name} prince={person} id={setid} filter={setFilter}  x={data.sortFilter}/>
            </Col>
            )
        })
    }

    else if (data.sortFilter === "full_brothers"){
        return (
            <React.Fragment>
                <Row>
                    <SortAndFilter setFilter={setFilter}/>
                    {console.log(data.sortFilter)}
                </Row>
                    <p> King Abdul Aziz had up to 22 wives with estimates of around 100 children. 
                    Despite having the same father, the sons with a common mother were naturally much closer
                    to one another. This would play out politically in the following generations as power blocs
                    were formed amongst full brothers. The most powerful of this bloc was the Sudairi Seven; 7 full brothers 
                    born to King Abdul-Aziz and his wife Hassa Al Sudairi. 
                </p>  
                <FullBrothers/>
            </React.Fragment>
        )
          
    }

    else{
        peopleCards = data.values.map(person => {
            return (
            <Col sm="3" stlye={{padding:'0.5em'}} key={person.name}>
                <PeopleCard key={person.name} prince={person} id={setid} filter={setFilter}  x={data.sortFilter}/>
            </Col>
            )
        })
    }


    if(data.values.length > 0) {
        return (
            <div>
            <Row>
                <SortAndFilter setFilter={setFilter}/>
                {console.log(data.sortFilter)}
                {console.log("id:",data.id)}
            </Row>
            <Row>
                <Col sm="6">
                    
                    <Container fluid  style={{alignContent:'space-between'}}>
                        <Row style={gridStyle}>
                            {peopleCards}
                        </Row>
                    </Container>
                </Col>
                <Col sm="6">
                <Description data={data.values} id={data.id} />
                </Col>
            </Row>
            
            </div>
        )
    }
    else{
        console.log("i am not sending data")
        return (
            <div>        
            </div>
        )
    }
}


export default Data
