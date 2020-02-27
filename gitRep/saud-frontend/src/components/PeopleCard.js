import React, { useState, useEffect } from 'react'
import { Card, Button } from 'react-bootstrap'

// function to display the images of the family members in card form

function PeopleCard(props) {
    const [activeid, setActive] = useState({
        name:"Nayef",
        filter:"old_first"
    })



    const {name} = props.prince
    
    
    let personList = name 
    let regexpNames =  /(.*)bin/mgi
    let match = personList.match(regexpNames)
    let slicedName = match[0].slice(0, match[0].length-3)
    slicedName = slicedName.trim()
    let img = ""
    try{
        img = require(`../princeFolder/${slicedName}.jpg`)
    }
    catch(err) {
        img = require(`../princeFolder/saudi.jpg`)
    }


    const cardStyle = {
        height: "100%",
        width: '100%',
        position: "relative",
        flexDirection: 'column',
        minWidth: 0,
        wordWrap: "break-word",
        border: "1px solid rgba(0,0,0,.125)",
        borderRadius: ".25rem"
    }

    const textStyle = {
        marginTop: "-7px",
        paddingTop: "5px",
        fontSize: "10px",
        lineHeight: "15px",
        textAlign: "center",
        width: "100%",
        marginBottom: "5px",
        fontWeight: "600"
    }
    
    const handleClick = (id, event) => {
        setActive(id)
    }


    return (
        <Button key={slicedName} 
        className={ activeid.name === slicedName && 'is-active' }
        onClick={ ()=> {handleClick.bind(this, slicedName)(); props.id.bind(this,slicedName,props.x)(); }}
        // onClick={() => { func1(); func2();}}
        variant="light" style={{height:"80%"}}   
        >
            <div style={{width:"100%", height:"100%"}}>
            <Card style={cardStyle}>
            <Card.Img top width="100%" src ={img} alt="House of Saud"  style={{height:"80%"}}/>
                <Card.Title style={textStyle}>{slicedName}</Card.Title>
            </Card>
            </div>
        </Button>

    )

}

export default PeopleCard
