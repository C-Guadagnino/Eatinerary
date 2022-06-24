import React from 'react';

class ReviewDetails extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div>
                <div className="col-md-6 m-5" id="mySkeweredList">
                    <p id="skeweredHeading">{this.props.title}</p>
                    <table className="table table-hover">
                        <thead>
                            <tr>
                                <th>Rating</th>
                                <th>Description</th>
                                <th>Eatery</th>
                                <th>Image</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>{this.props.rating}</td>
                                <td>{this.props.description}</td>
                                <td>{this.props.eatery}</td>
                                <td>
                                    {this.props.images.map(image => {
                                        return (
                                            <img src={image.image_url} key={image.id} height="150"></img>
                                        )
                                    })}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
}

export default ReviewDetails;
