import React from 'react';
import { Link } from 'react-router-dom';
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
        this.getReviewData()
    }

    componentDidUpdate(prevProps) {
        // if old username is not the same as the current username
        if (prevProps.username !== this.props.username) {
            this.getReviewData()
        }
    }

    async getReviewData() {
        const foodie_username = this.props.username

        if (!foodie_username) {
            return
        }

        //list all reviews for a foodie endpoint
        const reviewsUrl = `http://localhost:8100/api/foodies/${foodie_username}/eateries/reviews/`;
        const reviewsResponse = await fetch(reviewsUrl);

        if (reviewsResponse.ok) {
            const reviewsData = await reviewsResponse.json();
            //console.log(reviewsData);

            this.setState({ reviews: reviewsData.reviews })
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
                <div className="row mt-5 py-5">
                    <div className="col-md-6" id="sideNav">
                        <ul className="list-group list-group-flush">
                            <li className="list-nav-item">
                                <Link className='link' to="/mySkewered">My Skewered List</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/mySkeweredHistory">My Skewered History</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/review">Leave a Review</Link>
                            </li>
                        </ul>
                    </div>
                    <div className="col-md-3 mt-5" id="reviewsList">
                        <h2> Reviews </h2>
                        <div className="list-group" id="reviewsList2">
                            {this.state.reviews.map(review => {
                                return (
                                    <button onClick={() => this.selectReview(review)} key={review.skewered_eatery.id} type="button" className="button-38" id="reviewbuttons">{review.skewered_eatery.eatery.eatery_name}</button>
                                )
                            })}
                        </div>
                    </div>
                </div>
                <div className="row p-3">
                    <div className="col-md-6" id="skeweredMaps">
                        {this.state.selected ?
                            <ReviewDetails title={this.state.selected.title} rating={this.state.selected.rating} description={this.state.selected.description} eatery={this.state.selected.skewered_eatery.eatery.eatery_name} images={this.state.selected.review_images} />
                            : null}
                    </div>
                </div>
            </>
        );
    }
}

export default ShowReview;