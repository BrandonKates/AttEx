//import Async, { makeAsyncSelect } from 'react-select/async';
import React, { Component, Fragment } from 'react';

import Select from 'react-select';

type State = {
  isClearable: boolean,
  isDisabled: boolean,
  isLoading: boolean,
  isRtl: boolean,
  isSearchable: boolean,
};

export default class SelectList extends Component<*, State> {
	constructor(props){
		super(props);
		this.options = props.options;
	}
  state = {
    isClearable: false,
    isDisabled: false,
    isLoading: false,
    isSearchable: true,
  };

  toggleClearable = () =>
    this.setState(state => ({ isClearable: !state.isClearable }));
  toggleDisabled = () =>
    this.setState(state => ({ isDisabled: !state.isDisabled }));
  toggleLoading = () =>
    this.setState(state => ({ isLoading: !state.isLoading }));
  toggleRtl = () => this.setState(state => ({ isRtl: !state.isRtl }));
  toggleSearchable = () =>
    this.setState(state => ({ isSearchable: !state.isSearchable }));
  render() {
    const {
      isClearable,
      isSearchable,
      isDisabled,
      isLoading,
    } = this.state;
    return (
      <Fragment>
        <Select
          className="selectList"
          classNamePrefix="select"
          defaultValue={this.options[0]}
          isDisabled={isDisabled}
          isLoading={isLoading}
          isClearable={isClearable}
          isSearchable={isSearchable}
          name="color"
          options={this.options}
        />
      </Fragment>
    );
  }
}