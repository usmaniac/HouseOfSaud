import React,{useState} from 'react'
import {DropdownButton, Dropdown} from 'react-bootstrap'

function SortAndFilter(props) {
    const [filter, setFilter] = useState("old_first")

    const handleSelect = (filter,evtKey) => {
        props.setFilter(filter)
    }

    return (
        <div style={{marginLeft:'2em', marginBottom:'2em'}}>
            <DropdownButton id="dropdown-basic-button" title="Filters" onSelect={handleSelect}>
                <Dropdown.Item eventKey="old_first">Sort By Age: Old to Young</Dropdown.Item>
                <Dropdown.Item eventKey="young_first">Sort By Age: Young to Old</Dropdown.Item>
                <Dropdown.Item eventKey="full_brothers">Full Brothers</Dropdown.Item>
                <Dropdown.Item eventKey="alive">Alive</Dropdown.Item>
                <Dropdown.Item eventKey="kings">Kings</Dropdown.Item>
            </DropdownButton>
        </div>
    )
}

export default SortAndFilter
