import React from 'react'

function Description(props) {

    let element = props.data.find((element) => { 
        if (props.id === 'Turki I'){
            return element.name.includes('Turki I bin Abdulaziz Al Saud')
        }
        return element.name.replace("Al Saud", "").includes(props.id)
    }); 
    const borderStyle = {
        border: '1px solid', paddingLeft: '20px', paddingRight: '20px', paddingTop: '10px',
        height: '250px',
        overflowY: 'scroll',
        position: 'sticky',
        top:'10px'
    }

    return (
        <div style={borderStyle}>
            <b>Name</b>: {element.name}
            <br/>
            <b>Mother</b>: {element.mother}
            <br/>
            <b>Born</b>: {element.born}
            <br/>
            <b>Description</b>: {element.description}
            <br/>
            <b>Sons</b>: {element.sons.map(txt => <p>{txt}</p>)}
        </div>
    )

}

export default Description
