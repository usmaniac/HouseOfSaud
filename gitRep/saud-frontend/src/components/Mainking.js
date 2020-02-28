import React from 'react'
import { Card, Button, Popover, OverlayTrigger } from 'react-bootstrap'


function Mainking() {

    let img = require(`../princeFolder/ibnsaud.jpg`)
    let name = 'ibnsaud'
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

    const popover = (
        <Popover id="popover-basic">
          <Popover.Title as="h3">Abdul Aziz Ibn Saud</Popover.Title>
          <Popover.Content>
            First monarch and founder of Saudi Arabia. 
            Scroll Below for a more detailed view of all 36 of his sons.
            Utlilise the filters for further insight.
          </Popover.Content>
        </Popover>
      );
    


    return (
        <OverlayTrigger trigger="click" placement="right" overlay={popover}>
        <Button key={name} 
        variant="light" style={{width:"20%"}}   
        >
            <div style={{width:"100%", height:"100%"}}>
            <Card style={cardStyle}>
            <Card.Img top width="100%" src ={img} alt="House of Saud"  style={{height:"80%"}}/>
                <Card.Title style={textStyle}>{'Abdul Aziz Ibn Saud'}</Card.Title>
            </Card>
            </div>
        </Button>
        </OverlayTrigger>
    )
}

export default Mainking
