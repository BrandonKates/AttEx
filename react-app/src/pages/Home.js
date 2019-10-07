import React from 'react';
import { BrowserRouter, Route, Link } from "react-router-dom";

function Home(){
	return (
	<div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>)
}