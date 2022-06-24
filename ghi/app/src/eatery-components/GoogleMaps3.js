import React, { Component } from 'react';
import Iframe from 'react-iframe';


class GoogleMaps extends React.Component {
    constructor(props){
        super(props);
    }
    render(){
        return(
            

            <div>
                <Iframe url={`https://www.google.com/maps/embed/v1/place?key=AIzaSyAu_o8QZpXb6L161cw5FJS6v3g4k2VlZlE&q=${this.props.name}+${this.props.city}+${this.props.state}&center=${this.props.latitude},${this.props.longitude}`}
                        width="900px"
                        height="450px"
                        id="myId"
                        className="myClassname"
                        display="block"
                        position="relative"
                        
                        />
            </div>


            
        );
    }
}

export default GoogleMaps;
