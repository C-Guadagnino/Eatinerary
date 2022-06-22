import React from 'react';
import {Link} from 'react-router-dom';
import './Foodies.css';
import ReviewDetails from "./ReviewDetails";

class ShowReview extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "reviews": [],
        };
        this.selectReview = this.selectReview.bind(this);
    }
    async componentDidMount() {
        //list all reviews endpoint
        const reviewsUrl = 'http://localhost:8100/api/foodies/eateries/reviews/';
        const reviewsResponse = await fetch(reviewsUrl);

        if(reviewsResponse.ok){
            const reviewsData = await reviewsResponse.json();
            console.log(reviewsData);

            this.setState({reviews: reviewsData.reviews})
        }
    }

    selectReview(review) {
        console.log("is this selectReview:", review);
        this.setState({
            "selected": review,
        })
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
                                    <Link to="/mySkewered">My Skewered List</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/mySkeweredHistory">My Skewered History</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/review">Leave a Review</Link>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div className="col-md-3" id="reviewsList">
                        <div className="list-group" id="reviewsList2">
                                        {this.state.reviews.map(review => {
                                                return (
                                                    <button onClick={() => this.selectReview(review)} key={review.skewered_eatery.id} type="button" className="list-group-item list-group-item-action" id="reviewbuttons">{review.skewered_eatery.eatery.eatery_name}</button>
                                                )
                                        })}
                        </div>
                    </div>

                    <div className="row p-3">
                        <div className="col-md-6" id="skeweredMaps">
                            { this.state.selected?
                                <ReviewDetails title={this.state.selected.title} rating={this.state.selected.rating} description={this.state.selected.description} eatery={this.state.selected.skewered_eatery.eatery.eatery_name} images={this.state.selected.review_images}/>
                                 :null}
                        </div>
                    </div>
                </div>
            </>
        );
    }
}

export default ShowReview;