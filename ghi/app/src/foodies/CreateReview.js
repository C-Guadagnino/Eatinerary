import React from 'react';
import {Link} from 'react-router-dom';
//import './Foodies.css';

class CreateReview extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "title": '',
            "rating": '',
            "description": '',
            "skeweredEatery": '',
            "skeweredEateries": [],
            "reviewImage": '',
        };
        this.handleTitleChange = this.handleTitleChange.bind(this);
        this.handleRatingChange = this.handleRatingChange.bind(this);
        this.handleDescriptionChange = this.handleDescriptionChange.bind(this);
        this.handleSkeweredEateryChange = this.handleSkeweredEateryChange.bind(this);
        this.handleReviewImageChange = this.handleReviewImageChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async handleSubmit(event){
        event.preventDefault();

        const data = {...this.state};

        data.skewered_eatery = data.skeweredEatery; 
        delete data.skeweredEatery;
        delete data.skeweredEateries;

        const dataForReviewImage = {};
        dataForReviewImage.image_url = data.reviewImage;
        delete data.reviewImage;

        //POST url for foodie creates a review
        const reviewUrl = 'http://localhost:8100/api/foodies/eateries/reviews/';
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-type': 'application/json',
            },
        };
        const response = await fetch(reviewUrl, fetchConfig);
        let newReview;
        if(response.ok){
            newReview = await response.json();
            console.log("newReview is: ",newReview);
        
            // const cleared = {
            //     title: '',
            //     rating: '',
            //     description: '',
            //     skeweredEateries: [],
            // };
            // this.setState(cleared);
        }

        dataForReviewImage.review = newReview.id;
        // //This will be for review images
        const reviewImageUrl = 'http://localhost:8100/api/foodies/eateries/reviews/images/';
        const imageFetchConfig = {
            method: "post",
            body: JSON.stringify(dataForReviewImage),
            headers: {
                'Content-type': 'application/json',
            },
        };
        const imageResponse = await fetch(reviewImageUrl, imageFetchConfig);

        if(imageResponse.ok){
            const newReviewImage = await imageResponse.json();
            console.log("newReviewImage is: ",newReviewImage);
        
            const cleared = {
                title: '',
                rating: '',
                description: '',
                skeweredEateries: [],
                reviewImage: '',
            };
            this.setState(cleared);
        }


    }

    handleTitleChange(event) {
        const value = event.target.value;
        this.setState({ title: value });
    }

    handleRatingChange(event) {
        const value = event.target.value;
        this.setState({ rating: value });
    }

    handleDescriptionChange(event) {
        const value = event.target.value;
        this.setState({ description: value });
    }

    handleSkeweredEateryChange(event) {
        const value = event.target.value;
        this.setState({ skeweredEatery: value });
    }

    handleReviewImageChange(event) {
        const value = event.target.value;
        this.setState({ reviewImage: value });
    }

    async componentDidMount() {
        //list all skewered eateries endpoint
        const skeweredEateriesUrl = 'http://localhost:8100/api/foodies/eateries/skewered/';
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if(skeweredEateriesResponse.ok){
            const skeweredEateriesData = await skeweredEateriesResponse.json();
            console.log(skeweredEateriesData);

            this.setState({skeweredEateries: skeweredEateriesData.skewered_eateries})
        }
    }

    render() {
        return (
            <>
                    <div className="row mt-5 py-5">

                        <div className="col-md-4" id="sideNav">
                            <ul className="list-group list-group-flush">
                                <li className="list-group-item">
                                    <Link to="/mySkewered">My Skewered List</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/mySkeweredHistory">My Skewered History</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/showreview">My Reviews</Link>
                                </li>
                            </ul>
                        </div>
                   
                    <div className="col-md-4" id="reviewForm">
                        <div className="p-4 mt-4" id="innerForm">
                            <h1>Leave a Review</h1>
                            <form onSubmit={this.handleSubmit} id="create-review-form">

                                <div className="form-floating mb-3">
                                    <input onChange={this.handleTitleChange} value={this.state.title} placeholder="title" required type="text" name="title" id="title" className="form-control" />
                                    <label htmlFor="title">Title</label>
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleRatingChange} value={this.state.rating} placeholder="rating" required type="text" name="rating" id="rating" className="form-control" />
                                    <label htmlFor="rating">Rating</label>
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleDescriptionChange} value={this.state.description} placeholder="description" required type="text" name="description" id="description" className="form-control" />
                                    <label htmlFor="description">Description</label>
                                </div>

                                <div className="mb-3">
                                    <select onChange={this.handleSkeweredEateryChange} value={this.state.skeweredEatery} required name="skewered_eatery" id="skewered_eatery" className="form-select">
                                        <option value="">Choose a Skewered Eatery</option>
                                        {this.state.skeweredEateries.map(skeweredEatery => {
                                            return (
                                                <option key={skeweredEatery.id} value={skeweredEatery.id}>{skeweredEatery.eatery.eatery_name}</option>
                                            );
                                        })}
                                    </select>
                                </div>
                                
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleReviewImageChange} value={this.state.reviewImage} placeholder="review_image" type="text" name="review_image" id="review_image" className="form-control" />
                                    <label htmlFor="reviewImage">Review Image</label>
                                </div>


                                <button className="button-39" id="submitReviewBtn">Submit Review</button>
                            </form>
                        </div>

                    </div>
                    </div>
            </>
        );
    }
}

export default CreateReview;