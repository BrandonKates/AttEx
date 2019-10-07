import { combineReducers } from 'redux'
// redux-undo higher-order reducer

import state from './state';

export default combineReducers({
  state: state,
})
