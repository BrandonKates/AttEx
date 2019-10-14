import React from 'react';
import ClickableImage from './ClickableImage';

type State = {
  selected: string,
};

export default class ClickableImages extends React.Component<*, State> {
	constructor(props){
		super(props);
		this.options = props.options;
		this.state = {
			selected: 'null',
		};
		this.handleClick = this.handleClick.bind(this);
	}
	handleClick(id){
		this.setState(() => ({ selected: id}))
		this.props.onChange(id)
	}

	render() {
		const { selected } = this.state;
		var images = this.props.images;
		if(images){
			if(images.hasOwnProperty("image")){
				images = [images]
			}
		}

		return (
        	<div id="image-container">
        		{images && images.map(function(image, i){
					var id = 'image' + i
					return (
						<ClickableImage 
						id={id}
						{...image} 
						selected={selected === id} 
						onClick={() => this.handleClick(id)}
						clickable={this.props.clickable} 
						key={i} />);
        		},this)}

			</div>
		);
	}
}