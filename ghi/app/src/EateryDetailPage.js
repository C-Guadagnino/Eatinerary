import React from 'react';

class EateryDetailPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      eateryData: {}

    };
  }

  async componentDidMount() {
    const eateryUrl = 'http://localhost:8090/api/eateries/1/';
    const eateryResponse = await fetch(eateryUrl);

    if (eateryResponse.ok) {
      const eateryData = await eateryResponse.json();
      this.setState({ eateryData: eateryData });
      console.log("eateryData", eateryData)
    }
  }

  render() {
    let categories_html = ''
    if (this.state.eateryData.categories) {
      categories_html = this.state.eateryData.categories.map(category => {
        // console.log(category.title)
        return (
          <li>{category.title}</li>
        )
      })
    }

    let tags_html = ''
    if (this.state.eateryData.tags) {
      tags_html = this.state.eateryData.tags.map(tag => {
        // console.log(tag.tag_name)
        return (
          <li>{tag.tag_name}</li>
        )
      })
    }

    let address_line1 = ''
    let address_line2 = ''
    if (this.state.eateryData.location) {
      address_line1 = <p>
        {this.state.eateryData.location.address1} {this.state.eateryData.location.address2} {this.state.eateryData.location.address3}
      </p>
      address_line2 = <p>
        {this.state.eateryData.location.city}, {this.state.eateryData.location.state} {this.state.eateryData.location.zip_code}
      </p>
    }

    let openhours_html = ''
    if (this.state.eateryData.open_hours) {
      openhours_html = this.state.eateryData.open_hours.map(openhours => {
        return (
          <tr>
            <td>{openhours.weekday}</td>
            <td>{openhours.start_time}</td>
            <td>{openhours.end_time}</td>
          </tr>
        )
      })
    }

    return (
      <div className="container">


        <h1>{this.state.eateryData.eatery_name}</h1>
        <p>{this.state.eateryData.average_rating} Stars, {this.state.eateryData.review_count} reviews</p>
        <p>{this.state.eateryData.price}</p>

        <p>Categories</p>
        <ul>
          {categories_html}
        </ul>

        <p>Tags</p>
        <ul>
          {tags_html}
        </ul>

        <p>Address</p>
        {address_line1}
        {address_line2}

        <table>
          {openhours_html}
        </table>



      </div>
    );
  }
}

export default EateryDetailPage;