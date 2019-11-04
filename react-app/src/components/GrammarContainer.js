import React from 'react';
// import SelectList from './SelectList/SelectList';
import SelectForm from './SelectForm'


export default class GrammarContainer extends React.Component {
	constructor(props){
		super(props);
		this.state = {userclass:"panda ."}
		this.handleChange = this.handleChange.bind(this)
		this.grammar = this.processGrammar(props.grammar)
		this.options = props.options;
		

	}

	processGrammar(grammar){
		console.log(grammar)
		grammar = JSON.parse(grammar);
		var VAR = /^[A-Z]$/
		var COORD = /^\([0-9], [0-9]\)$/;
		
		var test = grammar['S'][4]
		var objectsToRender = test.map((item, key)=> {
			if(VAR.exec(item)!==null){
				//item is a variable
				if(item === "A") return <p key={key}>   </p>
				var listItem = grammar[item]
				// console.log(this.state)
				return (<SelectForm options={this.convertListToOptions(listItem)} key={key} handleChange = {this.handleChange} userclass = {this.state.userclass}></SelectForm>)
			}
			else if(COORD.exec(item)!==null){
				//item is a coordinate
				return <p key={key}> {item} </p>
			}
			else{
				// item is a string
				//if (["?", "!", "."].includes(item)){
			//		return <div> item </div>
		//		}
				return <p key={key}> {item} </p>
			}
			});
		//for(var key in grammar){
		//	if(grammar.hasOwnProperty(key)){
		//		grammar[key]
		//	}	
		//}
		return objectsToRender;
	}
	convertListToOptions(items){
		return items.map(item => {
			return {value: item, label: item};
		})
	}
	handleChange(event) {
	  this.setState({userclass: event.target.value});
	//   console.log(this.state)
	}


	render(){
		return (
			<div id='grammar-container'>
				{this.grammar}
			</div>
			
		)
	}
}
