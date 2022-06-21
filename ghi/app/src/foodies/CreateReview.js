import React from 'react';
import {Link} from 'react-router-dom';
//import './Foodies.css';

class CreateReview extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "skeweredEateries": [],
            "reviewTitle": '',
            "reviewRating": '',
            "reviewDescription": '',
        };
        this.handleTitleChange = this.handleTitleChange.bind(this);
        this.handleRatingChange = this.handleRatingChange.bind(this);
        this.handleDescriptionChange = this.handleDescriptionChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async handleSubmit(event){
        event.preventDefault();
        const data = {...this.state };

        data.title = data.reviewTitle;
        delete data.reviewTitle;

        data.rating = data.reviewRating;
        delete data.reviewRating;

        data.description = data.reviewDescription;
        delete data.reviewDescription;

        const reviewUrl = 'http://localhost:8100/api/foodies/eateries/reviews/';
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-type': 'application/json',
            },
        };

        const reviewPostResponse = await fetch(reviewUrl, fetchConfig);
        if(reviewPostResponse.ok){
            const newReview = await reviewPostResponse.json();
            console.log("newReview is: ",newReview);
        
            const cleared = {
                reviewTitle: '',
                reviewRating: '',
                reviewDescription: '',
            };
            this.setState(cleared);
        }
    }

    handleTitleChange(event) {
        const titleValue = event.target.value;
        this.setState({ reviewTitle: titleValue });
    }

    handleRatingChange(event) {
        const ratingValue = event.target.value;
        this.setState({ reviewRating: ratingValue });
    }

    handleDescriptionChange(event) {
        const descriptionValue = event.target.value;
        this.setState({ reviewDescription: descriptionValue });
    }






    async componentDidMount() {
        //list all skewered eateries endpoint
        const skeweredEateriesUrl = 'http://localhost:8100/api/foodies/eateries/skewered/';
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
                                    <input onChange={this.handleTitleChange} value={this.state.reviewTitle} placeholder="Title" required type="text" name="reviewTitle" id="reviewTitle" className="form-control" />
                                    <label htmlFor="reviewTitle">Title</label>
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleRatingChange} value={this.state.reviewRating} placeholder="Review Rating" required type="text" name="reviewRating" id="reviewRating" className="form-control" />
                                    <label htmlFor="reviewRating">Rating</label>
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleDescriptionChange} value={this.state.reviewDescription} placeholder="Review Description" required type="text" name="reviewDescription" id="reviewDescription" className="form-control" />
                                    <label htmlFor="reviewDescription">Description</label>
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