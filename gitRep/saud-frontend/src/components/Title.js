import React from 'react'

function Header() {
    return (
        <React.Fragment>
        <header style={headerStyle}>
            <h1 style={h1style}>Saudi Arabia’s Royal Family</h1>
            <h2 style={h2Style}> For more than eight decades since the founding of the modern kingdom of Saudi Arabia in 1932, the title of king has passed along a line of brothers born to the first king, Abdulaziz ibn Saud.</h2>
            <hr style={hrStyle}/>
        </header>
        <div style={byLineStyle}>
            By Usman Haidar
        </div>
        </React.Fragment>
    )
}

const h1style = {
    fontWeight: '300',
    fontSize: '55px',
    fontFamily: ["Chronicle Display","Times Roman","Times New Roman"]
}

const h2Style = {
    fontFamily: ["Whitney SSm","sans-serif","Helvetica Neue","Helvetica","Arial"],
    fontStyle: 'normal',
    fontSize: '22px',
    lineHeight: '32px',
    letterSpacing: '-.5px',
    color: '#666',
    fontWeight: '300',
    marginTop: '0',
    textTransform: 'none'
}

const headerStyle = {
    color: '#333',
    textAlign: 'center',
    padding: '10px'

}

const hrStyle = {
    height: '2px',
    width: '55px',
    display: 'block',
    margin: '20px auto 15px',
    paddingTop: '0',
    backgroundColor: '#555',
    border: '0'
}

const byLineStyle = {
    color: '#666',
    clear: 'both',
    fontFamily: ["Chronicle SSm","Times Roman","Times New Roman"],
    fontStyle: 'italic',
    fontWeight: '300',
    lineHeight: '24px'
}

export default Header
