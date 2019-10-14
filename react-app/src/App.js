import React from 'react';
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import './App.css';

import Header from './components/Header';
import Footer from './components/Footer';

import RecognitionTask from './pages/RecognitionTask';
import GrammarTask from './pages/GrammarTask';
import ClickPointTask from './pages/ClickPointTask';
import ChooseImageTask from './pages/ChooseImageTask';


const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' },
];

function App() {
  return (
    <div id="app">
      <Header/>
        <div id='page_wrap'>
          <Switch>
            {/* If the current URL is /about, this route is rendered
                while the rest are ignored */}
            <Route path="/recognition">
              <RecognitionTask options={options} getClass={'panda'}/>
            </Route>

            {/* Note how these two routes are ordered. The more specific
                path="/contact/:id" comes before path="/contact" so that
                route will render when viewing an individual contact */}
            <Route path="/grammar">
              <GrammarTask options={options}/>
            </Route>
            <Route path="/click">
              <ClickPointTask options={options}/>
            </Route>
            <Route path="/choose">
              <ChooseImageTask options={options}/>
            </Route>

            {/* If none of the previous routes render anything,
                this route acts as a fallback.

                Important: A route with path="/" will *always* match
                the URL because all URLs begin with a /. So that's
                why we put this one last of all */}
            <Route path="/">
              <div>
                <nav>
                  <ul>
                    <li>
                      <Link to="/recognition">Recognition Task</Link>
                    </li>
                    <li>
                      <Link to="/grammar">Grammar Task</Link>
                    </li>
                    <li>
                      <Link to="/click">Click Task</Link>
                    </li>
                    <li>
                      <Link to="/choose">Choose Task</Link>
                    </li>
                  </ul>
                </nav>
              </div>
            </Route>
          </Switch>
        </div>
      <Footer/>
    </div>
  );
}

export default App;