import React from 'react'

function Description(props) {

    let element = props.data.find((element) => { 
        if (props.id === 'Turki I'){
            return element.name.includes('Turki I bin Abdulaziz Al Saud')
        }
        return element.name.replace("Al Saud", "").includes(props.id)
    }); 

    // console.log(element)
    return (
        <div>
            {/* {props.id}      */}
            Name: {element.name}
            <br/>
            Mother: {element.mother}
            <br/>
            Born: {element.born}
            <br/>
            Description: {element.description}
            <br/>
            Sons: {element.sons.map(txt => <p>{txt}</p>)}
        </div>
    )

}

export default Description
