import React from 'react';

import GrammarContainer from '../components/GrammarContainer';
import ClickableImages from '../components/ClickableImages';

function GrammarTask(props) {
	return (
		<React.Fragment> 
        	<ClickableImages images={props.images} clickable={false}/>
        	<GrammarContainer grammar={props.grammar} options={props.options}/>
        </React.Fragment> 
	)
}

export default GrammarTask;