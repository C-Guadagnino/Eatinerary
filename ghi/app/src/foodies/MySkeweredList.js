import React from 'react';
import {Link} from 'react-router-dom';
import './Foodies.css';

class SkeweredList extends React.Component {
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
            <div id="mapPlaceholder">
                <p>I am a placeholder for google maps </p>
            </div>

            <div className="card">
                <ul className="list-group list-group-flush">
                    <li className="list-group-item">
                        <Link to="/myPastSkewered">My Past Skewered</Link>
                    </li>
                    <li className="list-group-item">
                        <Link to="/Reviews">Reviews</Link>
                    </li>
                </ul>
            </div>

            <div className="mySkeweredList">
                <h1>My Skewered List</h1>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Eatery Name</th>
                            <th>Price</th>
                            <th>Average Rating</th>
                            <th> </th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.skeweredEateries.map(skeweredEatery => {
                            return (
                                <tr key={skeweredEatery.id}>
                                    <td>{skeweredEatery.eatery_vo.eatery_name}</td>
                                    <td>{skeweredEatery.eatery_vo.price}</td>
                                    <td>{skeweredEatery.eatery_vo.average_rating}</td>
                                </tr>
                            )
                        })}
                    </tbody>
                </table>
            </div>
            </>
        );
    }
}

export default SkeweredList;


