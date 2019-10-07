import React from 'react';
import Image from 'react-bootstrap/Image';

type State = {
  isSelected: boolean,
};

export default class ClickableImage extends React.Component<*, State>{
	render(){
		return (
			<div className={this.props.selected ? ' image selected-class': 'image'} onClick={this.props.clickable ? this.props.onClick : null} >
				<Image src= {this.props.image} alt='icon' />
			</div> 
		)
	}
}