import React from 'react';
import { Link } from 'react-router-dom';

class CreateReview extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "title": '',
            "rating": '',
            "description": '',
            "skeweredEatery": '',
            "skeweredEateriesWithoutReview": [],
            "reviewImage": '',
        };
        this.handleTitleChange = this.handleTitleChange.bind(this);
        this.handleRatingChange = this.handleRatingChange.bind(this);
        this.handleDescriptionChange = this.handleDescriptionChange.bind(this);
        this.handleSkeweredEateryChange = this.handleSkeweredEateryChange.bind(this);
        this.handleReviewImageChange = this.handleReviewImageChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async componentDidMount() {
        this.getFoodieData()
    }

    componentDidUpdate(prevProps) {
        // if old username is not the same as the current username
        if (prevProps.username !== this.props.username) {
            this.getFoodieData()
        }
    }

    async getFoodieData() {

        const foodie_username = this.props.username

        if (!foodie_username) {
            return
        }
        // list all skewered eateries endpoint
        const skeweredEateriesUrl = `${process.env.REACT_APP_FOODIES_API}/api/foodies/user/${foodie_username}/eateries/skewered/`;
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if (skeweredEateriesResponse.ok) {
            const skeweredEateriesData = await skeweredEateriesResponse.json();
            const skeweredEateriesList = skeweredEateriesData.skewered_eateries;

            const reviewsUrl = `${process.env.REACT_APP_FOODIES_API}/api/foodies/${foodie_username}/eateries/reviews/`;
            const reviewsResponse = await fetch(reviewsUrl);
            if (reviewsResponse.ok) {
                const reviewsData = await reviewsResponse.json();
                const reviewsList = reviewsData.reviews;
                const eateriesWithoutReview = []

                for (const skeweredEatery of skeweredEateriesList) {
                    let eateryHasReview = false
                    for (const review of reviewsList) {
                        if (review.skewered_eatery.id === skeweredEatery.id) {
                            eateryHasReview = true
                        }
                    }
                    if (!eateryHasReview) {
                        eateriesWithoutReview.push(skeweredEatery)
                    }
                }
                this.setState({ skeweredEateriesWithoutReview: eateriesWithoutReview })
            }

        }
    }

    async handleSubmit(event) {
        event.preventDefault();

        const data = { ...this.state };
        data.skewered_eatery = data.skeweredEatery;
        delete data.skeweredEatery;
        delete data.skeweredEateriesWithoutReview;

        const dataForReviewImage = {};
        dataForReviewImage.image_url = data.reviewImage;
        delete data.reviewImage;

        // POST url for foodie creates a review
        const reviewUrl = `${process.env.REACT_APP_FOODIES_API}/api/foodies/eateries/reviews/`;
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-type': 'application/json',
            },
        };
        const response = await fetch(reviewUrl, fetchConfig);
        let newReview;
        if (response.ok) {
            newReview = await response.json();
            // The below handles the creation of a review image object and relates it to the
            // review object just created if an image url was provided
            if (this.state.reviewImage) {
                dataForReviewImage.review = newReview.id;
                const reviewImageUrl = `${process.env.REACT_APP_FOODIES_API}/api/foodies/eateries/reviews/images/`;
                const imageFetchConfig = {
                    method: "post",
                    body: JSON.stringify(dataForReviewImage),
                    headers: {
                        'Content-type': 'application/json',
                    },
                };
                const imageResponse = await fetch(reviewImageUrl, imageFetchConfig);
                if (imageResponse.ok) {
                    await imageResponse.json();
                }
            }
            const cleared = {
                title: '',
                rating: '',
                description: '',
                reviewImage: '',
            };
            this.setState(cleared);
            this.getFoodieData()
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

    render() {
        return (
            <>
                <div className="row mt-5 py-5">
                    <div className="col-md-4" id="sideNav">
                        <ul className="list-group list-group-flush">
                            <li className="list-nav-item">
                                <Link className='link' to="/myskewered">My Skewered List</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/myskeweredhistory">My Skewered History</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/showreview">My Reviews</Link>
                            </li>
                        </ul>
                    </div>


                    <div className="col-md-4 mx-3 mt-5" id="reviewForm">
                        <h1>Leave a Review</h1>
                        <form onSubmit={this.handleSubmit} id="create-review-form">
                            <div className="mb-3">
                                <select onChange={this.handleSkeweredEateryChange} value={this.state.skeweredEatery} required name="skewered_eatery" id="skewered_eatery" className="form-select">
                                    <option value="">Choose a Skewered Eatery</option>
                                    {this.state.skeweredEateriesWithoutReview.map(skeweredEatery => {
                                        return (
                                            <option key={skeweredEatery.id} value={skeweredEatery.id}>{skeweredEatery.eatery.eatery_name}</option>
                                        );
                                    })}
                                </select>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleTitleChange} value={this.state.title} placeholder="title" required type="text" name="title" id="title" className="form-control" />
                                <label htmlFor="title">Title</label>
                            </div>
                            <div className="mb-3">
                                <select onChange={this.handleRatingChange} value={this.state.rating} required name="rating" id="rating" className="form-select">
                                    <option value="">Choose a Rating</option>
                                    <option key={1} value={1}>{1}</option>
                                    <option key={2} value={2}>{2}</option>
                                    <option key={3} value={3}>{3}</option>
                                    <option key={4} value={4}>{4}</option>
                                    <option key={5} value={5}>{5}</option>
                                </select>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleDescriptionChange} value={this.state.description} placeholder="description" required type="text" name="description" id="description" className="form-control" />
                                <label htmlFor="description">Description</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleReviewImageChange} value={this.state.reviewImage} placeholder="review_image" type="text" name="review_image" id="review_image" className="form-control" />
                                <label htmlFor="reviewImage">Review Image URL</label>
                            </div>
                            <button className="button-38" id="submitReviewBtn">Submit Review</button>
                        </form>
                    </div>
                </div>
            </>
        );
    }
}

export default CreateReview;
