import React from 'react';
import {Link} from 'react-router-dom';
//import './Foodies.css';

class CreateReview extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "skeweredEateries": [],
        };
        //this.handleSkeweredList = this.handleSkeweredListChange.bind(this);
    }

    async componentDidMount() {
        //list all skewered eateries endpoint
        const skeweredEateriesUrl = 'http://localhost:8100/api/skewered/';
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if(skeweredEateriesResponse.ok){
            const skeweredEateriesData = await skeweredEateriesResponse.json();

            this.setState({skeweredEateries: skeweredEateriesData.skewered_eateries})
        }
    }

    render() {
        return (
            <>
                <div className="container">
                    <h1 id="reviewsheader">Reviews</h1>
                    <div className="row p-3">

                        <div className="col-md-6" id="sideNav">
                            <ul className="list-group list-group-flush">
                                <li className="list-group-item">
                                    <Link to="/skewered">My Skewered List</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/history">My Skewered History</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/review">Reviews</Link>
                                </li>
                            </ul>
                        </div>
                    </div>
                   
                <div className="col-md-3" id="reviews">
                    
                    <div className="list-group">
                                    {this.state.skeweredEateries.map(skeweredEatery => {
                                            return (
                                                <button key={skeweredEatery.id} type="button" className="list-group-item list-group-item-action" id="reviewbuttons">{skeweredEatery.eatery.eatery_name}</button>
                                            )
                                    })}
                            </div>
                        </div>

                    <div className="col-md-3" id="reviewForm">
                        <p>I am a column for the create/show review form</p>

                        <div className="shadow p-4 mt-4">
                            <h1>Leave a Review</h1>
                            <form onSubmit={this.handleSubmit} id="create-review-form">
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleCustomerNameChange} value={this.state.customerName} placeholder="Customer Name" required type="text" name="customerName" id="customerName" className="form-control" />
                                    <label htmlFor="customerName">Eatery Name</label>
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleCustomerAddressChange} value={this.state.customerAddress} placeholder="Customer Address" required type="text" name="customerAddress" id="customerAddress" className="form-control" />
                                    <label htmlFor="customerAddress">Rating</label>
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleCustomerPhoneChange} value={this.state.customerPhone} placeholder="Customer Phone Number" required type="text" name="customerPhone" id="customerPhone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" className="form-control" />
                                    <label htmlFor="customerPhone">Description</label>
                                </div>
                                <button className="btn btn-primary">Submit Review</button>
                            </form>
                            </div>

                    </div>
                </div>
            </>
        );
    }
}

export default CreateReview;