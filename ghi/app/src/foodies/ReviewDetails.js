import React, { Component } from 'react';

class ReviewDetails extends React.Component {
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div>


            title = {this.props.title}
            rating = {this.props.rating}
            description = {this.props.description}
            eatery = {this.props.eatery}
            {/* images = {this.props.images} */}
            {this.props.images.map(image => {
                return(
                    <img src={image.image_url} key={image.id} height="150"></img>
                    )
                })
            }
            </div>
        );
    }
}

export default ReviewDetails;