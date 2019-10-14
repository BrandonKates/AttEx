import React from 'react';
import Image from 'react-bootstrap/Image';

type State = {
  isSelected: boolean,
};
export default class ClickableImage extends React.Component<*, State>{
	render(){
		if(this.props.image){
			var { image } = this.props;
		}
		return (
			<div className={this.props.selected ? ' image selected-class': 'image'} onClick={this.props.clickable ? this.props.onClick : null} >
				{image && <Image src= {`data:image/jpeg;base64,${image}`} alt='icon' />}
			</div> 
		)
	}
}